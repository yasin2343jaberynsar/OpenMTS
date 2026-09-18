# OpenMTS - Open-source Machinelearning Toolset

## What is OpenMTS?

OpenMTS is a pretrained model zoo for **machine learning & deep learning**.

Many models pretrained, In one simple API.

---

## What works right now

```python
from openmts import GenderPredModel

model = GenderPredModel("plus")
gender = model.predict(face_image)

# → "male" / "female" one shot 
```
---

## Coming soon — 4 new vision models

- `digit` — 0–9 recognition
- `face_emotion` — happy / sad / angry / …
- `face_mask` — mask / no mask
- `shape` — circle / square / triangle

Each model will ship in **three tiers**: nano, baseline, plus.

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

We're fixing it. Nothing ships until it works on real data.

⭐ Star to follow along.
