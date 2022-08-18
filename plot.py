from plotly.subplots import make_subplots
import plotly.graph_objects as go
from countries import *
from household_income import counted_income_df

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Figure 1: Number of Participants per Country",
                    "Figure 2: Household income by decile",
                    "Figure 3: ",
                    "Figure 4: "))

fig.add_trace(go.Bar(x=country, y=count), row=1, col=1)
fig.add_trace(counted_income_df, x="cntry", y="count", color="hinctnta",
             labels={"cntry": "Country", "count": "", "hinctnta": "Decile"})
fig.add_trace(go.Bar(x=country, y=count), row=2, col=1)
fig.add_trace(go.Bar(x=country, y=count), row=2, col=2)

fig.update_layout(height=700, width=1500,
                  title_text="European Social Survey 10: display of variables country, household income, x and y")

fig.write_html('index.html', auto_open=True)
