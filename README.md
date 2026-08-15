# SPAR Applications

Private working archive of SPAR Fall 2026 application responses.

Each project folder contains:

- `application.md` - editable source with italicized application questions and the corresponding draft answers.
- `application.pdf` - compiled, shareable version of the same material.

The root-level [`missing-references.md`](missing-references.md) lists every citation link, writing-sample link, and graph asset that still needs to be supplied or verified. Missing sources are never replaced with guessed URLs.

## Projects

| Project | Folder | Draft status |
| --- | --- | --- |
| Representation Diagnostics for LLM Safety | `representation-diagnostics-for-llm-safety/` | Questions 1 and 2 drafted; optional Question 3 is a placeholder |
| Orthogonalization Against Reward Hacking | `orthogonalization-against-reward-hacking/` | Both questions drafted; Question 2 is explicitly marked for improvement |
| From Stethoscope to Scalpel: Making Feature Geometry Prescriptive for Fine-Tuning | `feature-geometry-for-fine-tuning/` | Questions 1 and 2 drafted; writing-sample link missing |
| Reliable Explanations of AI Behavior Across Functionally Equivalent Models | `reliable-explanations-across-equivalent-models/` | Four responses present; writing-sample link missing |
| Does Reinforcement Learning Improve a Transformer's Access to Its Own Internal Errors? | `rl-access-to-internal-errors/` | Both questions drafted |
| Model Psychology & Neuroscience: Explain Behavior on the Circuit-Level | `model-psychology-and-neuroscience/` | All three responses drafted; graph asset missing |
| What Tokens Lead to Emergent Misalignment? | `tokens-and-emergent-misalignment/` | All three responses drafted |

## Source material

- Draft responses: [spar application word count](https://docs.google.com/document/d/1QhLEr21R00P6lxiQg4o3Hg_5kF8XEecJWai82t-mXTc/)
- Representation Diagnostics instructions: [SPAR 2026 Representation Diagnostics Mentee Questions](https://docs.google.com/document/d/1QSMaGd9ezmsSuw22GdsSfX-SztDumAQRoBtyz-G9daU/)

The Google documents remain the source of truth. This repository is a structured snapshot prepared for review and PDF export.

## Rebuilding the PDFs

Install the dependency from `requirements.txt`, then run:

```bash
python tools/build_pdfs.py
```

The script rebuilds every `application.pdf` beside its corresponding `application.md`.
