# Author: Ben Murphy
# Purpose: Library for handling abnormal data present in the dataset
import pandas as pd

in_cols = ["Time taken In", "Date Taken In"]
out_cols = ["Time Outcome Reached", "Date Outcome Reached"]


def fix_date_time_in(df: pd.DataFrame) -> pd.DataFrame:
    fixed = df.copy()

    dt_objects = pd.to_datetime(fixed["DateTime"], format="mixed")

    fixed[in_cols[0]] = dt_objects.dt.strftime("%I:%M %p")
    fixed[in_cols[1]] = dt_objects.dt.strftime("%m/%d/%Y")

    fixed.drop(columns=["DateTime"], inplace=True)
    return fixed


def fix_date_time_out(df: pd.DataFrame) -> pd.DataFrame:
    fixed = df.copy()

    dt_objects = pd.to_datetime(fixed["DateTime"], format="mixed")

    fixed[out_cols[0]] = dt_objects.dt.strftime("%I:%M %p")
    fixed[out_cols[1]] = dt_objects.dt.strftime("%m/%d/%Y")

    fixed.drop(columns=["DateTime"], inplace=True)

    return fixed


def fix_breed_data(df: pd.DataFrame) -> pd.DataFrame:
    fixed_breed_data = df.copy()
    is_other = fixed_breed_data["Animal Type"] == "Other"

    fixed_breed_data.loc[is_other, "Animal Type"] = fixed_breed_data["Breed"]
    fixed_breed_data.loc[is_other, "Breed"] = "N/A"

    return fixed_breed_data
