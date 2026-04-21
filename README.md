# Adversarial AI — Attacks, Mitigations & Defense Strategies

This repository documents hands-on work exploring how machine learning models can be attacked, manipulated, and defended against. Each chapter is a self-contained project building toward a full adversarial attack and defense pipeline.

---

## ⚠️ Disclaimer

All work in this repository is intended **strictly for research and educational purposes**. Techniques, code, and exploits are documented to build awareness of AI security vulnerabilities. Nothing here should be used to attack, manipulate, or compromise systems without explicit authorisation. The author assumes no responsibility for misuse of any material in this repository.

---

## Project 2 — Building a Target: ML Environment & Image Classifier Service

The goal of this project is to build and deploy a working ML service that will serve as the primary attack target in subsequent chapters.

The work covers setting up a Python ML development environment with dependency management via `pip` and virtual environments, registered inside Jupyter notebooks for reproducibility. Two models are built from scratch: a simple Neural Network as a baseline, and a more advanced CNN for image classification on the CIFAR-10 dataset — 60,000 32×32 colour images across 10 classes.

**CNN Architecture**

| Stage | Details |
|---|---|
| Conv Block 1 | 32 filters — edge detection |
| Conv Block 2 | 64 filters — shape recognition |
| Conv Block 3 | 128 filters — object recognition |
| Flatten | 3D feature maps → 1D vector |
| Dense (128) | Fully connected decision layer |
| Output | 10 neurons, Softmax |

Each conv block: `Conv2D → BatchNorm → Conv2D → BatchNorm → MaxPool → Dropout`

Both models are evaluated and deployed behind a lightweight REST service that accepts prediction requests. A Python client is used to test the service against random images, confirming end-to-end functionality.

**This service is the main attack target for all adversarial work in the chapters that follow.**

---
