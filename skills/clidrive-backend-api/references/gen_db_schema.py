#!/usr/bin/env python3
"""Extract the Prisma schema of Clidrive/backend into a Markdown reference.

Usage: python3 gen_db_schema.py <output.md> [--schema <path-to-schema.prisma>]
"""
import argparse
import re
from pathlib import Path

BLOCK_RE = re.compile(r"^(model|view|enum)\s+(\w+)\s*\{", re.MULTILINE)


def split_blocks(text: str):
    matches = list(BLOCK_RE.finditer(text))
    blocks = []
    for i, m in enumerate(matches):
        kind, name = m.group(1), m.group(2)
        start = m.end()
        end = text.find("\n}", start)
        body = text[start:end]
        blocks.append((kind, name, body))
    return blocks


def balanced_paren_arg(text: str, open_pos: int) -> str:
    depth = 0
    for i in range(open_pos, len(text)):
        if text[i] == "(":
            depth += 1
        elif text[i] == ")":
            depth -= 1
            if depth == 0:
                return text[open_pos + 1 : i]
    return text[open_pos + 1 :]


def parse_field_line(line: str):
    line = line.strip()
    if not line or line.startswith("//") or line.startswith("@@"):
        return None
    m = re.match(r"(\w+)\s+([\w.]+)(\[\])?(\?)?\s*(.*)", line)
    if not m:
        return None
    field_name, base_type, is_array, is_nullable, rest = m.groups()
    attrs = []
    if "@id" in rest:
        attrs.append("PK")
    if re.search(r"@unique\b", rest):
        attrs.append("unique")
    if "@relation" in rest:
        attrs.append("relation")
    default_m = re.search(r"@default\(", rest)
    if default_m:
        attrs.append(f"default={balanced_paren_arg(rest, default_m.end() - 1)}")
    return {
        "field": field_name,
        "type": base_type + ("[]" if is_array else "") + ("?" if is_nullable else ""),
        "attrs": ", ".join(attrs),
    }


def table_name(kind: str, name: str, body: str):
    m = re.search(r'@@map\("([^"]+)"\)', body)
    return m.group(1) if m else name


def render_model(kind: str, name: str, body: str) -> list[str]:
    fields = [parse_field_line(l) for l in body.splitlines()]
    fields = [f for f in fields if f]
    lines = [f"### {name} ({kind}, table: `{table_name(kind, name, body)}`)", ""]
    lines.append("| Field | Type | Attributes |")
    lines.append("|---|---|---|")
    for f in fields:
        lines.append(f"| {f['field']} | {f['type']} | {f['attrs']} |")
    lines.append("")
    return lines


def render_enum(name: str, body: str) -> list[str]:
    values = [
        l.strip()
        for l in body.splitlines()
        if l.strip() and not l.strip().startswith(("//", "@@"))
    ]
    return [f"- **{name}**: {', '.join(values)}"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument(
        "--schema", default=str(Path.home() / "Documents/Clidrive/backend/database/schema.prisma")
    )
    args = parser.parse_args()

    schema_path = Path(args.schema).expanduser().resolve()
    text = schema_path.read_text(encoding="utf-8", errors="replace")
    blocks = split_blocks(text)

    models = sorted([b for b in blocks if b[0] in ("model", "view")], key=lambda b: b[1])
    enums = sorted([b for b in blocks if b[0] == "enum"], key=lambda b: b[1])

    lines = [
        "# Clidrive backend — database schema",
        "",
        f"Generated from `{schema_path}` by `gen_db_schema.py`. "
        f"{sum(1 for b in models if b[0] == 'model')} models, "
        f"{sum(1 for b in models if b[0] == 'view')} views, {len(enums)} enums. "
        "Regenerate after backend changes rather than editing by hand.",
        "",
        "## Index",
        "",
        ", ".join(f"[{name}](#{name.lower()})" for _, name, _ in models),
        "",
        "## Models and views",
        "",
    ]
    for kind, name, body in models:
        lines.extend(render_model(kind, name, body))

    lines.append("## Enums")
    lines.append("")
    for _, name, body in enums:
        lines.extend(render_enum(name, body))

    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(models)} models/views and {len(enums)} enums to {args.output}")


if __name__ == "__main__":
    main()
