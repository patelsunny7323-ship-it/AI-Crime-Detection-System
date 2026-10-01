"""
AI-Powered Smart Surveillance and Crime Detection System

Main pipeline:
1. Read video frames.
2. Detect and track persons using YOLOv8.
3. Check whether each tracked person's centroid enters a
   rectangular restricted zone.
4. Show an intrusion alert.
5. Save one evidence screenshot and one CSV record per
   newly detected tracking ID during the session.
"""

import argparse
import csv
from datetime import datetime
from pathlib import Path

import cv2
from ultralytics import YOLO


PROJECT_ROOT = Path(__file__).resolve().parent
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
LOG_FILE = PROJECT_ROOT / "intrusion_log.csv"

# Default restricted zone. Adjust these values for your video.
ZONE_X1 = 300
ZONE_Y1 = 150
ZONE_X2 = 650
ZONE_Y2 = 450


def ensure_storage():
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    if not LOG_FILE.exists():
        with LOG_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Time", "Person_ID", "Event"])


def log_intrusion(person_id, annotated_frame):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    screenshot_path = SCREENSHOT_DIR / f"person_{person_id}.jpg"

    cv2.imwrite(str(screenshot_path), annotated_frame)

    with LOG_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([current_time, person_id, "Intrusion"])

    print(
        f"[INTRUSION] Person ID {person_id} | "
        f"{current_time} | Evidence: {screenshot_path.name}"
    )


def run_intrusion_detection(source=0, model_path="yolov8n.pt"):
    ensure_storage()

    model = YOLO(model_path)
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"ERROR: Could not open video source: {source}")
        print("Check the file path or webcam index.")
        return

    logged_ids = set()

    print("Intrusion detection started.")
    print("Press 'q' to quit.")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = model.track(
            frame,
            persist=True,
            classes=[0],
            verbose=False,
        )

        annotated = frame.copy()

        # Draw restricted zone.
        cv2.rectangle(
            annotated,
            (ZONE_X1, ZONE_Y1),
            (ZONE_X2, ZONE_Y2),
            (0, 0, 255),
            2,
        )
        cv2.putText(
            annotated,
            "RESTRICTED ZONE",
            (ZONE_X1, max(ZONE_Y1 - 10, 25)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2,
        )

        intrusion_active = False

        result = results[0]
        boxes = result.boxes

        if boxes is not None:
            for box in boxes:
                if box.id is None:
                    continue

                person_id = int(box.id[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                inside_zone = (
                    ZONE_X1 < center_x < ZONE_X2
                    and ZONE_Y1 < center_y < ZONE_Y2
                )

                # Draw person box and ID.
                box_color = (0, 0, 255) if inside_zone else (0, 255, 0)
                cv2.rectangle(
                    annotated,
                    (x1, y1),
                    (x2, y2),
                    box_color,
                    2,
                )
                cv2.circle(
                    annotated,
                    (center_x, center_y),
                    5,
                    box_color,
                    -1,
                )
                cv2.putText(
                    annotated,
                    f"Person ID: {person_id}",
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    box_color,
                    2,
                )

                if inside_zone:
                    intrusion_active = True

                    if person_id not in logged_ids:
                        logged_ids.add(person_id)
                        log_intrusion(person_id, annotated)

        if intrusion_active:
            cv2.putText(
                annotated,
                "ALERT: INTRUSION DETECTED",
                (20, 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.95,
                (0, 0, 255),
                3,
            )
        else:
            cv2.putText(
                annotated,
                "Status: Monitoring",
                (20, 45),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

        cv2.imshow("AI Crime Detection System", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Detection stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="YOLOv8 restricted-zone intrusion detection"
    )
    parser.add_argument(
        "--source",
        default="0",
        help="Video file path or webcam index. Example: videos/test.mp4 or 0",
    )
    parser.add_argument(
        "--model",
        default="yolov8n.pt",
        help="YOLO model path. Default: yolov8n.pt",
    )
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source
    run_intrusion_detection(source, args.model)
