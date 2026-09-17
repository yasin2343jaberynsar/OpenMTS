# face_gender

Gender classification — male / female.

## Plus (CNN)

- Test accuracy: 88.6% (UTKFace)
- Real-world accuracy: 80–85%
- parameters: 3,315,042
- Size: ~38 MB

**Hardware used:**
- GPU: NVIDIA RTX 3060 Ti (8GB VRAM)
- CPU: Intel i5-9400F
- RAM: 16GB
- Framework: Keras 3 with PyTorch backend
- Training data: 128×128 RGB images

**Target and outcome:**
The goal was 90% accuracy. It was not reached due to hardware limitations.

**Architecture constraints:**
The network is missing standard components due to these limitations:
- No BatchNorm (GPU could not handle it)
- No `padding='same'` on Conv2D layers (training degraded when applied)

**Note:**
This Plus model has significantly better real-world performance than the previous classical Plus.

## Status

CNN models for Nano and Baseline are in training. They will be published when ready.
