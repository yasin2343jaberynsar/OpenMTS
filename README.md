# OpenMTS - Open-source Machinelearning Toolset

## What is OpenMTS?

OpenMTS is a pretrained model zoo for **machine learning & deep learning**.

Many models pretrained, In one simple API.

---

## What works right now

```python
from openmts import GenderPredModel

model = GenderPredModel("plus") # note : this is deprecated, we are rebuilding the gender_prediction model in DL
gender = model.predict(face_image)

# → "male" / "female" one shot 
```
---

## Coming soon — first 5 vision models

- `gender_prediction` - male / female
- `digit` — 0–9 recognition
- `face_emotion` — happy / sad / angry / …
- `face_mask` — mask / no mask
- `shape` — circle / square / triangle

Each model will ship in **three tiers**: nano, baseline, plus.

---

## Benchmarks & Model Accuracy

Every model in OpenMTS is measured and documented.

Each model ships in three tiers — **nano**, **baseline**, and **plus** — trading speed and size for accuracy.

### face_gender | NOTE : this is ML gender face, its being removed in days, its still available until the next version

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

---

## Status Update

OpenMTS was built on classical machine learning — decision trees, SVMs, gradient boosting. No GPUs. No deep learning. No neural networks. Tiny models that run on anything, offline, forever.

That approach has a ceiling.

### What we found

- **face_gender** — 87.58% on test set. Fails on real webcam input.
- **face_mask** — 97.55% on test set. Fails on real images.
- **digit** — 98.06% on MNIST. Fails on real handwritten digits.

The models learned their training data. They don't generalize to real-world input.

Classical ML learns patterns in the training distribution. When input differs — different lighting, angle, camera — the patterns don't apply. Deep learning handles this. Classical ML doesn't.

### What we're doing

- Gender, mask, and digit are being retrained with neural networks.
- Classical models remain available for edge cases (tiny, offline, CPU-only).
- All vision models from here forward use deep learning.

### New direction

**Before:** Pretrained classical ML models. Tiny, offline, CPU-only.

**Now:** Pretrained ML models that work on real data. Classical where it's fast. Deep where it's needed.

### Apology

We promised classical ML that works everywhere. We shipped models that looked good on benchmarks and failed in practice.

We're fixing it. Nothing ships until it works on real data.

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

## Status Update

OpenMTS was built on classical machine learning — decision trees, SVMs, gradient boosting. No GPUs. No deep learning. No neural networks. Tiny models that run on anything, offline, forever.

That approach has a ceiling.

### What we found

- **face_gender** — 87.58% on test set. Fails on real webcam input.
- **face_mask** — 97.55% on test set. Fails on real images.
- **digit** — 98.06% on MNIST. Fails on real handwritten digits.

The models learned their training data. They don't generalize to real-world input.

Classical ML learns patterns in the training distribution. When input differs — different lighting, angle, camera — the patterns don't apply. Deep learning handles this. Classical ML doesn't.

### What we're doing

- Gender, mask, and digit are being retrained with neural networks.
- Classical models remain available until new versions are available.
- Most vision/audio/text models from here forward use deep learning.

### Apology

We shipped models that looked good on benchmarks and failed in practice.

We're fixing it. Nothing ships until it works on real data.

⭐ Star to follow along.
