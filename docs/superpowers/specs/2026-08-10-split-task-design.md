# Spec: `/split-task` — Notion task decomposer

**Date:** 2026-08-10
**Author:** Felipe Guzmán
**Status:** approved (design), pending implementation plan

## 1. Purpose

`clidrive-developer-skills` is a new suite of Claude Code skills, built on the superpowers
plugin infrastructure, meant to eventually automate all of Felipe's day-to-day work across
Clidrive repos. This spec covers the first skill in that suite: `split-task`.

`split-task` takes one large or ambiguous Notion task and turns it into several small,
well-formed, immediately actionable sub-tasks in the same Notion database. It does not
implement anything, and it does not decide who or what executes the sub-tasks afterward —
that consumer (a person, `/run-task`, or some other future agent) is out of scope here.

This is explicitly **not** related to the existing `/run-task` pipeline
(`~/.claude/skills/run-task/`). That pipeline is untouched by this work.

## 2. Decisions (from brainstorming)

| Decision | Choice |
|---|---|
| Relationship to `/run-task` | None. Totally separate, new pipeline. |
| Sub-task destination | New pages in Notion, related via `Sub-task` / `Parent task`. |
| Trigger | Manual, one task per run: `/split-task <notion-url>`. |
| Reference media (images, links) | Read and interpreted as the deterministic source of business logic — not vague inspiration, not merely acknowledged. |
| Split criterion | Hybrid: primarily functional/business units drawn from the task text + media; light exploration of local Clidrive repos to ground technical scope, not to fully design the solution. |
| Sub-task completeness | "Ready to start": `Problem/Opportunity`, `Solution(s)`, `Design`, `Technical discovery` filled in (plus `QA discovery` when derivable), `Parent task` linked, `Status = Ready to start`. |
| Confirmation gate | Show the proposed split (titles + summaries) and wait for explicit approval before writing anything to Notion. |
| Parent task after split | Comment listing the created sub-tasks with links. `Status` is left untouched. |
| Sub-task sizing | No hard rule (no forced one-repo/one-PR). Judgment-based. |
| Command name | `/split-task` (English command name; conversational Spanish triggers still supported). |

## 3. Environment facts (verified live, 2026-08-10)

### 3.1 Notion data model

- Database "AI Tasks" (`2e17e666162280fbadc2d1cab7e6766f`), data source "AI/Data Tasks" =
  `collection://2e17e666-1622-8144-8f4a-000b4e307e9c`, teamspace JustTech.
- Felipe's user id: `1fbd872b-594c-81a0-9897-00024fb6c534`.
- Relevant schema (confirmed via live `notion-fetch` of the data source, not assumed from
  older documentation):
  - `Task ID` — `auto_increment_id`.
  - `Task name` — `title`.
  - `Status` — `status`, groups: to_do (`To be defined`, `For review`, `Ready to start`),
    in_progress (`On hold`, `Blocked`, `Implementing`, `PR`, `Deployed`), complete (`Done`,
    `Archived`).
  - `Priority` — `select`: `Low`, `Medium`, `High`, `Critic`.
  - `Parent task` — relation, **limit 1**, same data source.
  - `Sub-task` — relation, array, same data source.
  - `AI Projects`, `Sprint` — relations to other data sources.
  - `Stakeholders`, `""` (unnamed field) — `person`.
  - `Github Branch Name`, `Estimates count` — read-only formulas, not settable, not queryable
    via SQL.
- The "Nueva tarea" page template is **blank** (only default properties). The
  `Problem/Opportunity` / `Solution(s)` / `Design` / `Technical discovery` / `QA discovery` /
  `Fixes` section structure is a written convention the team follows, not an enforced
  template. `split-task` must write these headings itself as page content — it cannot rely on
  `template_id` to produce them.
- No Business plan on this workspace: `notion-query-data-sources` (SQL) is unavailable. Use
  `notion-fetch` / `notion-search` / `notion-create-pages` / `notion-update-page` /
  `notion-create-comment`.

### 3.2 Repos available for scope-grounding exploration

Local checkouts under `~/Documents/Clidrive/` (verified present, 2026-08-10): `backend`,
`lib-intelligence`, `svc-intelligence`, `svc-vision`, `lib-vision`, `lib-decision-science`,
`svc-decision-science`, `decision-apps`, `infra`, `clidrive.com`, `connect.clidrive.com`,
`dataflow-automation`, `backfill-scripts`, `scripts-data-analysis`, `rtk`. The skill only
reads these local checkouts (grep/search) — it does not clone or fetch remote repos. This
list can drift as repos are added/removed locally, so the skill should discover it by
listing `~/Documents/Clidrive/` at run time rather than hardcoding these names.

## 4. Pipeline

