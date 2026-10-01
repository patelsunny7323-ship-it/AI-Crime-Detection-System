"""
Person Tracking Module
Uses YOLOv8's built-in multi-object tracker with persist=True.
"""

import argparse
import cv2
from ultralytics import YOLO


def track_people(source=0, model_path="yolov8n.pt"):
    model = YOLO(model_path)

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print(f"ERROR: Could not open video source: {source}")
        return

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

        annotated = results[0].plot()

        cv2.putText(
            annotated,
            "Press q to quit",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2,
        )

        cv2.imshow("Person Tracking", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLOv8 person tracking")
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
    track_people(source, args.model)
