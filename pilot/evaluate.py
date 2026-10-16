"""Offline correctness evaluator for externally produced agent outputs.

This is a *scoring-tool smoke test*, not a language-model benchmark.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any


def load_jsonl(path: Path, required: tuple[str, ...]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            item = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_no}: invalid JSON: {exc.msg}") from exc
        if not isinstance(item, dict) or any(k not in item for k in required):
            raise ValueError(f"{path}:{line_no}: expected object with fields {required}")
        identifier = item.get("id")
        if not isinstance(identifier, str) or not identifier:
            raise ValueError(f"{path}:{line_no}: id must be a nonempty string")
        if identifier in seen:
            raise ValueError(f"{path}:{line_no}: duplicate id {identifier!r}")
        seen.add(identifier)
        records.append(item)
    if not records:
        raise ValueError(f"{path}: no valid records")
    return records


def evaluate(gold: list[dict[str, Any]], predictions: list[dict[str, Any]]) -> dict[str, Any]:
    """Exact-match demo metric; task-specific checkers are future work."""
    g = {x["id"]: x["expected"] for x in gold}
    p = {x["id"]: x["output"] for x in predictions}
    unknown = sorted(set(p) - set(g))
    if unknown:
        raise ValueError(f"predictions contain unknown IDs: {unknown}")
    outcomes = []
    for task_id in sorted(g):
        attempted = task_id in p
        success = attempted and p[task_id] == g[task_id]
        outcomes.append({"id": task_id, "attempted": attempted, "success": bool(success)})
    total = len(g)
    attempted_count = sum(x["attempted"] for x in outcomes)
    successes = sum(x["success"] for x in outcomes)
    return {
        "status": "fixture-only / not an LLM result",
        "metric": "exact_match",
        "tasks": total,
        "attempted": attempted_count,
        "correct": successes,
        "coverage": attempted_count / total,
        "pass_at_1": successes / total,
        "outcomes": outcomes,
    }


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gold", required=True, type=Path)
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--output", type=Path, help="Optional report JSON file")
    args = parser.parse_args(argv)
    try:
        gold = load_jsonl(args.gold, ("id", "expected"))
        predictions = load_jsonl(args.predictions, ("id", "output"))
        result = evaluate(gold, predictions)
        result["inputs_sha256"] = {
            "gold": file_hash(args.gold),
            "predictions": file_hash(args.predictions),
        }
    except (ValueError, OSError) as exc:
        print(f"Evaluation error: {exc}", file=sys.stderr)
        return 2
    report = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
