![AI Adversarial Attacks](readme_banner.png)

# Adversarial AI: Attacks, Mitigations & Defense Strategies

This repository documents hands-on work exploring how machine learning models can be attacked, manipulated, and defended against. Each chapter is a self-contained project building toward a full adversarial attack and defense pipeline.

---

## ⚠️ Disclaimer

All work in this repository is intended **strictly for research and educational purposes**. Techniques, code, scripts and exploits are documented to build awareness of AI security vulnerabilities. Nothing here should be used to attack, manipulate, or compromise systems without explicit authorisation. The author assumes no responsibility for misuse of any material in this repository.

---

## Project 1: Building a Target: ML Environment & Image Classifier Service

Project code and files: [Project 1](./project-1-basic-ml-service)

The goal of this project is to build and deploy a working ML service that will serve as the primary attack target in subsequent projects.

The work covers setting up a Python ML development environment with dependency management via `pip` and virtual environments, registered inside Jupyter notebooks for reproducibility. Two models are built from scratch: a simple Neural Network as a baseline, and a more advanced CNN for image classification on the CIFAR-10 dataset, 60,000 32×32 colour images across 10 classes.

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

**This service is the main attack target for all adversarial work in the projects that follow.**

### Project 1 credits
- [Adversial AI Attacks Packt Publishing](https://github.com/PacktPublishing/Adversarial-AI---Attacks-Mitigations-and-Defense-Strategies)

## Project 2: Securing Our Basic ML Service

### Threat Model
Our threat model assumes the following starting from the outer layer until we reach the encrypted ML model:
- Layer 1: VM/host network/perimeter    → assume compromised
- Layer 2: ufw firewall on host         → assume compromised
- Layer 3: Docker network isolation     → assume compromised
- Layer 4: NGINX rules                  → assume compromised
- Layer 5: API-KEY authentication       → assume compromised
- Layer 6: model encryption (enc)       → last line of defense

Our second lab is simulating a realistic attack surface where:
- The model itself is a valuable asset worth stealing
- Adversarial inputs could be used to manipulate predictions
- Each layer slows down or stops an attacker even after partial compromise
