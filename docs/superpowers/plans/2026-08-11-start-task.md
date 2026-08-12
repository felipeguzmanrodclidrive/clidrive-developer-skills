# start-task Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship the `start-task` skill that takes a `Ready to start` Notion sub-task, creates a git worktree per selected repo on the Notion branch name, and moves the task to `Implementing`.

**Architecture:** Thin control-flow skill in the main session. It delegates git worktree mechanics to `superpowers:using-git-worktrees` and Notion I/O to a repo-shared reference. No subagents, no code generation — read/validate/ask/create worktrees/write state.

**Tech Stack:** Claude Code skills (Markdown SKILL.md + references), Notion MCP connector, `superpowers:using-git-worktrees`, git.

## Global Constraints

- All skill content in English. Direct, instructive prose; no filler, no emphasis labels, no `Label: value` shapes.
- Paths never hardcoded. Read `CLIDRIVE_REPOS_ROOT` (default `~/Documents/REPOS`) and `CLIDRIVE_WORKTREES_ROOT` (default `$CLIDRIVE_REPOS_ROOT/.worktrees`).
- Notion data source: `collection://2e17e666-1622-8144-8f4a-000b4e307e9c`. No SQL (`notion-query-data-sources` unavailable); use `notion-fetch`, `notion-search`, `notion-update-page`.
- Branch name always the Notion `Github Branch Name` value (read-only formula); never derived, never written back.
- Guards strict: `Status == "Ready to start"` and non-empty `Github Branch Name`, else report and stop.
- SKILL.md authoring follows `superpowers:writing-skills` conventions (frontmatter `name` + `description` with triggers; body is control flow, not internals).

**Verification note:** These are prose artifacts. Each task ends with an acceptance check (a concrete, inspectable condition), not a unit test. A single live validation run (Task 6) is the end-to-end gate.

---

### Task 1: Shared Notion reference

**Files:**
- Create: `skills/_shared/notion.md`

**Interfaces:**
- Produces: the canonical Notion facts and I/O patterns consumed by `split-task` and `start-task` — data source id, `Status` values, `Github Branch Name` (read-only), and the `notion-fetch` / list-by-Status / `notion-update-page` patterns.

- [ ] **Step 1: Write `skills/_shared/notion.md`**

Content, in English:
- Identifiers: data source `collection://2e17e666-1622-8144-8f4a-000b4e307e9c`, database "AI Tasks", teamspace JustTech. No Business plan → no SQL; use `notion-fetch`, `notion-search`, `notion-update-page`, `notion-create-pages`, `notion-create-comment`.
- Schema: `Task ID` (auto id, read-only), `Task name` (title), `Status` (status; groups listed), `Priority` (select), `Parent task` (relation limit 1), `Sub-task` (relation array), `Github Branch Name` (read-only formula — read, never set).
- Patterns: fetch a task by URL/ID; list tasks by `Status` via `notion-search` / `notion-fetch` of the data source; set `Status` via `notion-update-page`.

- [ ] **Step 2: Acceptance check**

Confirm the file states the data source id, lists every `Status` value, marks `Github Branch Name` read-only, and contains no developer-specific paths. Grep must return nothing: `grep -nE '/Users/|Documents/Clidrive' skills/_shared/notion.md`.

- [ ] **Step 3: Commit**

```bash
git add skills/_shared/notion.md
git commit -m "feat(skills): add shared Notion I/O reference"
```

---

### Task 2: Repoint split-task to the shared reference

**Files:**
- Modify: `skills/split-task/references/notion.md`
- Modify: `skills/split-task/SKILL.md`
- Modify: `skills/split-task/SPEC.md`

**Interfaces:**
- Consumes: `skills/_shared/notion.md` from Task 1.

- [ ] **Step 1: Replace `skills/split-task/references/notion.md` body**

Replace its content with a one-line pointer: the Notion facts and I/O patterns now live in `skills/_shared/notion.md`; keep here only any split-task-specific write detail (sub-task creation with `Parent task`, parent comment) that is not general.

