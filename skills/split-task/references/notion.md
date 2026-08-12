# Notion I/O for split-task

General Notion facts and I/O patterns live in `skills/_shared/notion.md`. This file documents split-task-specific write patterns.

## Creating sub-tasks

Set `Parent task` to the original task's URL. Write the body content with headings `## Problem/Opportunity`, `## Solution(s)`, `## Design`, `## Technical discovery` (and `## QA discovery` when real test cases are derivable), each as direct prose grounded in findings — no placeholders.

## Reporting back

Comment on the parent task's page listing every created sub-task with its title and link. Do not change the parent's Status.
