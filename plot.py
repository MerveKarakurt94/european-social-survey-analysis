from countries import country, count
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("ESS10: Number of Participants per Country",
                    "ESS10: Number of Participants per Country",
                    "ESS10: Number of Participants per Country",
                    "ESS10: Number of Participants per Country"))

fig.add_trace(go.Bar(x=country, y=count), row=1, col=1)
fig.add_trace(go.Bar(x=country, y=count), row=1, col=2)
fig.add_trace(go.Bar(x=country, y=count), row=2, col=1)
fig.add_trace(go.Bar(x=country, y=count), row=2, col=2)

fig.update_layout(height=700, width=1500,
                  title_text="Multiple Subplots")

fig.write_html('index.html', auto_open=True)
