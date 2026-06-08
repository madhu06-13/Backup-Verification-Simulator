import streamlit as st

def upload_files():

    st.markdown("## 📂 Dataset Upload")

    original_file = st.file_uploader(
        "Upload Original Dataset",
        type=["csv"]
    )

    backup_file = st.file_uploader(
        "Upload Backup Dataset",
        type=["csv"]
    )

    return original_file, backup_file