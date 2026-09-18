# OpenMTS - Open-source Machinelearning Toolset

## What is OpenMTS?

OpenMTS is a pretrained model zoo for **machine learning & deep learning**.

Many models pretrained, In one simple API.

---

## Quick start

### Installation

Not on PyPi yet.

```bash
pip install git+https://github.com/yasin2343jaberynsar/OpenMTS.git
```

### Quick live program

```python
from openmts import GenderPredModel
import cv2

gender_model = GenderPredModel("plus")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        gender = gender_model.predict(face_img)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame, f"{gender}", (x, y-60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("Gender Live Test", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
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


⭐ Star to follow along.
