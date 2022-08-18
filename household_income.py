import pandas as pd

ess10_df = pd.read_csv("ESS10.csv")
country_income_df = ess10_df[["cntry", "hinctnta"]]
filtered_income_df = country_income_df[country_income_df["hinctnta"] <= 10.0]
counted_income_df = filtered_income_df.groupby(["cntry","hinctnta"])["hinctnta"].count().rename("count").reset_index()

print(counted_income_df)