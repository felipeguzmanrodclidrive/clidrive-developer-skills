# Worktrees Convention

This document defines how `start-task` creates and manages git worktrees across multiple repositories.

## Configuration

The worktree system uses two environment variables, both resolved at startup:

- `CLIDRIVE_REPOS_ROOT` defaults to `~/Documents/REPOS` if not set. This is the parent directory containing all cloned repositories (lib-intelligence, backend, etc.).
- `CLIDRIVE_WORKTREES_ROOT` defaults to `$CLIDRIVE_REPOS_ROOT/.worktrees` if not set. This is where all worktrees are created.

## Layout

Worktrees are organized by branch and repository. Each repository checked out in a worktree occupies a folder at:

```
$CLIDRIVE_WORKTREES_ROOT/<branch>/<repo>/
```

All repositories belonging to a single task share the branch folder, grouping related work together.

## Branch Naming

The branch name comes from Notion in the `Github Branch Name` field. This name must be identical across all repositories involved in the task. Fetch updates from the remote first. For a new branch, create the worktree based off the repository's default branch (usually `main`). If the branch already exists, attach to it instead.

## Idempotency

If the branch already exists in a repository's worktree folder, attach the worktree to it and leave it as-is. Nothing is recreated, refreshed, or deleted.

## Delegation

Do not run raw `git worktree` commands inside the skill. Instead, invoke the `superpowers:using-git-worktrees` skill once per repository. Pass the repository name, branch name, and local worktree path to this skill; it handles all worktree operations and ensures consistency.
