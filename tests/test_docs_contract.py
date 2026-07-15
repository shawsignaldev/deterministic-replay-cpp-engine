from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_engineering_depth_docs_exist() -> None:
    for relative in [
        "docs/architecture.md",
        "docs/cpp-interface.md",
        "docs/benchmark-plan.md",
    ]:
        path = ROOT / relative
        assert path.exists(), f"missing {relative}"
        assert len(path.read_text(encoding="utf-8").split()) >= 120

def test_readme_links_depth_docs() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for relative in [
        "docs/architecture.md",
        "docs/cpp-interface.md",
        "docs/benchmark-plan.md",
    ]:
        assert relative in readme
