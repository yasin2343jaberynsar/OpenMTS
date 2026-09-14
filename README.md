# OpenMTS - Open-source Machinelearning Toolset

**Pretrained classical ML models. One import. Many jobs.**

> 🚧 **Early development.**  
> ✅ **1 model family shipped:** `face_gender` (nano / baseline / plus)  
> 🔜 4 more vision models coming.

---

## What is OpenMTS?

OpenMTS is a pretrained model zoo for **classical machine learning** — not deep learning.

Tiny models. CPU-only. Fully offline. One simple API.

No GPU. No CUDA. No cloud. No 100MB downloads.

---

## What works right now

```python
from openmts import GenderPredModel

model = GenderPredModel("plus")
gender = model.predict(face_image)

# → "male" / "female" one shot
```
---

## Coming soon — first 4 new vision models

- `digit` — 0–9 recognition
- `face_emotion` — happy / sad / angry / …
- `face_mask` — mask / no mask
- `shape` — circle / square / triangle

Each model will ship in **three tiers**: nano, baseline, plus.

---

## What OpenMTS will be

A pretrained model zoo for **classical machine learning** — not deep learning.

Tiny models. CPU-only. Fully offline. One simple API.

No GPU. No CUDA. No cloud. No 100MB downloads.

---

## Honest about limits

OpenMTS uses **classical ML**, not deep learning.

Deep learning (YOLO, Hugging Face, etc.) **may beat OpenMTS on hard tasks.**

OpenMTS is for when you want something simple, tiny, offline, and multi-purpose — many jobs behind one import.

---

## Benchmarks & Model Accuracy

Every model in OpenMTS is measured and documented.

Each model ships in three tiers — **nano**, **baseline**, and **plus** — trading speed and size for accuracy.

### face_gender

| Tier | Algorithm | Test Accuracy | Train Time |
|---|---|---|---|
| nano | Decision Tree | 70.01% | ~40 seconds |
| baseline | HistGradientBoosting | 86.04% | ~1.5 minutes |
| plus | SVM (RBF) | 87.58% | ~109 minutes |

Trained on UTKFace (20,000 images, 80/20 train/test split).

For each model, the following is published:

- Accuracy per tier
- Training dataset and split
- Model file size
- Inference speed (CPU)
- Known limitations and failure modes

Benchmarks are published as models ship.

### Why we publish benchmarks

Because accuracy claims without numbers are just marketing. When OpenMTS says a model works, you'll be able to see:

- How well it works
- Where it fails
- What it was trained on
- How big and fast it is

### What to expect

Classical ML is not deep learning. These models are built to be **small, fast, offline, and simple** — not to set records on hard tasks.

Deep learning (YOLO, Hugging Face, etc.) can beat OpenMTS on hard tasks. That's expected, and we'll say so honestly in every model card.

---

## Roadmap

- [x] Repo + vision setup
- [ ] 5 vision models
- [ ] load() API + model bundles
- [ ] save / load
- [ ] Heatmaps
- [ ] Audio models
- [ ] Text models
- [ ] 100 models

---

## Status

🚧 **Pre-release.**

⭐ Star to follow along.
