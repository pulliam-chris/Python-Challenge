# Python-Challenge

## PyBank

Had to make some adjustments in calculating the average profit/loss.  In initializing the variable, it needed to be set to the initial profit/loss value in the file so that the initial change in either direction would not skew the average as if it was starting from $0.

I preferred to break out the screen printing and write-file procedures to make for easier troubleshooting and knowing that I could replicate the logic down once the output file was initialized.

## PyPoll

Created a defined function to check whether a candidate was already being tracked in the candidate list[] data structure.  This function returned a boolean value and simplified the loop through the voting rows.  It also helped prevent trying to retrieve a .index() value for a candidate that didn't exist and would cause the script to error.

I preferred to break out the screen printing and write-file procedures to make for easier troubleshooting and knowing that I could replicate the logic down once the output file was initialized.