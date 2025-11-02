import remove as rm
import add
import pandas as pd

# Constants
IN_COL_NAME = "Sex upon Intake"
OUT_COL_NAME = "Sex upon Outcome"


def main():
    in_df = pd.read_csv("oldData/Austin_Animal_Center_Intakes.csv")
    out_df = pd.read_csv("oldData/Austin_Animal_Center_Outcomes.csv")

    intakes_removal = rm.remove_columns_intakes(in_df)
    outcomes_removal = rm.remove_columns_outcomes(out_df)
    date_change_intakes = rm.adjust_date_time_vals(intakes_removal)
    date_change_outcomes = rm.adjust_date_time_vals(outcomes_removal)

    sep_intakes = add.separate_neuter_gender_col(date_change_intakes, IN_COL_NAME)
    sep_outcomes = add.separate_neuter_gender_col(date_change_outcomes, OUT_COL_NAME)

    sep_intakes.to_csv("newData/Austin_Animal_Center_Intakes.csv")
    sep_outcomes.to_csv("newData/Austin_Animal_Center_Outcomes.csv")


if __name__ == "__main__":
    main()
