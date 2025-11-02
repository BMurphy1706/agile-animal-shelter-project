# Author: Ben Murphy
# Purpose: This script is designed to identify and remove redundant code the dataframes and also combine the two files to make our singular unified dataframe.

import pandas as pd


def clean_empty_outcomes(df: pd.DataFrame) -> pd.DataFrame:
    clean_df = df.copy()
    clean_df.fillna({"Outcome Subtype": "N/A"}, inplace=True)

    return clean_df


def remove_dupes(df: pd.DataFrame) -> pd.DataFrame:
    clean_df = df.copy()
    clean_df.drop_duplicates()
    return clean_df


def combine_dataframes(df_one, df_two) -> pd.DataFrame:
    df_one_copy = df_one.copy()
    df_two_copy = df_two.copy()

    ignore_cols = [  # Columns that will not change and do not need to be recorded again
        "Animal Type",
        "Breed",
        "Color",
        "Sex upon Outcome",
        "Gender",
    ]

    df_two_copy_cleaned = df_two_copy.drop(columns=ignore_cols, axis=1, errors="ignore")

    combined_df = pd.merge(df_one_copy, df_two_copy_cleaned, on="Animal ID", how="left")

    return combined_df


def clean(df) -> pd.DataFrame:
    clean_df = df.copy()

    elim_empty = clean_empty_outcomes(clean_df)
    elim_dupe = remove_dupes(elim_empty)

    return elim_dupe
