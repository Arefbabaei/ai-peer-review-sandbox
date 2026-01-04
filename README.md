# AI-peer-review
Experiment with AI-supported peer review automated feedback
# AI Peer Review Sandbox

This repository contains a small prototype for experimenting with **AI-supported peer review and automated feedback**.

> ⚠️ All data in this repository is **synthetic** and used only for demonstration.  
> No real student data or confidential information is included.

## Overview

The goal of this sandbox is to simulate how large language models (LLMs) could assist instructors and students by:

- Generating draft feedback for sample submissions
- Producing simple rubric-style scores (clarity, technical accuracy, completeness)
- Allowing simple analysis of feedback quality

At this stage, the project uses a **mock LLM** (`llm_mock.py`) instead of a real API, in order to keep the code lightweight and fully reproducible.

## Project structure

- `data/` – Synthetic assignments and student submissions  
- `src/main.py` – Entry point for generating feedback  
- `src/llm_mock.py` – Mock LLM that simulates scoring and comments  
- `src/evaluation.py` – Simple script for aggregating scores  
- `outputs/` – Generated feedback (JSONL format)  
- `requirements.txt` – Optional Python dependencies

## How to run

```bash
pip install -r requirements.txt

# Generate feedback for the sample submissions
python src/main.py

# Compute average scores from the generated feedback
python src/evaluation.py
## Example output

After running `python src/main.py`, the system produces rubric-based scores and feedback such as:

- Clarity: 4
- Technical accuracy: 5
- Completeness: 4

Sample comment:
> "The response is generally clear and easy to follow. Key technical concepts appear to be described correctly. Overall, the answer covers the main points requested in the prompt."

This demonstrates how AI-assisted feedback could support peer review and instructional workflows.