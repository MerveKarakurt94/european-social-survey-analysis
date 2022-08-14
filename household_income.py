import csv

income = []

with open("ESS10.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    header = next(reader)
    income_column = header.index("hinctnta")
    print(income_column)

    # The following values do not represent any interesting answer by a candidate
    no_answer = ["77.000000", "88.000000", "99.000000"]

    for line in reader:
        if line[income_column] in no_answer:
            continue
        income.append(line[income_column])

print(len(income))
print(income)