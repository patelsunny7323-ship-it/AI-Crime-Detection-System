"""
Streamlit dashboard for reviewing intrusion_log.csv.
"""

from pathlib import Path

import pandas as pd
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LOG_FILE = PROJECT_ROOT / "intrusion_log.csv"

st.set_page_config(
    page_title="AI Crime Detection Dashboard",
    page_icon="🚨",
    layout="wide",
)

st.title("🚨 AI-Powered Smart Surveillance Dashboard")
st.caption("Review logged restricted-zone intrusion events.")

if not LOG_FILE.exists():
    st.warning(
        "No intrusion_log.csv file exists yet. "
        "Run intrusion_detection.py first."
    )
    st.stop()

try:
    df = pd.read_csv(LOG_FILE)
except Exception as exc:
    st.error(f"Could not read the intrusion log: {exc}")
    st.stop()

if df.empty:
    st.info("No intrusion events have been logged yet.")
    st.stop()

st.metric("Total Intrusion Events", len(df))

if "Person_ID" in df.columns:
    st.metric(
        "Unique Person IDs",
        df["Person_ID"].nunique(),
    )

st.subheader("Intrusion Event Log")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Saved Evidence")

screenshot_dir = PROJECT_ROOT / "screenshots"
images = sorted(screenshot_dir.glob("*.jpg"))

if not images:
    st.info("No evidence screenshots have been saved yet.")
else:
    for image_path in images:
        st.image(
            str(image_path),
            caption=image_path.name,
            width=500,
        )
