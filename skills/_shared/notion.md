# Notion I/O reference

Canonical schema and patterns for AI Tasks database, shared by `split-task` and `start-task` skills.

## Identifiers

Data source: `collection://2e17e666-1622-8144-8f4a-000b4e307e9c` ("AI Tasks" database, teamspace JustTech).

No Business plan is available on this workspace, so `notion-query-data-sources` (SQL) is unavailable. Use `notion-fetch`, `notion-search`, `notion-update-page`, `notion-create-pages`, and `notion-create-comment` instead.

## Schema

- `Task ID` — auto increment id, read-only.
- `Task name` — title.
- `Status` — status property with groups:
  - To-do group: To be defined, For review, Ready to start.
  - In-progress group: On hold, Blocked, Implementing, PR, Deployed.
  - Complete group: Done, Archived.
- `Priority` — select: Low, Medium, High, Critic.
- `Parent task` — relation, limit 1, same data source.
- `Sub-task` — relation, array, same data source.
- `Github Branch Name` — read-only formula; read this value, never try to set it.

## Patterns

### Fetch a task

Use `notion-fetch` with the task's URL or ID. Read Task ID, Task name, Status, Priority, and full body content.

### List tasks by Status

Use `notion-search` or `notion-fetch` with filter on the data source by Status value. The Status property is a grouped select with distinct values per group.

### Update task Status

Use `notion-update-page` with the task's ID and new Status value. This is the only mutation performed on task properties by these skills.

### Create sub-tasks

Use `notion-create-pages` with `parent: {type: "data_source_id", data_source_id: "2e17e666-1622-8144-8f4a-000b4e307e9c"}` and one entry per sub-task. For each page, set `Task name` (title), `Status: "Ready to start"`, and `Priority`.

### Comment on a task

Use `notion-create-comment` with the task's page ID. This is used to report progress back to the parent task without modifying task properties.
