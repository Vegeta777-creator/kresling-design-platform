import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "platform_data.js"


def read_csv(path):
    rows = []
    with path.open("r", encoding="utf-8-sig") as f:
        clean = (line for line in f if not line.lstrip().startswith("#"))
        reader = csv.DictReader(clean)
        for row in reader:
            rows.append({k: float(v) if v not in ("", None) and k != "case" else v for k, v in row.items()})
    return rows


dataset = read_csv(ROOT / "data" / "jump3_dataset_cal.csv")
inverse = read_csv(ROOT / "data" / "verify_inverse_cal_results.csv")

meta = {
    "dataset_source": "data/jump3_dataset_cal.csv",
    "inverse_source": "data/verify_inverse_cal_results.csv",
    "n_designs": len(dataset),
    "scope": "reduced-model calibrated design space; FEM-gated only at anchor cases",
    "fem_anchor": {
        "case": "m2s2 pass-2",
        "odb": "fem/runs_ec1736/pass2/kresling_dynjump_m2s2.odb",
        "reduced_vs_fem_error": {
            "t_lift": "±4.4%",
            "v_top": "±7%",
            "spin": "±8.2%",
        },
        "caveat": "velocity values are mesh-sensitive; use FEM gate for reportable claims",
    },
}

text = "window.KRESLING_PLATFORM_DATA = "
text += json.dumps({"meta": meta, "designs": dataset, "inverse": inverse}, indent=2)
text += ";\n"
OUT.write_text(text, encoding="utf-8")
print(OUT)
