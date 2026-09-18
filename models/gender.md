# face_gender

Gender classification — male / female.

## Tiers

| Tier | Model | Test accuracy | Real-world accuracy | Size |
|---|---|---|---|---|
| Nano | Decision Tree | 70.01% | ~30% | 57 KB |
| Baseline | CNN | 84.27% | ~50% | ~21 MB |
| Plus | CNN | 88.6% | ~70% | ~38 MB |

## Plus (CNN)

- Test accuracy: 88.6% (UTKFace)
- Real-world accuracy: ~70%
- Trainable parameters: 3,315,042
- Size: ~38 MB (with optimizer state)
- Architecture: 3 Conv blocks + Dense classifier
- Input: 128×128 RGB

## Baseline (CNN)

- Test accuracy: 84.27% (UTKFace)
- Real-world accuracy: ~50%
- Trainable parameters: 1,700,000
- Size: ~21 MB (with optimizer state)
- Architecture: 3 Conv blocks + Dense classifier
- Input: 128×128 RGB

## Nano (Decision Tree)

- Test accuracy: 70.01% (UTKFace)
- Real-world accuracy: ~30%
- Size: 57 KB
- Input: 64×64 RGB

## Hardware used

- GPU: NVIDIA RTX 3060 Ti (8GB VRAM)
- CPU: Intel i5-9400F
- RAM: 16GB
- Framework: Keras 3 with PyTorch backend
- Training data: 128×128 RGB images for CNNs / 64x64 RGB images for Nano

## Target and outcome

The goal was 90% accuracy. It was not reached due to hardware limitations.

## Architecture constraints

The CNNs are missing standard components due to hardware limitations:

- No BatchNorm (GPU could not handle it)
- No `padding='same'` on Conv2D layers (training degraded when applied)
- No data augmentation

## Fine-tuning

Models are saved with optimizer state. You can resume training from where we left off:

```python
import keras
model = keras.models.load_model("gender_plus.keras")
model.fit(your_data, epochs=10)
```
