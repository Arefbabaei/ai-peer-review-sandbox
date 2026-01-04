# src/llm_mock.py

from dataclasses import dataclass
from typing import Dict, Any, List


KEYWORDS = {
    1: ["labeled", "unlabeled", "map", "structure"],
    2: ["overfitting", "generalize", "regularization", "cross-validation", "more data"],
    3: ["loss function", "difference", "predictions", "labels", "minimize"]
}


@dataclass
class FeedbackResult:
    scores: Dict[str, int]
    overall_comment: str


def _score_length(text: str) -> int:
    """Very naive scoring based on length."""
    words = len(text.split())
    if words < 20:
        return 2
    elif words < 40:
        return 4
    else:
        return 5


def _score_keywords(text: str, keywords: List[str]) -> int:
    text_lower = text.lower()
    hits = sum(1 for k in keywords if k.lower() in text_lower)
    if hits == 0:
        return 1
    elif hits == 1:
        return 3
    elif hits == 2:
        return 4
    else:
        return 5


def generate_feedback(sample: Dict[str, Any]) -> FeedbackResult:
    """
    Simulate LLM-based feedback for one submission.

    sample keys:
      - id
      - assignment_title
      - submission
      - rubric (dict of criteria)
    """
    submission = sample["submission"]
    rubric = sample["rubric"]
    assignment_id = sample["id"]

    scores = {}

    # clarity: based on length
    scores["clarity"] = _score_length(submission)

    # technical_accuracy: based on keyword hits
    keywords = KEYWORDS.get(assignment_id, [])
    scores["technical_accuracy"] = _score_keywords(submission, keywords)

    # completeness: average of the two above (rounded)
    scores["completeness"] = round((scores["clarity"] + scores["technical_accuracy"]) / 2)

    # Build a simple comment
    comment_parts = []

    if scores["clarity"] >= 4:
        comment_parts.append("The answer is generally clear and easy to follow.")
    else:
        comment_parts.append("The answer could be clearer; consider using more precise language and examples.")

    if scores["technical_accuracy"] >= 4:
        comment_parts.append("Key technical concepts appear to be described correctly.")
    else:
        comment_parts.append("Some technical details may be missing or inaccurate; double-check the main definitions.")

    if scores["completeness"] >= 4:
        comment_parts.append("Overall, the response covers the main points requested in the prompt.")
    else:
        comment_parts.append("Try to address all parts of the question explicitly to improve completeness.")

    overall_comment = " ".join(comment_parts)

    return FeedbackResult(scores=scores, overall_comment=overall_comment)
