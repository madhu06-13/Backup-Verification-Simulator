import pandas as pd


def row_count_check(original_file, backup_file):

    original_df = pd.read_csv(original_file)
    backup_df = pd.read_csv(backup_file)

    return {
        "original_rows": len(original_df),
        "backup_rows": len(backup_df)
    }