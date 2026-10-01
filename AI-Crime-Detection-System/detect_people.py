"""
Person Detection Module
AI-Powered Smart Surveillance and Crime Detection System

Detects persons (COCO class 0) using YOLOv8 and displays
bounding boxes and a per-frame person count.
"""

import argparse
import cv2
from ultralytics import YOLO


def detect_people(source=0, model_path="yolov8n.pt"):
    model = YOLO(model_path)

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print(f"ERROR: Could not open video source: {source}")
        return

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = model(frame, classes=[0], verbose=False)
        person_count = 0

        for result in results:
            if result.boxes is None:
                continue

            for box in result.boxes:
                if int(box.cls[0]) == 0:
                    person_count += 1
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    confidence = float(box.conf[0])

                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(
                        frame,
                        f"Person {confidence:.2f}",
                        (x1, max(y1 - 10, 20)),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.55,
                        (0, 255, 0),
                        2,
                    )

        cv2.putText(
            frame,
            f"Persons: {person_count}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2,
        )

        cv2.imshow("Person Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 person detection")
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
    detect_people(source, args.model)
