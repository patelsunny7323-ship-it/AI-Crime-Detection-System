# AI-Crime-Detection-System
AI-powered smart surveillance and crime detection system using YOLOv8, OpenCV, person tracking, and restricted-zone intrusion alerts.
# 🛡️ AI-Powered Smart Surveillance & Crime Detection System

An automated computer vision and deep learning pipeline designed to detect people, track their movements with persistent identities, monitor restricted zones, and trigger real-time intrusion alerts with automatic event logging[cite: 3, 8].

---

## 📌 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [System Architecture & Workflow](#-system-architecture--workflow)
- [Project Directory Structure](#-project-directory-structure)
- [Hardware & Software Requirements](#-hardware--software-requirements)
- [Installation & Setup](#-installation--setup)
- [How to Run](#-how-to-run)
- [System Testing & Validation](#-system-testing--validation)
- [Future Scope](#-future-scope)
- [License & Acknowledgments](#-license--acknowledgments)

---

## 🧐 About the Project

Traditional CCTV surveillance relies heavily on continuous human observation, leading to operator fatigue, missed alerts, and delayed responses[cite: 3, 4, 8]. 

This project addresses those issues by utilizing **YOLOv8** for real-time person detection, **built-in multi-object tracking (MOT)** for persistent person identification, and a **Streamlit dashboard** for interactive event review[cite: 3, 4, 7, 8]. The system monitors user-defined restricted zones, raises on-screen alerts, takes photographic evidence upon intrusion, and writes timestamped audit records to a CSV file[cite: 3, 8, 10].

### 🎯 Key Objectives
1. **Person Detection:** Detect human presence in video feeds using pre-trained deep learning models[cite: 3, 5].
2. **Multi-Object Tracking:** Assign persistent numeric IDs to individual persons across frames[cite: 3, 5].
3. **Restricted Zone Check:** Continuously monitor bounding box centroids against restricted spatial bounds[cite: 3, 5, 12, 13].
4. **Automated Alerting & Evidence Logging:** Save event timestamps, screenshots, and logs upon intrusion[cite: 3, 5].
5. **Interactive Review:** Provide a clean, non-technical Streamlit interface to review audit logs[cite: 3, 5, 19].

---

## ✨ Key Features

- **Object-Specific Filtering:** Targets only human entities (`class=0` on the COCO dataset)[cite: 3, 12, 14].
- **Persistent Tracking:** Preserves identity across frame sequences using Kalman-filter and Intersection-over-Union (IoU) matching[cite: 7, 12].
- **Single-Trigger Intrusion Logging:** Logs an intrusion **once per unique person ID** per session to avoid duplicate log entries[cite: 11, 13, 18, 25].
- **Evidence Storage:** Captures annotated image screenshots (`person_<ID>.jpg`) at the exact frame of intrusion[cite: 11, 18].
- **Web Dashboard:** Simple, lightweight Streamlit UI for reviewing all logged intrusion records[cite: 3, 11, 19].

---

## 🏗️ System Architecture & Workflow

The system is organized into a modular 5-layer architecture:
