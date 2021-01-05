import os
import csv

# Path to collect data from the Resources folder
votes_csv = os.path.join('Resources', 'election_data.csv')

#Define Variables for Calculations
totalVotes = 0

#Define Dictionary using key of candidates name for vote percentage and number of votes

# Open and read the budget csv
with open(votes_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip the header
    next(csv_file)

    for row in csv_reader:
    
        #Increment vote count
        totalVotes = totalVotes + 1

print('\n'"Election Results")
print("-----------------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------------")


# Specify the file to write to
output_path = os.path.join("Analysis", "election_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:

    file.write("Election Results"'\n')
    file.write("-----------------------------"'\n')
    file.write(f"Total Votes: {totalVotes}"'\n')
    file.write("-----------------------------"'\n')