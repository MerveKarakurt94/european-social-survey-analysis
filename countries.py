import csv
import collections

cntries = collections.Counter()

with open("ESS10.csv") as file:
    for line in csv.reader(file, delimiter=","):
        if line[5] == "cntry":
            continue
        cntries[line[5]] += 1

print(cntries.most_common())