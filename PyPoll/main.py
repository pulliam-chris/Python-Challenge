import os
import csv

# Path to collect data from the Resources folder
votes_csv = os.path.join('Resources', 'election_data.csv')

def candidate_in_list(candidateList, aCandidate):
    name = str(aCandidate)
    inList = bool(False)

    for candidate in candidateList:
        if candidate == name:
            inList = True
    
    return inList
        
#Define Variables for Calculations
totalVotes = 0
winner = str("Unknown")

#Define List for Candidate List in form [Candidate1, Candidate1's VoteCount, Candidate 2, Candidate2's VoteCount,..]
candidateList = []

candidateIndex = int(0)
candidateVotes = int(0) 

#Define Dictionary using key of candidates name for vote percentage and number of votes
#candidates = dict()

# Open and read the budget csv
with open(votes_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip the header
    next(csv_file)

    for row in csv_reader:
    
        #Increment vote count
        totalVotes = totalVotes + 1

        #If the candidate is not already in the candidate list, add them and a vote counter
        if candidate_in_list(candidateList, row[2]):
            #add a vote to their adjacent vote count in list
            candidateIndex = candidateList.index(str(row[2]))
            candidateIndex = int(candidateIndex) + 1
            candidateVotes = int(candidateList[candidateIndex])
            candidateVotes = int(candidateVotes) + 1
            candidateList[candidateIndex] = candidateVotes
        
        #create a new candidate entry with candidate name and set their adjacent vote count to 0    
        else:
            candidateList.append(str(row[2]))
            candidateList.append(1)
        
        #for candidate in candidateList:
            
        #    if candidate == str(row[2]):
        #        #add a vote to their adjacent count
        #        candidateIndex = candidateList.index(str(row[2]))
        #        candidateIndex = int(candidateIndex) + 1
        #        candidateVotes = int(candidateList[candidateIndex])
        #        candidateVotes = int(candidateVotes) + 1
        #        candidateList[candidateIndex] = candidateVotes 
        #    else:
                #create a new candidate entry
        #        candidateList.append(str(row[2]))
        #        candidateList.append(0)
                #candidateIndex = int(candidateList.index(str(row[2])))
                #candidateIndex = int(candidateIndex) + 1
                #candidateList[candidateIndex] = int(0)
                

        #if candidateList.index(row[2]) == :
        #    candidateList.append(row[2])
        
        #candidateList[3]
        #len(candidateList)
                      

print('\n'"Election Results")
print("-----------------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------------")
#print(candidateList)

#Print Results

#Define some helpful variables
i = int(0)
printName = ""
printVotes = ""
votePercentage = float(0)
mostVotes = int(0)

#Use while loop to go through candidate List to collect and print the voting results to screen
while i < len(candidateList):
    printName = str(candidateList[i])
    i = i + 1
    printVotes = str(candidateList[i])
    votePercentage = float(int(printVotes)/int(totalVotes)*100)
    votePercentage = round(votePercentage,2)
    
    #Track the winner by votes
    if mostVotes < int(candidateList[i]):
        mostVotes = int(candidateList[i])
        winner = str(printName)

    #Print 
    print(f"{printName}: {votePercentage}% ({printVotes})")   

    i = i + 1

#Print the winner
print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")

# Specify the file to write to
output_path = os.path.join("Analysis", "election_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:

    file.write("Election Results"'\n')
    file.write("-----------------------------"'\n')
    file.write(f"Total Votes: {totalVotes}"'\n')
    file.write("-----------------------------"'\n')
    
    #Use while loop to go through candidate List to collect and print the voting results to file
    i = int(0)
    while i < len(candidateList):
        printName = str(candidateList[i])
        i = i + 1
        printVotes = str(candidateList[i])
        votePercentage = float(int(printVotes)/int(totalVotes)*100)
        votePercentage = round(votePercentage,2)
    
        #Track the winner by votes
        if mostVotes < int(candidateList[i]):
            mostVotes = int(candidateList[i])
            winner = str(printName)

        #Write candidate to file
        file.write(f"{printName}: {votePercentage}% ({printVotes})"'\n')   

        i = i + 1

    #Print the winner to file
    file.write("-----------------------------"'\n')
    file.write(f"Winner: {winner}"'\n')
    file.write("-----------------------------"'\n')