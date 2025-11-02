# Author: Gavin Moore
# Purpose: main output file

import remove as rm
import add
import abnormal as ab
import pandas as pd
import redundancy as rd


# Constants
IN_COL_NAME = "Sex upon Intake"
OUT_COL_NAME = "Sex upon Outcome"


def main():
    in_df = pd.read_csv("oldData/Austin_Animal_Center_Intakes.csv")
    out_df = pd.read_csv("oldData/Austin_Animal_Center_Outcomes.csv")

    intakes_removal = rm.remove_columns(in_df)
    outcomes_removal = rm.remove_columns(out_df)
    date_change_intakes = rm.adjust_date_time_vals(intakes_removal)
    date_change_outcomes = rm.adjust_date_time_vals(outcomes_removal)

    sep_intakes = add.separate_neuter_gender_col(date_change_intakes, IN_COL_NAME)
    sep_outcomes = add.separate_neuter_gender_col(date_change_outcomes, OUT_COL_NAME)

    abnormal_adj_in = ab.fix_date_time_in(sep_intakes)
    abnormal_adj_out = ab.fix_date_time_out(sep_outcomes)
    breed_fix_in = ab.fix_breed_data(abnormal_adj_in)
    breed_fix_out = ab.fix_breed_data(abnormal_adj_out)

    cleaned_intakes = rd.clean(breed_fix_in)
    cleaned_outcomes = rd.clean(breed_fix_out)

    cleaned_intakes.to_csv("newData/Austin_Animal_Center_Intakes.csv")
    cleaned_outcomes.to_csv("newData/Austin_Animal_Center_Outcomes.csv")

    final_df = rd.combine_dataframes(cleaned_intakes, cleaned_outcomes)

    final_df.to_csv("newData/Austin_Animal_Center.csv")


if __name__ == "__main__":
    main()
