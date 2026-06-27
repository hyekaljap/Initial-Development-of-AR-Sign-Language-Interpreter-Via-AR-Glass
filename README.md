<div align="center">

# 🤟 AR Sign Language Interpreter via AR Glasses

### PSM 1 (Projek Sarjana Muda 1) — Initial Development Phase

[![Status](https://img.shields.io/badge/Status-In%20Development-yellow?style=for-the-badge)](https://github.com/hyekaljap/Initial-Development-of-AR-Sign-Language-Interpreter-Via-AR-Glass)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green?style=for-the-badge&logo=opencv)](https://opencv.org/)
[![University](https://img.shields.io/badge/UTM-PSM%201-red?style=for-the-badge)](https://www.utm.my/)

> A real-time Augmented Reality system that detects and translates **Bahasa Isyarat Malaysia (BIM)** gestures into text overlays, displayed directly through **XREAL Air 2 Ultra** AR glasses — bridging communication between the deaf/hard-of-hearing community and the hearing world.

</div>

---

## 📌 Project Overview

The **AR Sign Language Interpreter** is a wearable-computing project developed as part of **PSM 1 (Projek Sarjana Muda 1 — Final Year Project Part 1)** at **Universiti Teknologi Malaysia**. The system uses computer vision and augmented reality to provide real-time, hands-free **Bahasa Isyarat Malaysia (BIM)** interpretation through the **XREAL Air 2 Ultra** AR glasses.

When a user performs a BIM gesture in front of the glasses' paired camera, the system:

| Step | Action |
|------|--------|
| 1️⃣ | Captures the hand gesture in real-time via **OpenCV** |
| 2️⃣ | Detects and segments the hand region using **image processing techniques** |
| 3️⃣ | Classifies the gesture using a trained **computer vision model** |
| 4️⃣ | Displays the translated word as an **AR text overlay** through the XREAL Air 2 Ultra lenses |

> This system aims to reduce communication barriers and promote inclusivity for the deaf and hard-of-hearing community in Malaysia.

---

## ✨ Features

### 🔵 PSM 1 — Current
- [x] Real-time hand detection using **OpenCV skin segmentation**
- [x] Static **BIM sign classification** (alphabets)
- [x] Integration with **XREAL Air 2 Ultra** display 
- [x] Real-time **AR text overlay** on XREAL lenses
- [x] Basic **word-level BIM recognition**

### 🔮 PSM 2 — Planned
- [ ] Dynamic/motion BIM gesture support
- [ ] Expanded BIM vocabulary (words & phrases)
- [ ] On-device model optimisation
- [ ] Full wearable deployment & user testing

---

## 🧠 Model & Training

### OpenCV Detection Pipeline

```
Frame Capture
    └── Capture live video frames using cv2.VideoCapture

Colour Conversion
    └── Convert BGR → HSV or YCrCb colour space

Skin Segmentation
    └── Apply colour thresholding to isolate skin pixels

Noise Removal
    └── Morphological operations (erosion, dilation) to clean mask

Contour Detection
    └── Find hand contours using cv2.findContours

Convex Hull & Defects
    └── Extract finger count and hand shape features

Classification
    └── Predict BIM sign label from extracted features
```

---

## 🥽 AR Hardware — XREAL Air 2 Ultra

| Spec | Detail |
|------|--------|
| 🖥️ Display | Dual Micro-OLED, 1080p per eye |
| 👁️ FOV | 52° diagonal |
| 🔌 Connectivity | USB-C (to PC or XREAL Beam) |
| 📍 Tracking | 6DoF SLAM |
| ⚖️ Weight | ~80g |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Hand Detection | OpenCV (skin segmentation, contour) |
| Feature Extraction | OpenCV + NumPy |
| Classifier | SVM / Rule-based (Scikit-learn) |
| AR Display | XREAL Air 2 Ultra + XREAL SDK |
| Language | Python 3.10+ |

---

## 📅 Progress & Milestones

| Week | Milestone | Status |
|------|-----------|--------|
| 1 – 2 | Literature review & proposal | ✅ Done |
| 3 – 4 | BIM dataset collection & labelling | ✅ Done |
| 5 – 6 | OpenCV hand detection pipeline | ✅ Done |
| 7 – 8 | Skin segmentation & contour extraction | 🔄 In Progress |
| 9 – 10 | BIM gesture classifier training | 🔄 In Progress |
| 11 – 12 | XREAL Air 2 Ultra SDK setup & display test | ✅ Done |
| 13 – 14 | End-to-end integration & testing | ⏳ Planned |
| 15 | PSM 1 submission & demo | ⏳ Planned |

---

## ⚠️ Known Issues / Limitations

- OpenCV skin segmentation is **sensitive to lighting conditions**
- Currently supports **static gestures only** (no dynamic/motion signs)
- Background complexity may affect **segmentation accuracy**
- XREAL Air 2 Ultra integration is still in **early stages**

---

## 🔮 Future Work (PSM 2)

- Extend to **dynamic BIM gesture recognition**
- Improve robustness using **deep learning-based detection**
- Expand BIM vocabulary to **common words and phrases**
- Full **end-to-end deployment** on XREAL Air 2 Ultra
- **User study** with Malaysian deaf/hard-of-hearing participants

---

## 👨‍💻 Author

<div align="center">

| | |
|---|---|
| **Name** | Muhammad Haikal Bin Japri |
| **Programme** | Bachelor of Computer Science (Graphic and Multimedia Software) |
| **University** | Universiti Teknologi Malaysia (UTM) |
| **Email** | [haikal04@graduate.utm.my](mailto:haikal04@graduate.utm.my) |

</div>

---

<div align="center">

**PSM 1 — Universiti Teknologi Malaysia**

*Developed for academic purposes as part of the Final Year Project (PSM) requirement.*

</div>
