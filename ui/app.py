import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.append(project_root)

import streamlit as st
import tempfile
from agent.agent import run_agent

st.set_page_config(
    page_title="AI Backup Verification Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Backup Verification Agent")

st.markdown(
    "Upload Original and Backup files to verify data integrity."
)

# Upload files
original_file = st.file_uploader("Upload Original File", type=["csv"])
backup_file = st.file_uploader("Upload Backup File", type=["csv"])

# Verify Button
if st.button("Verify Backup"):

    if original_file is None or backup_file is None:
        st.warning("Please upload both files.")

    else:
        # Save files temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_original:
            temp_original.write(original_file.read())
            original_path = temp_original.name

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_backup:
            temp_backup.write(backup_file.read())
            backup_path = temp_backup.name

        # Run agent
        result = run_agent(original_path, backup_path)

        validation = result["validation"]
        ai_analysis = result["ai_analysis"]
        report = result["report"]

        # Status
        st.subheader("Verification Status")

        if validation["status"] == "PASS":
            st.success("PASS")
        else:
            st.error("FAIL")

        # Metrics
        st.subheader("Validation Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric("Original Rows", validation.get("original_rows", 0))
        col2.metric("Backup Rows", validation.get("backup_rows", 0))
        col3.metric("Missing Rows", validation.get("missing_rows", 0))

        st.write(f"Duplicates: {validation.get('duplicates', 0)}")
        st.write(f"Schema Mismatch: {validation.get('schema_mismatch', False)}")
        st.write(f"Checksum Match: {validation.get('checksum_match', False)}")

        # ✅ FIXED AI ANALYSIS (STRING SAFE)
        if ai_analysis:
            st.subheader("AI Analysis")
            st.text(ai_analysis)   # 🔥 FIX HERE

        # Report
        st.subheader("Generated Report")

        st.text_area("Report", report, height=300)

        st.download_button(
            label="Download Report",
            data=report,
            file_name="backup_report.txt",
            mime="text/plain"
        )

        # Cleanup
        os.remove(original_path)
        os.remove(backup_path)