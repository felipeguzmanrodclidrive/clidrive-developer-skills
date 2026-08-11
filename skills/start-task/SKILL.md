---
name: start-task
description: Use to start a Notion sub-task that is Ready to start — create a git worktree per affected repo on the task's branch and move it to Implementing. Triggers on "/start-task <notion-url>", "empieza esta tarea", "arranca la subtarea".
---

# /start-task

Take one Notion task that is Ready to start and move it into Implementing, with a git
worktree created for every repository the task touches. This skill does not plan, does not
implement, and does not open a PR.

## Input

`/start-task <notion-url-or-id>` — optional. Without an argument, the skill lists the tasks
currently in Ready to start and lets the user pick one.

## Procedure

1. **Resolve config.** Read `CLIDRIVE_REPOS_ROOT` and `CLIDRIVE_WORKTREES_ROOT`, following
   the defaults in `references/worktrees.md`. If `CLIDRIVE_REPOS_ROOT` is not set, or it is
   set but contains no repository checkouts, report the exact `export CLIDRIVE_REPOS_ROOT=...`
   command needed and stop. Do not guess a path.

2. **Resolve the task.** With an argument, fetch the task by URL or ID using `notion-fetch`
   as described in `../_shared/notion.md`. Without one, list the tasks in Ready to start and
   let the user pick, also per `../_shared/notion.md`.

3. **Guards.** Both conditions must hold before continuing.
   - `Status` is exactly "Ready to start".
   - `Github Branch Name` is non-empty.

   If either fails, report which one and stop. Never derive a branch name yourself and never
   attempt to write `Github Branch Name`; it is a read-only formula.

4. **Announce.** Once the guards pass, say "Using start-task to start <Task name> (<Task ID>)
   on branch <branch>."

5. **Pick repos.** List the repository checkouts under `CLIDRIVE_REPOS_ROOT` and let the user
   multi-select which ones this task affects.

6. **Create worktrees.** For each selected repo, follow `references/worktrees.md`, which
   delegates the actual worktree operations to `superpowers:using-git-worktrees`. Reuse an
   existing branch and worktree if one is already there instead of recreating it.

7. **Move state.** Call `notion-update-page` to set `Status` to "Implementing", per
   `../_shared/notion.md`.

8. **Report.** Summarize what happened for the user: each repo mapped to its worktree path,
   the branch name, and the suggested next step (start implementing in the created
   worktrees).

## Error handling

- If the config guard fails, report the missing or empty environment variable and the export
  command to fix it, then stop before touching Notion.
- If the task fetch fails or the URL is invalid, report the error and stop; do not fabricate
  task content.
- If a guard fails (wrong Status, empty branch name), report which one and stop without
  creating any worktree or writing to Notion.
- If worktree creation fails for one or more repos, report exactly which repos succeeded and
  which failed, and do not move Status to Implementing until every selected repo has a
  worktree.
- If the Notion status update fails after worktrees were created, report the worktrees that
  now exist and the failed status update separately, so the user can retry the update without
  redoing the worktrees.

## Scope

Starts one task at a time and stops at Implementing. It does not plan the work, does not
implement it, does not open a pull request, and does not move Status past Implementing. No
batch mode and no polling or cron trigger.
