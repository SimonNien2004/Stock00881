"""共用路徑與設定讀取。"""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
RAW = DATA / "raw"
REPORTS = ROOT / "reports"

TRADES_CSV = DATA / "trades.csv"
PREDICTIONS_CSV = DATA / "predictions.csv"


def load_config() -> dict:
    with open(ROOT / "config.yaml", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_dirs() -> None:
    for p in (DATA, RAW, REPORTS):
        p.mkdir(parents=True, exist_ok=True)
