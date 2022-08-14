from countries import *
import plotly.express as px

fig = px.bar(x=country, y=count,
             labels={
                 "x": "Country",
                 "y": "Number of Participants"
             },
             title="ESS10: Number of Participants per Country")

fig.write_html('index.html', auto_open=True)
