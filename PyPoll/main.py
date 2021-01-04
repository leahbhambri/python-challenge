# import modules
import os
import csv

# open csv file
election_csv = os.path.join("Resources", "election.csv")

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    csv_header = next(csv_file)

    # count the votes in the dataset using method found at "https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python"
    votes = 0

    #create list for each candidate
    unique_list = []
    name = str(row[2])
    for names in row:
        if name not in unique_list:
                unique_list.append(name)

    #define dictionary, keys = candidate names, values = list of voter IDs

    candidateDict = {}
    for i in len(unique_list):
        candidateDict[i] = []
    
    

#     #create variables to list items
#     for i in len(unique_list):


#     #calculate total votes per candidate
#     for row in csvreader:
#             votes = votes + 1


#     #determine winner of the election

#     #print results
#     print("Election Results")
#     print ("Total Votes: " + totalvotes)
#     print (summary)
#     print ("winner: " + str(winner))

#  #calculate vote percentages in the print statement
    

    

    