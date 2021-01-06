import os
import csv

# Path to collect data from the Resources folder
votes_csv = os.path.join('Resources', 'election_data.csv')

#Function created to more easily check whether candidate already has an entry in the candidate list[]
def candidate_in_list(candidateList, aCandidate):
    name = str(aCandidate)
    inList = bool(False)

    #Cycle through the current candidate list, if the name is found set inList to true
    for candidate in candidateList:
        if candidate == name:
            inList = True
    
    #return whether the candidate was found or not 
    return inList


#Define Variables for candidate calculations
totalVotes = 0
winner = str("Unknown")

#Define List for Candidate List in form [Candidate1, Candidate1's VoteCount, Candidate 2, Candidate2's VoteCount,..]
candidateList = []

#Variables to create and update candidateList
candidateIndex = int(0)
candidateVotes = int(0) 

# Open and read the votes csv
with open(votes_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skip the header
    next(csv_file)

    for row in csv_reader:
    
        #Increment total vote count
        totalVotes = totalVotes + 1

        #If the candidate is already in the list ( found by function ), add to their vote counter
        if candidate_in_list(candidateList, row[2]):
            candidateIndex = candidateList.index(str(row[2])) #locate list index of candidate
            candidateIndex = int(candidateIndex) + 1 #locate list index of the candidate's vote counter
            candidateVotes = int(candidateList[candidateIndex]) #capture their number of current votes
            candidateVotes = int(candidateVotes) + 1 #add to the count from the vote data
            candidateList[candidateIndex] = candidateVotes #reset the candidate's vote counter to the new value
        
        #create a new candidate entry with candidate name and set their adjacent vote count to register their first vote   
        else:
            candidateList.append(str(row[2]))
            candidateList.append(1)
        
#Candidate list now built from file and can be used for processing outputs        
                      
#Print screen headers and total votes counted
print('\n'"Election Results")
print("-----------------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------------")

#Define some helpful output variables
i = int(0)
printName = ""
printVotes = ""
votePercentage = float(0)
mostVotes = int(0)

#Print Results by Candidate

#Use while loop to go through candidate List to collect and print the voting results to screen
while i < len(candidateList):
    printName = str(candidateList[i])
    i = i + 1 #jump to the candidate's adjacent vote count in list
    printVotes = str(candidateList[i])
    votePercentage = float(int(printVotes)/int(totalVotes)*100)
    #format percentage
    votePercentage = round(votePercentage,2)
    
    #Check with each candidate to track largest number of votes to set the winner
    if mostVotes < int(candidateList[i]):
        mostVotes = int(candidateList[i])
        winner = str(printName)

    #Print candidate line
    print(f"{printName}: {votePercentage}% ({printVotes})")   

    i = i + 1 #continue to next candidate in list

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
    i = int(0) #reset i from previous loop, reuse existing variables from screen prints
    while i < len(candidateList):
        printName = str(candidateList[i])
        i = i + 1 #jump to adjacent candidate vote count in list
        printVotes = str(candidateList[i])
        votePercentage = float(int(printVotes)/int(totalVotes)*100)
        #format percentage
        votePercentage = round(votePercentage,2)
    
        #Winner has already been calculated
        
        #Write candidate line to file
        file.write(f"{printName}: {votePercentage}% ({printVotes})"'\n')   

        i = i + 1 #continue to next candidate in list

    #Print the winner to file
    file.write("-----------------------------"'\n')
    file.write(f"Winner: {winner}"'\n')
    file.write("-----------------------------"'\n')

#File read and output complete