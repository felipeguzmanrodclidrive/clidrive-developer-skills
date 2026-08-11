---
name: clidrive-backend-api
description: Use when a task touches the Clidrive/backend API (endpoints, routes, DTOs, scopes) or its database schema (Prisma models, fields, relations, enums) — including when lib-intelligence or svc-intelligence need to know which backend endpoint to call or the shape of data the backend returns.
---

# Clidrive backend — API and database

Compact reference generated from the `Clidrive/backend` repo (NestJS 11 + `@nestjs/swagger` + Prisma 5 on PostgreSQL).

## When to use each resource

- **API questions** (which endpoints exist, method, route, which DTO it takes, what scopes it requires, which controller file it lives in) — read `references/endpoints.md`. Grouped by Swagger tag.
- **Data questions** (which tables/models exist, fields, types, relations, enums, PK/unique/default) — read `references/db-schema.md`. Covers Prisma models, views, and enums.
- **Real implementation** (how an endpoint is actually resolved, which use case/service runs, who calls what) — query the codebase-memory-mcp graph for the backend project (`search_graph`, `trace_path`, `get_code_snippet`) instead of grepping files by hand.

Both references are compact indexes. When you need the exact detail of one endpoint or model, use the reference to locate the file, then open the real file in the backend repo or query the graph.

## Reading endpoints.md

Each row is one endpoint. Routes already include their version prefix (`/v1/...`, `/ai/v1/...`) exactly as declared by `@Controller`. The Scopes column lists the permissions required by `@Scopes` (empty if the controller does not restrict by scope). The File column points at the controller where it is defined.

## Reading db-schema.md

Models are listed alphabetically with an index at the top. Per-field attributes: PK, unique, relation, default. Many domain models use a `Prisma...` prefix; legacy core tables are lowercase (`clients`, `deals`, `invoices`, ...). Views are listed alongside models and marked as such.

## Regenerating after backend changes

The references are generated from code — they go stale as soon as the backend changes. Regenerate them from your local clone of `Clidrive/backend`:

```bash
cd ~/Documents/Clidrive/backend && git pull --ff-only
SKILL=~/.claude/skills/clidrive-backend-api
python3 "$SKILL/references/gen_endpoints.py" "$SKILL/references/endpoints.md" --repo ~/Documents/Clidrive/backend
python3 "$SKILL/references/gen_db_schema.py" "$SKILL/references/db-schema.md" --schema ~/Documents/Clidrive/backend/database/schema.prisma
codebase-memory-mcp cli index_repository --repo_path ~/Documents/Clidrive/backend
```

Both scripts default to `~/Documents/Clidrive/backend`, so the `--repo`/`--schema` flags are only needed if your clone lives elsewhere. Re-run this after pulling backend changes rather than editing the generated `.md` files by hand.
