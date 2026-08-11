#!/usr/bin/env python3
"""Extract NestJS endpoints from Clidrive/backend into a Markdown reference.

Usage: python3 gen_endpoints.py <output.md> [--repo <path-to-backend-repo>]
"""
import argparse
import re
from pathlib import Path

HTTP_VERBS = ("Get", "Post", "Put", "Patch", "Delete", "All")
SKIP_DIRS = {"node_modules", "dist", ".git", "coverage"}


def find_controllers(repo: Path):
    for path in repo.rglob("*.controller.ts"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def balanced_call_args(text: str, start: int) -> tuple[str, int]:
    """Given text[start] == '(', return (args_string, index_after_closing_paren)."""
    depth = 0
    i = start
    for i in range(start, len(text)):
        if text[i] == "(":
            depth += 1
        elif text[i] == ")":
            depth -= 1
            if depth == 0:
                return text[start + 1 : i], i + 1
    return text[start + 1 :], len(text)


def decorators_before(text: str, end: int, start: int = 0):
    """Collect (name, args, pos) for every @Decorator(...) between start and end."""
    out = []
    for m in re.finditer(r"@(\w+)\s*\(", text[start:end]):
        name = m.group(1)
        paren_pos = start + m.end() - 1
        args, _ = balanced_call_args(text, paren_pos)
        out.append((name, args.strip(), start + m.start()))
    return out


def method_name_after(text: str, pos: int, max_scan: int = 2000) -> str:
    """Skip any decorators between pos and the method signature, then return its name."""
    i = pos
    limit = min(len(text), pos + max_scan)
    while i < limit:
        while i < limit and text[i] in " \t\r\n":
            i += 1
        if i < limit and text[i] == "@":
            m = re.match(r"@\w+", text[i:limit])
            if not m:
                break
            i += m.end()
            while i < limit and text[i] in " \t\r\n":
                i += 1
            if i < limit and text[i] == "(":
                _, i = balanced_call_args(text, i)
            continue
        m = re.match(
            r"(?:public\s+|private\s+|protected\s+|static\s+|readonly\s+)*"
            r"(?:async\s+)?(\w+)\s*(?:<[^>]*>)?\s*\(",
            text[i:limit],
        )
        if m:
            return m.group(1)
        break
    return "?"


def extract_strings(args: str):
    return [s for s in re.findall(r"""['"]([^'"]*)['"]""", args)]


def clean_scopes(args: str):
    return [s.replace("Scope.", "") for s in re.findall(r"Scope\.(\w+)", args)]


def parse_controller(path: Path, repo: Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    class_match = re.search(r"export\s+class\s+(\w+)", text)
    if not class_match:
        return []
    class_end = class_match.start()

    class_decorators = decorators_before(text, class_end)
    controller_args = next((a for n, a, _ in class_decorators if n == "Controller"), "")
    prefix_parts = extract_strings(controller_args)
    prefix = prefix_parts[0] if prefix_parts else ""

    tags_args = next((a for n, a, _ in class_decorators if n == "ApiTags"), "")
    tags = extract_strings(tags_args) or ["untagged"]

    class_scopes = clean_scopes(next((a for n, a, _ in class_decorators if n == "Scopes"), ""))

    rel_file = str(path.relative_to(repo))

    rows = []
    verb_pattern = re.compile(r"@(" + "|".join(HTTP_VERBS) + r")\s*\(")
    last_end = class_end
    for vm in verb_pattern.finditer(text, class_end):
        verb = vm.group(1)
        paren_pos = vm.end() - 1
        route_args, after_args = balanced_call_args(text, paren_pos)
        route_parts = extract_strings(route_args)
        route = route_parts[0] if route_parts else ""

        # Method-level decorators live between the end of the *previous* handler's
        # signature and this @Verb(...) call - that window can also contain this
        # decorator plus siblings like @HttpCode/@ApiOkResponse, so re-scan a small
        # window starting right after the previous method body found so far.
        window_start = last_end
        sibling_decorators = decorators_before(text, vm.start(), window_start)
        method_scopes = clean_scopes(
            next((a for n, a, p in sibling_decorators if n == "Scopes" and p >= window_start), "")
        )
        if not method_scopes:
            # look forward too: @Scopes can appear after the verb decorator
            forward_decorators = decorators_before(text, after_args + 400, after_args)
            method_scopes = clean_scopes(
                next((a for n, a, p in forward_decorators if n == "Scopes"), "")
            )
        scopes = method_scopes or class_scopes

        handler = method_name_after(text, after_args)

        full_route = "/".join(p.strip("/") for p in (prefix, route) if p) or "/"
        full_route = "/" + full_route if not full_route.startswith("/") else full_route

        rows.append(
            {
                "tags": tags,
                "method": verb.upper(),
                "route": full_route,
                "handler": handler,
                "scopes": ", ".join(sorted(scopes)) if scopes else "",
                "file": rel_file,
            }
        )
        last_end = after_args

    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output")
    parser.add_argument("--repo", default=str(Path.home() / "Documents/Clidrive/backend"))
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    all_rows = []
    for controller in sorted(find_controllers(repo)):
        all_rows.extend(parse_controller(controller, repo))

    by_tag: dict[str, list[dict]] = {}
    for row in all_rows:
        for tag in row["tags"]:
            by_tag.setdefault(tag, []).append(row)

    lines = [
        "# Clidrive backend — API endpoints",
        "",
        f"Generated from `{repo}` by `gen_endpoints.py`. {len(all_rows)} endpoints across "
        f"{len(by_tag)} Swagger tags. Regenerate after backend changes rather than editing by hand.",
        "",
    ]
    for tag in sorted(by_tag):
        rows = sorted(by_tag[tag], key=lambda r: (r["route"], r["method"]))
        lines.append(f"## {tag}")
        lines.append("")
        lines.append("| Method | Route | Handler | Scopes | File |")
        lines.append("|---|---|---|---|---|")
        for r in rows:
            lines.append(
                f"| {r['method']} | `{r['route']}` | {r['handler']} | {r['scopes']} | {r['file']} |"
            )
        lines.append("")

    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(all_rows)} endpoints ({len(by_tag)} tags) to {args.output}")


if __name__ == "__main__":
    main()
