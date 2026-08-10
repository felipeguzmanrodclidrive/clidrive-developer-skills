---
name: split-task
description: Use when a Notion task is too large or ambiguous to work as one unit and needs to become several smaller, ready-to-start sub-tasks. Triggers on "/split-task <notion-url>", "parte esta tarea", "divide esta tarea en subtareas".
---

# /split-task

Take one large or ambiguous Notion task and turn it into several small, well-formed,
immediately actionable sub-tasks in the same Notion database. This skill does not implement
anything and does not decide who picks up the sub-tasks afterward.

Announce at start: "Using split-task to break down <Task name> (<Task ID>)."

## Input

`/split-task <notion-url-or-id>` — one task per run.

## Procedure

1. **Ingest.** Follow `references/notion.md` to fetch the task and extract Task ID, Task
   name, Status, Priority, and the full body.

2. **Media pass.** For every embedded image and every reference link in the body, interpret
   it rather than just noting it exists. Describe what images actually show, at the level of
   detail needed to derive business rules — a screen-flow mockup, a pricing-rule table, an
   annotated diagram. Fetch and read what reference links point to (`notion-fetch` for Notion
   pages, `WebFetch` for anything external). Treat what these show as the deterministic
   source of business logic; where the body text and a reference disagree, the reference
   wins.

3. **Scope exploration.** For each candidate sub-task taking shape, search the local repos
   under `~/Documents/Clidrive/` (list them at run time rather than assuming a fixed set) to
   confirm which repo(s) or component(s) it touches and whether related code already exists.
   This grounds `Technical discovery` for each sub-task; it is not full solution design.

4. **Split.** Produce a list of sub-tasks, each an independently understandable and
   executable unit of work, driven primarily by the functional/business units found in the
   media pass and confirmed against real repo structure. There is no fixed count or size
   rule — judge each case.

5. **Business-ambiguity check.** If writing a sub-task well needs a business decision that is
   not in the task text, the media, or the codebase — a policy call, a price, whether
   something is mandatory, user-facing copy with commercial impact — ask the person who
   triggered the run one specific question with a recommended default, wait for the answer,
   then continue. Decide technical gaps yourself instead of asking.

6. **Present the plan.** Show the proposed sub-tasks — title and a one- or two-line summary
   each, noting which repo(s) it touches — and stop. Wait for explicit approval before
   writing anything to Notion. If changes are requested, revise the plan and present it
   again.

7. **Create the sub-tasks.** Once approved, follow `references/notion.md` to create each
   sub-task page: `Task name`, `Status` set to "Ready to start", `Priority` inherited from
   the parent unless the sub-task's scope clearly warrants a different one, `Parent task` set
   to the original task. Body content covers Problem/Opportunity, Solution(s), Design, and
   Technical discovery grounded in the scope exploration — real file paths and repo names,
   not generic advice — plus QA discovery when test cases are actually derivable; omit it
   rather than inventing cases.

8. **Report back.** Comment on the parent task listing every created sub-task with its link
   and a one-line summary, following `references/notion.md`. Leave the parent's Status
   untouched. Report in the chat that the sub-tasks are live and ready to be picked up.

## Error handling

- If the task fetch fails or the URL is invalid, report the error and stop; do not fabricate
  task content.
- If the task is already small enough that no real split makes sense, say so instead of
  forcing one, and leave the task as is.
- If a Notion write fails partway through creating sub-tasks, report exactly which sub-tasks
  were created (with links) and which were not, so nothing is silently lost or duplicated on
  retry.

## Scope

One Notion task in, several Notion sub-tasks out, always approved by a person before
anything is written. No batch mode, no polling/cron trigger, no downloading or attaching
media files to sub-tasks — media is read for context and business logic only, never
attached.
