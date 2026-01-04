# src/evaluation.py

import json
from pathlib import Path
from typing import Dict, Any

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "outputs"


def load_feedback(path: Path):
    records = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def compute_average_scores(records):
    sums: Dict[str, float] = {}
    counts: Dict[str, int] = {}

    for r in records:
        for crit, score in r["scores"].items():
            sums[crit] = sums.get(crit, 0.0) + score
            counts[crit] = counts.get(crit, 0) + 1

    avgs = {crit: round(sums[crit] / counts[crit], 2) for crit in sums}
    return avgs


def main():
    feedback_path = OUTPUT_DIR / "feedback.jsonl"
    if not feedback_path.exists():
        print("No feedback file found. Run main.py first.")
        return

    records = load_feedback(feedback_path)
    avgs = compute_average_scores(records)

    print("Average scores across all samples:")
    for crit, score in avgs.items():
        print(f"  {crit}: {score}")


if __name__ == "__main__":
    main()
