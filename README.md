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