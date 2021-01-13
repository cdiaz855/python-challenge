import os
import csv 

totalVotes=0
khan_votes=0
correy_votes=0
li_votes=0
otooley_votes=0
winner=""

election_csv= os.path.join('Resources','election_data.csv')
outfile=os.path.join("Analysis","election_output.csv")

with open(election_csv) as csv_file:
    csv_reader= csv.reader(csv_file)
    header=csv_file.readline()
    rows=csv.reader(csv_file)

    for row in rows:
        # print(row)
        # exit()
        candidate=row[2]
        totalVotes=totalVotes+1
         
        # print(f"candidate= {candidate}  {row[2]}")

        if (candidate == "Khan"):
            khan_votes=khan_votes+1
        
        elif (candidate == "Correy"):
            correy_votes=correy_votes+1
        
        elif (candidate == "Li"):
            li_votes=li_votes+1
        
        elif (candidate == "O'Tooley"):
            otooley_votes=otooley_votes+1
        
        # exit()
    winner="Khan"
        
# print(khan_votes)

        

output = f"""
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
Khan: % ({khan_votes})
Correy: % ({correy_votes})
Li: % ({li_votes})
O'Tooley: % ({otooley_votes})
-------------------------
Winner: {winner}
"""
print(output)

with open(outfile,'w')as output_data:
    output_data.write(output)






