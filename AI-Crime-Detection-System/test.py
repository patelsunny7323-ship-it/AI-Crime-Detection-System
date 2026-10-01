"""Basic project environment check."""

import importlib.util


REQUIRED = [
    "cv2",
    "numpy",
    "pandas",
    "streamlit",
    "ultralytics",
]


def main():
    print("AI Crime Detection System - Environment Check")
    print("-" * 50)

    all_ok = True

    for package in REQUIRED:
        installed = importlib.util.find_spec(package) is not None
        status = "OK" if installed else "MISSING"
        print(f"{package:15} : {status}")

        if not installed:
            all_ok = False

    print("-" * 50)

    if all_ok:
        print("Environment check passed.")
    else:
        print("Some dependencies are missing.")
        print("Run: pip install -r requirements.txt")


if __name__ == "__main__":
    main()
