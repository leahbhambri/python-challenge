# import modules
import os
import csv

# open csv file
budget_data.csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data.csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    csv_header = next(csv_file)

    #define variables
    month = 0
    net_profit = 0
    previous_day = 0
    change = 0

    #define list for change values
    changelist = []
    
    #create for loop for each row in the dataset
    for row in csvreader:
        
        #define updated month total using method found at "https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python"
        month = month + 1

        #define netprofit total
        profit_loss = (row[1])
        net_profit = net_profit + profit_loss

        #append change figure to the list and save updated value
        change = profit_loss - previous_day
        changelist.append(change)

        #define previousday variable
        previous_day=profit_loss
    
    #find average change of changelist values using method found at "https://www.geeksforgeeks.org/find-average-list-python/"
    def average(changelist):
        return sum(changelist)/len(changelist)
        average_change = average(changelist)

    # #find max value of changelist
    max_change = max(changelist)
    max_change_row = changelist.index(max_change)

    #find min value of changelist
    min_change = min(changelist)
    min_change_row = changelist.index(min_change)
    
    #****create loop to find max and min values in list and print the corresponding dates
    for row in csvreader:
        if row[1] == max_change
            max_date = row[0] 

        elif row[1] == min_change
            min_date = row[0]       
        
    #print Analysis statement
    print ("Financial Analysis")
    print ("Total Months: " + month)
    print ("Total: $" + net_profit)
    print ("Average Change: $" + average_change)
    print ("Greatest Increase in Profits: " + max_date + max_change)
    print ("Greatest Increase in Profits: " + min_date + min_change)


#OPTION - write changelist to the csv file
for item in changelist:
    write to the csv