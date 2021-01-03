# import modules
import os
import csv

# open csv file
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    csv_header = next(csv_file)

    #define variables
    month = 0
    netprofit = 0
    previousday = 0
    change = 0

    #define list for change values
    changelist = []
    
    #create for loop for each row in the dataset
    for row in csvreader:
        
        #define updated month total using method found at "https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python"
        month = month + 1

        #define netprofit total
        profit_loss = (row[1])
        netprofit = netprofit + profit_loss

        #append change figure to the list and save updated value
        change = profit_loss - previousday
        changelist.append(change)
    
    #find max value of changelist

    #find min value of changelist

    #create loop to find max and min values in list and print the corresponding dates
    for row in csvreader:
        if row[1] == maxchange
            maxdate = row[0] 

        if row[1] == minchange
            mindate = row[0]       
        
    #print Analysis statement
    print ("Financial Analysis")
    print ("Total Months: " + month)
    print ("Total: $" + netprofit)
    print ("Average Change: $" + averagechange)
    print ("Greatest Increase in Profits: " + maxdate + maxchange)
    print ("Greatest Increase in Profits: " + mindate + minchange)
