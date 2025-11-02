# Author: Daniel Soden
# Purpose: This script will be used to remove columns from the two csv files from Animal intakes and outtakes

import pandas as pd
import datetime as dt

# Constants

REMOVE_FROM_BOTH = ["MonthYear", "Name"]


def remove_columns_intakes(df: pd.DataFrame) -> pd.DataFrame:
    removal = df.copy()
    irrelevant_columns = REMOVE_FROM_BOTH
    removal.drop(columns=irrelevant_columns, inplace=True)

    return removal


def remove_columns_outcomes(df: pd.DataFrame) -> pd.DataFrame:
    removal = df.copy()
    irrelevant_columns = ["Sex upon Outcome"] + REMOVE_FROM_BOTH
    df.drop(columns=irrelevant_columns, inplace=True)
    return removal


def adjust_date_time_vals(df: pd.DataFrame) -> pd.DataFrame:
    adjustments = df.copy()
    adjustments["DateTime"] = pd.to_datetime(
        adjustments["DateTime"],
        format="%m/%d/%Y %I:%M:%S %p",
    ).dt.strftime("%m/%d/%Y %I:%M %p")
    return adjustments


def main():
    pass


if __name__ == "__main__":
    main()
