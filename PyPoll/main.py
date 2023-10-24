import csv

#path to collect data
election_data = "Resources/election_data.csv" 

#output to text file
output = "Analysis/election_homework.txt"

#set total count 
total_votes = 0

#set canidate count
candidates = {
  'Charles Casper Stockham': 0,
  'Diana DeGette': 0,
  'Raymon Anthony Doane': 0
}
candidate_names = []


#open datafile
with open(election_data) as infile:
    
        rows=csv.reader(infile)
        
        header = next(rows)
        
        for row in rows:

                total_votes += 1
                name = row[2] 
                candidates[name] += 1

                if name not in candidate_names:
                        candidate_names.append(name)


        
max_votes = 0

#open datafile
with open(output,"w") as outfile:

        #find winner and percentage
        for candidate in candidate_names:

                total_candidate_votes = candidates[candidate]
                if total_candidate_votes > max_votes:
                        max_votes = total_candidate_votes
                        winner = candidate

                votes = total_candidate_votes
                vote_percentage = candidates [candidate] /total_votes *100
                voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"            

#print results 
        results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
        print(results)

        for candidate in candidate_names:
                print(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")


        f"-------------------------\n"
        winning_candidate= (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
        print(winning_candidate)

 #write files to txt       
        outfile.write(results)

        
        for candidate in candidate_names:
                outfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")


        outfile.write(winning_candidate)









                
                






