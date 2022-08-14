import csv
import collections

cntries = collections.Counter()
country = []
count = []

with open("ESS10.csv") as file:
    for line in csv.reader(file, delimiter=","):
        if line[5] == "cntry":
            continue
        cntries[line[5]] += 1

    for key in cntries:
        value = cntries[key]
        country.append(key)
        count.append(value)
