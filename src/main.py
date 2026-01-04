# src/main.py

import json
from pathlib import Path
from datetime import datetime
from typing import Any, Dict

from llm_mock import generate_feedback


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"


def load_samples(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_feedback_linewise(path: Path, record: Dict[str, Any]):
    """Append one JSON record per line (JSONL format)."""
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    samples_path = DATA_DIR / "sample_submissions.json"
    samples = load_samples(samples_path)

    timestamp = datetime.utcnow().isoformat()
    output_path = OUTPUT_DIR / "feedback.jsonl"

    print(f"Loaded {len(samples)} samples.")
    print(f"Writing feedback to: {output_path}")

    # اگر فایل وجود داشته باشد، برای سادگی پاکش می‌کنیم
    if output_path.exists():
        output_path.unlink()

    for sample in samples:
        fb = generate_feedback(sample)

        record = {
            "sample_id": sample["id"],
            "assignment_title": sample["assignment_title"],
            "submission": sample["submission"],
            "scores": fb.scores,
            "overall_comment": fb.overall_comment,
            "generated_at": timestamp,
        }

        print("-" * 60)
        print(f"ID: {record['sample_id']}")
        print(f"Title: {record['assignment_title']}")
        print(f"Scores: {record['scores']}")
        print(f"Comment: {record['overall_comment']}\n")

        save_feedback_linewise(output_path, record)


if __name__ == "__main__":
    main()