- [ ] **Step 2: Fix hardcoded repo path in split-task**

In `skills/split-task/SKILL.md` and `skills/split-task/SPEC.md`, replace every `~/Documents/Clidrive/` with `$CLIDRIVE_REPOS_ROOT` and state the default (`~/Documents/REPOS`).

- [ ] **Step 3: Acceptance check**

`grep -rnE 'Documents/Clidrive' skills/split-task` returns nothing. The split-task references file no longer duplicates the schema block (it points to `_shared`).

- [ ] **Step 4: Commit**

```bash
git add skills/split-task
git commit -m "refactor(split-task): use shared Notion ref and CLIDRIVE_REPOS_ROOT"
```

---

### Task 3: Worktrees reference

**Files:**
- Create: `skills/start-task/references/worktrees.md`

**Interfaces:**
- Produces: the worktree path/name convention and the exact way `start-task` invokes `superpowers:using-git-worktrees`.

- [ ] **Step 1: Write `skills/start-task/references/worktrees.md`**

Content, in English:
- Config: `CLIDRIVE_REPOS_ROOT` (default `~/Documents/REPOS`), `CLIDRIVE_WORKTREES_ROOT` (default `$CLIDRIVE_REPOS_ROOT/.worktrees`). Resolve defaults at startup.
- Layout: one worktree per selected repo at `$CLIDRIVE_WORKTREES_ROOT/<branch>/<repo>/`, grouping all repos of one task under the branch folder.
- Branch: the Notion `Github Branch Name`, identical across repos. Base off the repo default branch (`main`) after fetch.
- Idempotency: if `<branch>` already exists in a repo, attach the worktree to it; never recreate or delete.
- Delegation: invoke `superpowers:using-git-worktrees` once per repo; do not run raw `git worktree` in the skill.

- [ ] **Step 2: Acceptance check**

The file names both env vars with defaults, the `$CLIDRIVE_WORKTREES_ROOT/<branch>/<repo>/` layout, the idempotency rule, and the delegation to `using-git-worktrees`. `grep -nE '/Users/' skills/start-task/references/worktrees.md` returns nothing.

- [ ] **Step 3: Commit**

```bash
git add skills/start-task/references/worktrees.md
git commit -m "feat(start-task): add worktrees convention reference"
```

---

### Task 4: start-task SKILL.md

**Files:**
- Create: `skills/start-task/SKILL.md`

**Interfaces:**
- Consumes: `skills/_shared/notion.md` (Task 1), `skills/start-task/references/worktrees.md` (Task 3), `superpowers:using-git-worktrees`.

- [ ] **Step 1: Write frontmatter**

```markdown
---
name: start-task
description: Use to start a Notion sub-task that is Ready to start — create a git worktree per affected repo on the task's branch and move it to Implementing. Triggers on "/start-task <notion-url>", "empieza esta tarea", "arranca la subtarea".
---
```

- [ ] **Step 2: Write the control flow**

Body, in English, as a numbered procedure matching spec §4:
1. Resolve config: read `CLIDRIVE_REPOS_ROOT` / `CLIDRIVE_WORKTREES_ROOT` with defaults; if `CLIDRIVE_REPOS_ROOT` is missing or has no checkouts, report how to `export` it and stop.
2. Resolve the task: with an argument, `notion-fetch` by URL/ID; without one, list `Ready to start` tasks and let the user pick. See `../_shared/notion.md`.
3. Guards: `Status == "Ready to start"` and non-empty `Github Branch Name`, else report which failed and stop.
4. Announce: `Using start-task to start <Task name> (<Task ID>) on branch <branch>.`
5. Pick repos: list checkouts under `CLIDRIVE_REPOS_ROOT`; user multi-selects.
6. Create worktrees: per selected repo, follow `references/worktrees.md` (delegates to `superpowers:using-git-worktrees`); reuse an existing branch.
7. Move state: `notion-update-page` → `Status = Implementing`.
8. Report: created worktrees (repo → path), branch, next step.

