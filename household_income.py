import csv
import collections
from countries import country_column

BG = collections.Counter()
income_BG = []
count_BG = []


with open("ESS10.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    income_column = header.index("hinctnta")
    print(income_column)

    # The following values do not represent any interesting answer by a respondent
    no_answer = ["77.000000", "88.000000", "99.000000"]

    for line in reader:
        if line[income_column] in no_answer:
            continue
        if line[country_column] == "BG":
            BG[float(line[income_column])] += 1

    for key in BG:
        value = BG[key]
        income_BG.append(key)
        count_BG.append(value)

print(income_BG)
print(count_BG)
