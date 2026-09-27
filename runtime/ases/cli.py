from __future__ import annotations
import argparse, json, yaml, shutil
from pathlib import Path
from .pipeline import scan_project, clean_output
from .audit import audit_project
from .selfcheck import selfcheck
from .export import export_json
from .repo_source import resolve_source
from .diffing import load_findings, diff_findings
from . import __version__

def build_parser():
    p = argparse.ArgumentParser(prog="ases", description="ASES software-engineering and reverse-engineering toolkit")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = p.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="Recover a semantic baseline from a local path or Git repository URL")
    scan.add_argument("source", help="Local repository path or Git URL")
    scan.add_argument("--out", help="Output directory")
    scan.add_argument("--json", action="store_true")
    scan.add_argument("--baseline", help="Previous .ases directory or scanner-findings.json; writes findings-diff.json")

    inspect = sub.add_parser("inspect", help="Summarize a semantic model")
    inspect.add_argument("path")

    audit = sub.add_parser("audit", help="Compare a fresh scan against the stored .ases baseline")
    audit.add_argument("path")
    audit.add_argument("--json", action="store_true")


    diff = sub.add_parser("diff", help="Compare two ASES scanner outputs using stable finding fingerprints")
    diff.add_argument("before", help="Previous .ases directory or scanner-findings.json")
    diff.add_argument("after", help="Current .ases directory or scanner-findings.json")
    diff.add_argument("--out", help="Optional JSON output path")

    exp = sub.add_parser("export", help="Export generic consumer context")
    exp.add_argument("path", help="semantic-model.yaml or .ases directory")
    exp.add_argument("--out", required=True)

    clean = sub.add_parser("clean", help="Remove generated ASES scan output")
    clean.add_argument("path", nargs="?", help=".ases output directory to remove")
    clean.add_argument("--all", action="store_true", help="Remove direct .ases outputs in the current directory")

    sc = sub.add_parser("selfcheck", help="Use ASES to inspect its own repository/runtime")
    sc.add_argument("path", nargs="?", default=".")
    sc.add_argument("--clean", action="store_true", help="Remove .ases-selfcheck after completion")
    return p

def _default_remote_output(repo_name: str) -> Path:
    return Path.cwd() / f"{repo_name}.ases"

def main(argv=None):
    args = build_parser().parse_args(argv)

    if args.command == "scan":
        source = None
        try:
            source = resolve_source(args.source)
            if args.out:
                out = Path(args.out)
            elif source.is_remote:
                out = _default_remote_output(source.repo_name)
            else:
                out = source.root / ".ases"

            result = scan_project(
                source.root,
                out,
                source_uri=source.display_source if source.is_remote else None
            )
            model = result["semantic_model"]
            finding_diff = None
            if args.baseline:
                finding_diff = diff_findings(load_findings(Path(args.baseline)), load_findings(Path(result["output"])))
                (Path(result["output"]) / "findings-diff.json").write_text(json.dumps(finding_diff, indent=2), encoding="utf-8")
            summary = {
                "source": source.display_source,
                "remote": source.is_remote,
                "output": result["output"],
                "languages": model["project"]["languages"],
                "frameworks": model["project"]["frameworks"],
                "components": len(model["components"]),
                "behaviors": len(model["behaviors"]),
                "tests": len(model["tests"]),
                "assets": len(model["assets"]),
                "controls": len(model.get("controls",[])),
                "trust_boundaries": len(model["trust_boundaries"]),
                "observed_patterns": len([p for p in model.get("pattern_findings",[]) if p.get("status")=="OBSERVED"]),
                "pattern_opportunities": len(model.get("pattern_opportunities",[])),
                "pattern_hints": len(model.get("pattern_hints",[])),
                "frontend_findings": len(model.get("frontend_findings",[])),
                "cross_boundary_findings": len(model.get("cross_boundary_findings",[])),
                "source_roles": model.get("source_classification",{}).get("roles",{}),
                "trace_links": len(model["trace_links"]),
                "validation": result["validation"]["status"],
                "diff": finding_diff["summary"] if finding_diff else None,
            }
            print(json.dumps(summary, indent=2) if args.json else "\n".join(f"{k}={v}" for k,v in summary.items()))
            return 0
        except (ValueError, RuntimeError) as e:
            raise SystemExit(str(e))
        finally:
            if source is not None:
                source.cleanup()

    if args.command == "inspect":
        p = Path(args.path)
        if p.is_dir():
            p = p/"semantic-model.yaml"
        model = yaml.safe_load(p.read_text(encoding="utf-8"))
        print(json.dumps({
            "project": model.get("project"),
            "actors": [a["name"] for a in model.get("actors",[])],
            "behaviors": [b["name"] for b in model.get("behaviors",[])],
            "controls": [c.get("control_type") for c in model.get("controls",[])],
            "pattern_findings": model.get("pattern_findings",[]),
            "unknowns": [u["statement"] for u in model.get("unknowns",[])],
        }, indent=2))
        return 0

    if args.command == "audit":
        report = audit_project(Path(args.path))
        print(json.dumps(report, indent=2))
        return 0 if report["status"] in {"PASS","NO_BASELINE"} else 1

    if args.command == "diff":
        report = diff_findings(load_findings(Path(args.before)), load_findings(Path(args.after)))
        if args.out:
            Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, indent=2))
        return 0

    if args.command == "export":
        data = export_json(Path(args.path), Path(args.out))
        print(json.dumps({"output":args.out,"schema":data["schema"]}, indent=2))
        return 0


    if args.command == "clean":
        if args.all:
            targets = [p for p in Path.cwd().iterdir() if p.is_dir() and (p.name == ".ases" or p.name.endswith(".ases") or (p / ".ases-output").exists())]
            removed = [str(p) for p in targets if clean_output(p)]
            print(json.dumps({"removed": removed}, indent=2))
            return 0
        if not args.path:
            raise SystemExit("Provide an ASES output directory or use --all")
        removed = clean_output(Path(args.path))
        print(json.dumps({"removed": [str(Path(args.path).resolve())] if removed else []}, indent=2))
        return 0

    if args.command == "selfcheck":
        root = Path(args.path).resolve()
        report = selfcheck(root)
        print(json.dumps(report, indent=2))
        if args.clean:
            shutil.rmtree(root/".ases-selfcheck", ignore_errors=True)
        return 0 if report["status"] == "PASS" else 1

    return 2
