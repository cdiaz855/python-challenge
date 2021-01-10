import os
import csv
budget_csv= os.path.join('..','Resources','budget_data.csv.')
with open(budget_csv) as csv_file:
    csv_reader= csv.reader(csvfile,delimeter=",")
    for row in csv_reader:
        print(row)
        exit()

        date.count(row[0])
        amount.sum(row[1])
        sum_total=sum(row[1])

MonthsCount=len(data)

increase=amount[0]
decrease=amount[0]

for value in range(len(amount)):
    if amount[value] >=increase:
        increase=amount[value]
        increase_month=date[value]
    elif amount[value]<=decrease:
        decrease=amount[value]
        decrease_month=amount[value]
avg_change=(sum_total/MonthsCount)

print("Financial Analysis")
print("----------------------------")
print("Total Months:",MonthsCount)
print("Total:",sum_total)
print("Average Change:",avg_change)
print("Greatest Increase in Profits:", increase_month)
print("Greatest Decrease in Profits:",decrease_month)


