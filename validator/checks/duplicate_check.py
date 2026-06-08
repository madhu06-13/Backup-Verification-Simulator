import pandas as pd


def duplicate_check(file_path):

    df = pd.read_csv(file_path)

    return int(df.duplicated().sum())