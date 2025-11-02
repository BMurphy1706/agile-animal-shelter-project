# Author: Daniel Soden
# Purpose: Library containing the functionality to add new columns based on existing columns in the dataset

# Imports
import pandas as pd

# Constants

NEW_COLS = ["Neuter/Spay Status", "Gender"]
GENDER_VALS = ["F", "M", "Unknown"]


def separate_neuter_gender_col(df: pd.DataFrame, col: str) -> pd.DataFrame:
    sep = df.copy()
    sep.columns = sep.columns.str.strip()

    gender_map = {
        "Neutered Male": "M",
        "Intact Male": "M",
        "Spayed Female": "F",
        "Intact Female": "F",
        "Unknown": "U",
    }

    neuter_map = {
        "Neutered Male": 1,
        "Intact Male": 0,
        "Spayed Female": 1,
        "Intact Female": 0,
        "Unknown": 0,
    }

    sep[NEW_COLS[0]] = sep[col].map(gender_map)
    sep[NEW_COLS[1]] = sep[col].map(neuter_map)
    sep.drop(columns=[col], inplace=True)
    return sep


def main():
    pass


if __name__ == "__main__":
    main()
