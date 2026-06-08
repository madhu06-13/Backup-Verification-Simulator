import streamlit as st

def show_metrics(result):

    st.markdown("## 📊 Verification Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Status",
        result["status"]
    )

    col2.metric(
        "Missing Rows",
        result["missing_rows"]
    )

    col3.metric(
        "Duplicates",
        result["duplicates"]
    )

    col4.metric(
        "Risk Level",
        result["risk_level"]
    )

    st.write(
        "**Schema Mismatch:**",
        "Yes" if result["schema_mismatch"] else "No"
    )