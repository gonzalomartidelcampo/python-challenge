import csv

election_data = "Resources/election_data.csv" 

output = "Analysis/election_homework.txt"

total_votes = 0

with open(election_data) as infile:
    
        rows=csv.reader(infile)
        
        header = next(rows)
        
        print(header)
        exit()