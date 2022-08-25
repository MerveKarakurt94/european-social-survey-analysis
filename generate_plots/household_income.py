import pandas as pd
import plotly.express as px

ess10_df = pd.read_csv("../ESS10.csv")
hh_income = ess10_df[["cntry", "hinctnta"]]
filtered_hh_income = hh_income[hh_income["hinctnta"] <= 10.0]
counted_hh_income = filtered_hh_income.groupby(["cntry","hinctnta"])["hinctnta"].count().rename("Count").reset_index()
print(counted_hh_income)

fig = px.bar(counted_hh_income, x="cntry", y="Count", color="hinctnta", title="Figure 2: Household Income Deciles",
             labels={"cntry": "Country", "hinctnta": "Decile"})

fig.update_layout(
    margin=dict(l=0, r=0, t=30, b=0),
)

fig.write_html('../generated_html/household_income.html', auto_open=True)