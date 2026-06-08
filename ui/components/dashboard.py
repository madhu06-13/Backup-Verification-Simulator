import streamlit as st
import pandas as pd

def show_dashboard(result):

    st.markdown("## 📈 Issue Statistics")

    chart_data = pd.DataFrame({
        "Issues": ["Missing Rows", "Duplicates"],
        "Count": [
            result["missing_rows"],
            result["duplicates"]
        ]
    })

    st.bar_chart(
        chart_data.set_index("Issues")
    )