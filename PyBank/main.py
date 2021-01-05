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
previousMonth_amount = 0.00
currentDifference = 0.00

# Open and read the budget csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip the header
    next(csv_file)

    # Read the header row first (skip this part if there is no header)
    #csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

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
        
        #if great decrease is less than the current figure, capture new value
        if float(greatestDecrease_amount) > float(currentDifference):
            greatestDecrease_amount = float(currentDifference)
            greatestDecrease_month = row[0]

        #Set amount for next month comparison
        previousMonth_amount = float(row[1])

        


print(f"Total Months: {monthCount}")
print(f"Total: ${netRevenue}")
print(f"Average Change: $")
print(f"Greatest Increase in Profits: {greatestIncrease_month} ($ {greatestIncrease_amount})")
print(f"Greatest Decrease in Profits: {greatestDecrease_month} ($ {greatestDecrease_amount})")

# Specify the file to write to
output_path = os.path.join("Analysis", "budget_analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])

    # Write the calculated results
    csvwriter.writerow([monthCount, netRevenue, ' ', greatestIncrease_month, greatestDecrease_month])
