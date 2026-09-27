from pathlib import Path
from ases.pipeline import scan_project
from ases.export import export_json

def test_export(tmp_path):
    fixture = Path(__file__).parent / "fixture_python"
    out = tmp_path/"scan"
    scan_project(fixture, out)
    target = tmp_path/"consumer.json"
    data = export_json(out, target)
    assert data["schema"] == "ases-consumer-context/1.3"
    assert target.exists()
    assert "behaviors" in data and "controls" in data
