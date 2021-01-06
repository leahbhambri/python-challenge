# import modules
import os
import csv

# open csv file
csvpath = os.path.join("Resources", "election_data.csv")
 # Specify the file to write to
output_path = os.path.join("PyPoll_Analysis", "pypoll_analysis.txt")

# count the votes in the dataset using method found at "https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python"
votes = 0

#create list for each candidate using method found at "https://www.geeksforgeeks.org/python-get-unique-values-list/"
unique_list = []

#create dictionary
candidate_votes = {}

#assign highestest percentage vote
hightest_percentage = 0

#assign winner variable 
winner_candidate = ""

#open file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    csv_header = next(csvfile)

    for row in csvreader:
        #calculate total votes per candidate
        votes = votes + 1
        name = str(row[2])
       
        #append list for candidate names 
        if name not in unique_list:
                unique_list.append(name)
                
            #start counting voter count at 0 and add 1 for each candidate
                candidate_votes[name] = 0
        
        candidate_votes[name] =candidate_votes[name] + 1

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    analysis_statement = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {votes}\n"
        f"-------------------------\n")

    print(analysis_statement)

    txtfile.write(analysis_statement)

    #determine winner of the election
    for candidate in candidate_votes:

        vote = candidate_votes[candidate]
        percentage = round(vote/votes*100,3)
        
        if percentage > hightest_percentage:
            hightest_percentage = percentage
            winner_candidate = candidate

        output = f"{candidate}: {percentage}% ({str(vote)})\n"

        print(output)    
    
        txtfile.write(output)

    summary = (
        f"-------------------------\n"
        f"Winner: {winner_candidate}\n"
        f"-------------------------\n")
    
    print(summary)

    txtfile.write(summary)