Include an Error handling section mirroring spec §5 and a Scope section stating v1 boundaries (no planning/implementing/PR; only up to `Implementing`).

- [ ] **Step 3: Acceptance check**

Frontmatter has `name` and a trigger-based `description`. Body contains all eight steps, both guards, the config-missing guard, and references `../_shared/notion.md` and `references/worktrees.md`. No `→`, no `Label:` shapes, no ALL-CAPS emphasis. `grep -nE '/Users/|Documents/Clidrive' skills/start-task/SKILL.md` returns nothing.

- [ ] **Step 4: Commit**

```bash
git add skills/start-task/SKILL.md
git commit -m "feat(start-task): add SKILL.md control flow"
```

---

### Task 5: start-task SPEC.md and README config docs

**Files:**
- Create: `skills/start-task/SPEC.md`
- Create or Modify: `README.md`

**Interfaces:**
- Consumes: the approved design spec `docs/superpowers/specs/2026-08-11-start-task-design.md`.

- [ ] **Step 1: Write `skills/start-task/SPEC.md`**

A condensed version of the design spec: Decisions table, Environment facts (Notion, config env vars, repos, worktrees), Pipeline, Error handling, Scaffolding, Out of v1. English, no placeholders.

- [ ] **Step 2: Document env vars in `README.md`**

Add a Configuration section: `CLIDRIVE_REPOS_ROOT` and `CLIDRIVE_WORKTREES_ROOT`, their meaning, defaults, and an `export` example for shell rc. State they are per-developer and never committed.

- [ ] **Step 3: Acceptance check**

`README.md` names both env vars with defaults and an `export` example. `SPEC.md` has no "TBD"/"TODO": `grep -nE 'TBD|TODO' skills/start-task/SPEC.md` returns nothing.

- [ ] **Step 4: Commit**

```bash
git add skills/start-task/SPEC.md README.md
git commit -m "docs(start-task): add SPEC and env-var configuration docs"
```

---

### Task 6: Live validation

**Files:** none (verification only).

- [ ] **Step 1: Dry structural pass**

Confirm the tree matches spec §6: `skills/_shared/notion.md`, `skills/start-task/{SKILL.md,SPEC.md,references/worktrees.md}`, updated `skills/split-task/*`. Every internal link resolves. Repo-wide check returns nothing: `grep -rnE 'Documents/Clidrive|/Users/[a-z]+/Documents/REPOS' skills`.

- [ ] **Step 2: Run against a real task**

With someone watching, run `/start-task <url>` on a real `Ready to start` sub-task. Confirm in order: config resolves, guards pass, repo pick works, a worktree appears at `$CLIDRIVE_WORKTREES_ROOT/<branch>/<repo>/` on `<branch>`, and Notion `Status` becomes `Implementing`. Re-run the same task and confirm the guard now blocks it (idempotency).

- [ ] **Step 3: Negative checks**

Run against a task not in `Ready to start` and confirm it stops at the guard. Temporarily unset `CLIDRIVE_REPOS_ROOT` to a bad path and confirm the config guard reports and stops.

---

## Self-Review

**Spec coverage:** Trigger both modes (T4 step 2.2), repo pick (T4 step 2.5), multi-repo worktrees (T3, T4 step 2.6), branch from Notion (T3), env-var config (T3, T4 step 2.1, T5), strict guards (T4 step 2.3), Notion end state (T4 step 2.7), shared Notion ref (T1, T2), split-task path fix (T2), scaffolding (all), validation (T6). No gaps.

**Placeholder scan:** No "TBD"/"TODO"/"handle edge cases". Acceptance checks are concrete greps or inspections.

**Type consistency:** Env var names (`CLIDRIVE_REPOS_ROOT`, `CLIDRIVE_WORKTREES_ROOT`), branch source (`Github Branch Name`), path layout (`$CLIDRIVE_WORKTREES_ROOT/<branch>/<repo>/`), and data source id are used identically across Tasks 1–6.
