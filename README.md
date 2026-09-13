# OpenMTS - Open-source Machinelearning Toolset

**Pretrained classical ML models. One import. Many jobs.**

> ⚠️ **This library is not ready yet.**
> Models are being trained. The API is being built. Nothing works right now.
> Star the repo to follow along.

---

## Coming soon — first 5 vision models

- `face_gender` — male / female
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

**Benchmarks are coming. Models are coming.**

OpenMTS is in early development. Right now, there are no released models and no published numbers — because there is nothing to measure yet.

When models ship, this section will include:

- Accuracy per model (nano / baseline / pro)
- Training dataset + split used
- Model file size
- Inference speed (CPU)
- Known limitations and failure cases

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
Nothing works yet. 5 vision models are on the way.

⭐ Star to follow along.
