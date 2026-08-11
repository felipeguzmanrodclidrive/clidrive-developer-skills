# Spec: start-task Skill

## Overview

`start-task` is the first stage of the code-generation leg in the Notion task lifecycle. It takes a ready sub-task, materializes the work environment (worktrees), and moves it to `Implementing`. It does not plan or implement anything.

## Decisions

| Decision | Choice |
|---|---|
| Trigger | `/start-task [<notion-url>]`. With a URL or ID it starts that task; without an argument it lists "Ready to start" tasks and the user picks one. One task per run. |
| Repo detection | User picks. The skill lists checkouts under `$CLIDRIVE_REPOS_ROOT`; the user selects which repos the sub-task touches. No graph inference. |
| Multi-repo support | Supported. If the sub-task touches several repos, a worktree is created in each. |
| Materialization | Isolated git worktree per repo, delegating to `superpowers:using-git-worktrees`. Never in-place checkout. |
| Branch name | The Notion `Github Branch Name` value, identical across all repos. |
| Path configuration | Environment variables so each developer keeps their own layout without touching versioned code: `CLIDRIVE_REPOS_ROOT` (checkout root) and `CLIDRIVE_WORKTREES_ROOT` (worktree root), with sane defaults. |
| Guards | Strict. `Status` must equal "Ready to start" and `Github Branch Name` must be non-empty; on either failure, report and stop. No branch-name fallback. |
| Notion end state | Only `Status = Implementing` via `notion-update-page`. No task comment. |
| Chat output | Report of created worktrees (repo to path), branch, and next step. |
| Implementation approach | Thin control-flow that delegates git to `superpowers:using-git-worktrees`; no reimplementation of worktree mechanics. |

## Environment Facts

### Notion Data Source

Data source `collection://2e17e666-1622-8144-8f4a-000b4e307e9c`, database "AI Tasks", teamspace JustTech. No Business plan, so `notion-query-data-sources` (SQL) is unavailable; use `notion-fetch`, `notion-search`, `notion-update-page`.

Relevant fields:
- `Status` (status): to_do group has "To be defined", "For review", "Ready to start"; in_progress group has "On hold", "Blocked", "Implementing", "PR", "Deployed"; complete group has "Done", "Archived".
- `Github Branch Name`: read-only formula. The skill reads it, never writes it.
- `Task ID` (auto_increment), `Task name` (title), `Priority` (select), `Parent task` (relation, limit 1), `Sub-task` (relation array).

### Configuration

The repo is used by several developers with different layouts, so paths are never hardcoded:

- `CLIDRIVE_REPOS_ROOT`: root where checkouts live. Default when unset is `~/Documents/REPOS`.
- `CLIDRIVE_WORKTREES_ROOT`: root where worktrees are created. Default when unset is `$CLIDRIVE_REPOS_ROOT/.worktrees`.

The skill reads these at startup, applies defaults, and verifies `CLIDRIVE_REPOS_ROOT` exists and contains checkouts before continuing; otherwise it reports how to set it and stops.

### Local Repos

Checkouts under `$CLIDRIVE_REPOS_ROOT` (e.g., backend, lib-intelligence, svc-intelligence). The skill discovers the list by scanning that root at run time; it does not hardcode names.

### Worktrees

- Worktree root at `$CLIDRIVE_WORKTREES_ROOT`, grouped by branch: `$CLIDRIVE_WORKTREES_ROOT/<branch>/<repo>/`.
- Base: the repo default branch (main) after fetch; resolved by `using-git-worktrees`.
- Idempotent: if the branch already exists in a repo, the worktree attaches to it; nothing is recreated or deleted.

## Pipeline

Runs as an orchestrating skill in the main session (no subagents: read, validate, ask, create worktrees, write state).

1. Resolve the task. With an argument, `notion-fetch` by URL or ID. Without one, list "Ready to start" tasks from the data source and let the user pick one.
2. Guards. Verify `Status == "Ready to start"` and `Github Branch Name` non-empty. On either failure, report and stop.
3. Announce. "Using start-task to start `<Task name>` (`<Task ID>`) on branch `<branch>`."
4. Pick repos. Resolve `CLIDRIVE_REPOS_ROOT` (with default), list its checkouts, and let the user select which repos the sub-task touches (multi-select).
5. Create worktrees. For each selected repo, invoke `superpowers:using-git-worktrees` to create a worktree at `$CLIDRIVE_WORKTREES_ROOT/<branch>/<repo>/` on branch `<branch>`. Reuse the branch if it already exists.
6. Move state. `notion-update-page` to set `Status = Implementing`.
7. Report. In chat: created worktrees (repo to path), branch, and next step.

## Error Handling

- `CLIDRIVE_REPOS_ROOT` missing or empty: report how to set the variable (name and an export example) and stop before touching the task.
- Fetch fails or invalid URL: report and stop; do not fabricate task content.
- Guard fails (Status not "Ready to start" or missing Github Branch Name): report exactly which guard failed and stop. The guard makes re-runs idempotent; a task already in "Implementing" is blocked here.
- Worktree creation fails: report which repos got a worktree and which failed; stop before touching Notion so state never runs ahead of the real environment.
- Notion write fails after worktrees exist: report which worktrees were created so a retry leaves nothing silently orphaned.

## Scaffolding

Directory layout:

```
clidrive-developer-skills/
└── skills/
    ├── _shared/
    │   └── notion.md          (shared Notion I/O, data source, schema, patterns)
    ├── split-task/            (existing; its references/notion.md now points to _shared)
    └── start-task/
        ├── SKILL.md           (control flow and guards)
        ├── SPEC.md            (this spec)
        └── references/
            └── worktrees.md   (path/name convention + using-git-worktrees usage)
```

Collateral change in `split-task`: replace the hardcoded `~/Documents/Clidrive/` path with `$CLIDRIVE_REPOS_ROOT` (same config as `start-task`) in its SKILL.md and SPEC.md, and repoint its Notion reference to `skills/_shared/notion.md`.

## Out of Scope for v1

Planning, implementing, reviewing, or opening a PR; the `build-task` orchestrator; moving to states past "Implementing"; commenting on the task; assigning stakeholders; batch mode; cron triggers.
