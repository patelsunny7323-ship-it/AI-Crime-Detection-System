# AI-Powered Smart Surveillance and Crime Detection System

An AI-powered computer-vision surveillance system for person detection, multi-object tracking, restricted-zone monitoring, intrusion alerting, evidence capture, and event logging.

## Project Information

- **Course:** CSE3010
- **Student:** Sunny Patel
- **Registration No.:** 24BAI10976
- **Technologies:** Python, YOLOv8, OpenCV, Streamlit, Pandas, NumPy

## Features

- Person detection using YOLOv8
- Persistent person tracking using YOLOv8 tracking
- Rectangular restricted-zone monitoring
- On-screen intrusion alert
- One-time event logging per tracking ID during a session
- Timestamped CSV event log
- Automatic evidence screenshot capture
- Streamlit dashboard for reviewing events
- Webcam or video-file input

## System Workflow

```text
Video / Webcam
      |
      v
YOLOv8 Person Detection
      |
      v
Person Tracking + ID
      |
      v
Restricted Zone Check
      |
      +---- No intrusion ----> Continue monitoring
      |
      v
Intrusion Alert
      |
      +----> Screenshot Evidence
      |
      +----> intrusion_log.csv
      |
      v
Streamlit Dashboard
```

## Project Structure

```text
AI-Crime-Detection-System/
│
├── dashboard/
│   └── app.py
│
├── models/
│   └── README.md
│
├── screenshots/
│   └── README.md
│
├── videos/
│   └── README.md
├── docs/
│   └── project_report.pdf
│
├── detect_people.py
├── track_people.py
├── intrusion_detection.py
├── intrusion_log.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.9 or newer is recommended.
- A webcam or a local video file.
- Internet access is normally needed the first time the YOLOv8 model weights are downloaded.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/patelsunny7323-ship-it/AI-Crime-Detection-System.git
cd AI-Crime-Detection-System
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

### Person detection

For the default webcam:

```bash
python detect_people.py
```

For a video file:

```bash
python detect_people.py --source videos/test.mp4
```

### Person tracking

```bash
python track_people.py
```

Or:

```bash
python track_people.py --source videos/test.mp4
```

### Full intrusion detection

For webcam:

```bash
python intrusion_detection.py
```

For a video file:

```bash
python intrusion_detection.py --source videos/test.mp4
```

The first execution may automatically download `yolov8n.pt`.

Press `q` to close the OpenCV window.

## Restricted Zone

The default restricted-zone coordinates are defined in `intrusion_detection.py`:

```python
ZONE_X1 = 300
ZONE_Y1 = 150
ZONE_X2 = 650
ZONE_Y2 = 450
```

These values are pixel coordinates and may need to be changed for a different camera angle or video resolution.

## Intrusion Evidence

When a tracked person's centroid enters the restricted zone for the first time during the current session:

1. An intrusion alert is displayed.
2. An evidence screenshot is saved in `screenshots/`.
3. A timestamped record is appended to `intrusion_log.csv`.

Example CSV structure:

```text
Time,Person_ID,Event
2026-01-14 10:32:07,1,Intrusion
```

## Streamlit Dashboard

After running the detection system, launch the dashboard from the project root:

```bash
streamlit run dashboard/app.py
```

A browser window will open with the intrusion event table and saved evidence images.

## Important Notes

- This is a proof-of-concept surveillance system, not a production security platform.
- YOLOv8n prioritizes speed and low resource usage; accuracy can be affected by poor lighting, crowding, or occlusion.
- Tracking IDs can change if the tracker temporarily loses a person.
- The restricted zone is currently a hardcoded rectangle.
- No formal precision, recall, or mAP benchmark is included in this project.
- Do not commit passwords, API keys, private data, or sensitive footage to GitHub.

## Future Scope

- Interactive restricted-zone selection
- Multiple camera support
- Email/SMS/Telegram alerts
- Database or cloud storage
- Face recognition or person re-identification
- Larger or custom-trained detection models
- Containerized deployment
- Dashboard analytics and heatmaps

## Project Report

The submitted project report is included at `docs/project_report.pdf`.

## References

- Ultralytics YOLO documentation: https://docs.ultralytics.com/
- OpenCV documentation: https://docs.opencv.org/
- Streamlit documentation: https://docs.streamlit.io/
- COCO dataset: https://cocodataset.org/

## Author

**Sunny Patel**  
Registration No. **24BAI10976**
