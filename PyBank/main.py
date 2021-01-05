# import modules
import os
import csv

# open csv file
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header row
    csv_header = next(csvfile)

    #define variables
    month = 0
    net_profit = 0
    previous_day = 0
    change = 0
    average_change = 0
    first_row = True
    
    #define list for change values
    changelist = []
    
    #create for loop for each row in the dataset
    for row in csvreader:
        
        #define updated month total using method found at "https://www.kite.com/python/answers/how-to-count-the-number-of-lines-in-a-csv-file-in-python"
        month = month + 1

        #define netprofit total
        profit_loss = int((row[1]))
        net_profit = net_profit + profit_loss

        #append change figure to the list and save updated value
        change = profit_loss - previous_day

        #define previousday variable
        previous_day=profit_loss
    
        if first_row:
                first_row = False
                continue
        changelist.append(change)
        
    #find average change of changelist values using method found at "https://www.guru99.com/find-average-list-python.html/"
    def average(num):
        return sum(num)/len(num)

    
    average_change = round(average(changelist),2)

    #find max value of changelist
    max_change = max(changelist)
    max_change_row = changelist.index(max_change)
    print(max_change_row)

    #find min value of changelist
    min_change = min(changelist)
    min_change_row = changelist.index(min_change)
    print(min_change_row)
   
    #****create loop to find max and min values in list and print the corresponding dates
    row_count = 1
    max_date = 0
    min_date = 0

    for row in csvreader:
        
        row_count = row_count + 1
        
        if row_count == max_change_row:
            max_date = str(row[0])

        elif row_count == min_change_row:
            min_date = str(row[0])     
        
    #print Analysis statement
    # analysis_text = (f'{month} Financial Analysis \n
    # "----------------------------- \n"
    # "Total Months: {month} \n"
    # "Total: $ {net_profit} \n"
    # "Average Change: $ {average_change} \n"
    # "Greatest Increase in Profits: {max_date} {max_change} \n"
    # "Greatest Decrease in Profits: {min_date} {min_change} \n")

    # print(analysis_text)

    print ("Total Months: " + str(month))
    print ("Total: $" + str(net_profit))
    print ("Average Change: $" + str(average_change))
    # # print (str(max_change)+ "   " + str(max_change_row))
    # # print (str(min_change)+"    " + str(min_change_row))
    print ("Greatest Increase in Profits: " + str(max_date) +"  " + str(max_change))
    print ("Greatest Increase in Profits: " + str(min_date) + "  " + str(min_change))


    # # Specify the file to write to
    # output_path = os.path.join("PyBank_Analysis", "pybank_analysis.txt")

    # # Open the file using "write" mode. Specify the variable to hold the contents
    # with open(output_path, 'w', newline='') as txtfile:

    #     # Initialize csv.writer
    #     txtwriter = txt.writer(txtfile, delimiter=',')

    #     # Write the print statement using f method***
    #     txtwriter.write(f'{("Financial Analysis \n Total Months:" month "\n Total: $" net_profit "\n Average Change: $" average_change "\n Greatest Increase in Profits: " max_date max_change "\n Greatest Increase in Profits: " min_date min_change)}')

