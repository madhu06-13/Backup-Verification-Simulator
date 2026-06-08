import pandas as pd


def schema_check(original_file, backup_file):

    original_columns = list(
        pd.read_csv(original_file).columns
    )

    backup_columns = list(
        pd.read_csv(backup_file).columns
    )

    return original_columns == backup_columns