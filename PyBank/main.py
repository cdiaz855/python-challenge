import os
import csv
monthsCount=0
netTotal=0
previousAmount=0
changeTotal=0
greatestIncrease=0
greatestDecrease=0
greatesIncreaseDate=""
greatestDecreaseDate=""

budget_csv= os.path.join('Resources','budget_data.csv.')
outfile=os.path.join("Analysis","data_output.csv")

with open(budget_csv) as csv_file:
    csv_reader= csv.reader(csv_file)
    header=csv_file.readline()
    rows=csv.reader(csv_file)

    changeCount=0
    change=0
    for row in csv_reader:
        # print(row)
        

        monthsCount=monthsCount+1
        currentAmount=int(row[1])
        netTotal= netTotal + currentAmount

        if previousAmount != 0:
            change= currentAmount-previousAmount
            changeTotal=changeTotal+change
    
            changeCount=changeCount+1
            # print(change)
            # exit()
        previousAmount=currentAmount
  
        if change > greatestIncrease:
            greatestIncrease=change
            greatestIncreaseDate=row[0]

        if change < greatestDecrease:
            greatestDecrease=change
            greatestDecreaseDate=row[0]
        


output=f"""
Financial Analysis
----------------------------
Total Months: {monthsCount}
Total: ${netTotal}
Average  Change: ${changeTotal/changeCount:.2f}
Greatest Increase in Profits: {greatestIncreaseDate} ${greatestIncrease}
Greatest Decrease in Profits: {greatestDecreaseDate} ${greatestDecrease}
"""
print(output)

with open(outfile,'w')as output_data:
    output_data.write(output)


