import streamlit as st

def show_report(result):

    st.markdown("## 🤖 AI Analysis")

    if result["status"] == "PASS":

        st.success("""
Backup validation completed successfully.

No issues detected.
""")

    else:

        st.warning("""
Backup appears incomplete.

Missing records and duplicates detected.

Schema mismatch found.
""")

    st.markdown("## 🛠 Recovery Suggestions")

    if result["status"] == "PASS":

        st.success("""
✓ Backup is healthy

✓ Safe for restoration
""")

    else:

        st.info("""
1. Re-run backup process

2. Verify source database

3. Validate schema consistency

4. Review logs
""")

    report = f"""
AI BACKUP VERIFICATION REPORT

Status: {result['status']}
Missing Rows: {result['missing_rows']}
Duplicates: {result['duplicates']}
Risk Level: {result['risk_level']}
"""

    st.download_button(
        "📄 Download Report",
        report,
        file_name="backup_report.txt"
    )