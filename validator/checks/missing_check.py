import pandas as pd


def missing_row_check(original_file, backup_file):

    original_df = pd.read_csv(original_file)
    backup_df = pd.read_csv(backup_file)

    original_rows = set(
        map(tuple, original_df.values)
    )

    backup_rows = set(
        map(tuple, backup_df.values)
    )

    missing_rows = original_rows - backup_rows

    return len(missing_rows)