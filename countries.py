import csv
import collections

count_country = collections.Counter()
country = []
count = []

with open("ESS10.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    country_column = header.index("cntry")

    for line in reader:
        count_country[line[country_column]] += 1

    for key in count_country:
        value = count_country[key]
        country.append(key)
        count.append(value)
