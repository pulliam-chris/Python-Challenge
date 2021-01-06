import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Define Variables for Calculations
monthCount = 0
netRevenue = 0.00
greatestIncrease_amount = 0.00
greatestIncrease_month = "Unknown"
greatestDecrease_amount = 0.00
greatestDecrease_month = "Unknown"
#set as original profit amount to accurately reflect profit/loss change
previousMonth_amount = 867884.00 
currentDifference = 0.00
averageChange = 0.00

# Open and read the budget csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip the header
    next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        
        #Increase the month count
        monthCount = monthCount + 1

        #Add entry to total revenue
        netRevenue = float(netRevenue) + float(row[1])

        #Calculate change from previous month
        currentDifference = float(row[1]) - float(previousMonth_amount)
        
        #If greatest increase is more than the current figure, capture new value
        if float(greatestIncrease_amount) < float(currentDifference):
            greatestIncrease_amount = float(currentDifference)
            greatestIncrease_month = row[0]
        
        #If greatest decrease is less than the current figure, capture new value
        if float(greatestDecrease_amount) > float(currentDifference):
            greatestDecrease_amount = float(currentDifference)
            greatestDecrease_month = row[0]

        #Set amount for next month comparison
        previousMonth_amount = float(row[1])

        #Keep running total for average profit
        averageChange = averageChange + float(currentDifference)
        
#calculate average profit before printing. Reduce month count to eliminate starting month
averageChange = float(averageChange / int(monthCount-1))
averageChange = round(averageChange,2)

#Use round() on calculated money values before printing and writing to file
netRevenue = round(netRevenue)
greatestDecrease_amount = round(greatestDecrease_amount)
greatestIncrease_amount = round(greatestIncrease_amount)

print('\n'"Financial Analysis")
print("-----------------------------")
print(f"Total Months: {monthCount}")
print(f"Total: ${netRevenue}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {greatestIncrease_month} ($ {greatestIncrease_amount})")
print(f"Greatest Decrease in Profits: {greatestDecrease_month} ($ {greatestDecrease_amount})")

# Specify the file to write to
output_path = os.path.join("Analysis", "budget_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:

    #Write each line as it has already been printed.  Include '\n' for end of line
    file.write("Financial Analysis"'\n')
    file.write("---------------------------------"'\n')
    file.write(f"Total Months: {monthCount}"'\n')
    file.write(f"Total: ${netRevenue}"'\n')
    file.write(f"Average Change: ${averageChange}"'\n')
    file.write(f"Greatest Increase in Profits: {greatestIncrease_month} ($ {greatestIncrease_amount})"'\n')
    file.write(f"Greatest Decrease in Profits: {greatestDecrease_month} ($ {greatestDecrease_amount})"'\n')

#File read and outputs complete
