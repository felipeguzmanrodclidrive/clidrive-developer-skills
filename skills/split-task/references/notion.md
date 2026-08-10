# Notion I/O for split-task

## Identifiers

Data source: `collection://2e17e666-1622-8144-8f4a-000b4e307e9c` ("AI/Data Tasks", database
"AI Tasks", teamspace JustTech). There is no Business plan on this workspace, so
`notion-query-data-sources` (SQL) is unavailable; use `notion-fetch`, `notion-search`,
`notion-create-pages`, `notion-update-page`, and `notion-create-comment` instead.

## Schema

- `Task ID` — auto increment id, read-only.
- `Task name` — title.
- `Status` — status property. To-do group: To be defined, For review, Ready to start.
  In-progress group: On hold, Blocked, Implementing, PR, Deployed. Complete group: Done,
  Archived.
- `Priority` — select: Low, Medium, High, Critic.
- `Parent task` — relation, limit 1, same data source.
- `Sub-task` — relation, array, same data source.
- `AI Projects`, `Sprint` — relations to other data sources; leave unset unless the parent's
  values are clearly known and relevant.
- `Github Branch Name`, `Estimates count` — read-only formulas; never try to set them.

The "Nueva tarea" page template is blank aside from default properties. The
Problem/Opportunity, Solution(s), Design, Technical discovery, QA discovery, Fixes section
structure is a written convention, not an enforced template — write these headings directly
into the page content rather than relying on a template.

## Ingest

Fetch the task with `notion-fetch` using the URL or ID. Read Task ID, Task name, Status,
Priority, and the full body content, including embedded images and links.

## Creating sub-tasks

Use `notion-create-pages` with
`parent: {type: "data_source_id", data_source_id: "2e17e666-1622-8144-8f4a-000b4e307e9c"}`
and one entry per sub-task in the same call. For each page:

- `properties`: `Task name` (title), `Status: "Ready to start"`, `Priority`, `Parent task`
  set to the original task's URL.
- `content`: markdown body with `## Problem/Opportunity`, `## Solution(s)`, `## Design`,
  `## Technical discovery` (and `## QA discovery` when there are real test cases to write),
  each written as direct prose grounded in what was actually found — no placeholders.

## Reporting back

Use `notion-create-comment` on the parent task's page id with a markdown comment listing
every created sub-task's title and link. Do not call `notion-update-page` on the parent's
Status.
