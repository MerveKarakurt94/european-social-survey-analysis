import csv
import collections
import plotly.express as px

count_country = collections.Counter()
country = []
count = []

with open("../ESS10.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    country_column = header.index("cntry")

    for line in reader:
        count_country[line[country_column]] += 1

    for key in count_country:
        value = count_country[key]
        country.append(key)
        count.append(value)

fig = px.bar(x=country, y=count,
             labels={
                 "x": "Country",
                 "y": "Number of Participants"
             },
             title="Figure 1: Number of Participants per Country")

fig.update_layout(
    margin=dict(l=0, r=0, t=30, b=0),
)

fig.write_html('../generated_html/participating_countries.html', auto_open=True)
