# clidrive-developer-skills

A collection of skills for driving the Clidrive development workflow through Notion task lifecycle automation.

## Configuration

The skills in this repository use environment variables to locate your local checkouts and configure worktree placement. These variables are per-developer and should never be committed to the repository.

### Environment Variables

**`CLIDRIVE_REPOS_ROOT`**

The root directory where your local checkouts of Clidrive repositories live. The skills scan this directory to discover available repos (backend, lib-intelligence, svc-intelligence, etc.).

- Default when unset: `~/Documents/REPOS`
- Example: `/Users/yourname/Documents/REPOS` or `$HOME/dev/repos`

**`CLIDRIVE_WORKTREES_ROOT`**

The root directory where git worktrees are created when starting tasks. Worktrees are organized by branch name and repository: `$CLIDRIVE_WORKTREES_ROOT/<branch>/<repo>/`.

- Default when unset: `$CLIDRIVE_REPOS_ROOT/.worktrees`
- Example: `/Users/yourname/Documents/REPOS/.worktrees` or `$HOME/.worktrees`

### Setup

Add these environment variables to your shell configuration file (`.bashrc`, `.zshrc`, or equivalent):

```bash
export CLIDRIVE_REPOS_ROOT=$HOME/Documents/REPOS
export CLIDRIVE_WORKTREES_ROOT=$CLIDRIVE_REPOS_ROOT/.worktrees
```

These variables are read at skill startup. If `CLIDRIVE_REPOS_ROOT` is not set or does not exist, the skill will report how to configure it and stop before making any changes.