Runs as a single orchestrating skill in the main session (no subagent dispatch needed — this
is read/analyze/propose/write, not implementation).

1. **Ingest.** `notion-fetch` the task by URL/ID. Extract `Task ID`, `Task name`, `Status`,
   `Priority`, and the full body.
2. **Media pass.** For every embedded image and every reference link in the body:
   - Images: describe what they actually show, at the level of detail needed to derive
     business rules (a screen-flow mockup, a pricing-rule table, an annotated diagram) — not
     "there is an image here."
   - Links: `notion-fetch` (Notion pages) or `WebFetch` (external) their content and extract
     what's relevant.
   - Treat what these show as the deterministic source of business logic. Where the body
     text and a reference disagree or the text is vague, the reference wins.
3. **Hybrid scope exploration.** For each candidate sub-task taking shape, search the local
   repos (grep/Explore) to confirm which repo(s)/component(s) it touches and whether related
   code already exists. This is scoping, not solution design — enough to write a grounded
   `Technical discovery`, not a full implementation plan.
4. **Split.** Produce a list of sub-tasks: each one an independently understandable and
   executable unit of work, driven primarily by the functional/business units found in step 2,
   confirmed against real repo structure from step 3. No fixed count or size rule.
5. **Business-ambiguity check.** If writing a sub-task well requires a business decision that
   isn't in the task text, the media, or derivable from the codebase (a policy call, a price,
   whether something is mandatory, user-facing copy with commercial impact), ask Felipe one
   specific question with a recommended default, wait for the answer, then continue. Never
   guess silently on a business call; never block indefinitely on a technical one — decide
   technical gaps yourself from the exploration in step 3.
6. **Present the plan.** Show the proposed sub-tasks (title + 1-2 line summary each,
   noting which repo(s) each touches) and **stop**. Wait for Felipe's explicit approval before
   writing anything to Notion. If he requests changes, revise the plan and present again.
7. **Create sub-tasks.** On approval, `notion-create-pages` with `parent` =
   `data_source_id: 2e17e666-1622-8144-8f4a-000b4e307e9c` (one call, one page per sub-task).
   For each: `Task name`, `Status = "Ready to start"`, `Priority` (inherited from the parent
   unless the sub-task's own scope clearly warrants a different one), `Parent task` = the
   original task's URL. Body content: `Problem/Opportunity`, `Solution(s)`, `Design`,
   `Technical discovery` (grounded in step 3's findings — real file paths/repo names, not
   generic advice), and `QA discovery` when test cases are derivable from the parent task or
   the media; omit `QA discovery` rather than inventing cases that aren't grounded in
   anything.
8. **Report back.** `notion-create-comment` on the **parent** task listing every created
   sub-task with its link and a one-line summary. Do not change the parent's `Status`. Tell
   Felipe in the chat that the sub-tasks are live and ready to be picked up.

## 5. Error handling

- **Task fetch fails / URL invalid** — report the error, stop; do not fabricate task content.
- **No real split exists** (task is already small enough) — say so instead of forcing a split,
  and leave the task as is.
- **Ambiguous business call** — ask Felipe (step 5); never proceed on a guess for something
  that depends on what the business wants.
- **Notion write fails partway** (some sub-tasks created, then an error) — report exactly
  which sub-tasks were created (with links) and which were not, so nothing is silently lost or
  duplicated on retry.

## 6. Scope

**In v1:** one Notion task in, N Notion sub-tasks out, human-approved before write, parent
commented. Manual trigger only.

**Out of v1:** who picks up the sub-tasks afterward; batch/multi-task mode; polling/cron
triggers; any change to `/run-task`; downloading/attaching media files to sub-tasks (media is
read for context/business logic only, per the brainstorming decision).

## 7. Repo scaffolding (this being the first skill in `clidrive-developer-skills`)

The repo is currently empty (no commits). This work also lays minimal plugin scaffolding
modeled on superpowers' layout, so future skills in the suite drop in the same way:

```
clidrive-developer-skills/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── split-task/
│       ├── SKILL.md
│       └── references/
│           └── notion.md
└── docs/
    └── superpowers/
        └── specs/
            └── 2026-08-10-split-task-design.md
```

`references/notion.md` holds the schema facts from §3.1 (data source id, property names,
status values) and the write patterns from §4 steps 7-8, so `SKILL.md` stays control-flow
only, following the same separation of concerns as the existing `run-task` skill.

## 8. Validation

Before relying on this in real Notion data: run it once against a real, sufficiently large
task with Felipe watching, using the confirmation gate (step 6) as the safety net — if the
proposed split is wrong, reject it there before anything is written. No `--dry-run` flag is
needed for v1 since step 6 already gates every write.
