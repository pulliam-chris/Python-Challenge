# Python-Challenge

## PyBank
Script file: main.py

Had to make some adjustments in calculating the average profit/loss.  In initializing the variable, it needed to be set to the initial profit/loss value in the file so that the initial change in either direction would not skew the average as if it was starting from $0.

Output:

![PyBank Financial Summary](https://github.com/pulliam-chris/Python-Challenge/blob/main/images/PyBank_output.JPG "PyBank Financial Summary")

I preferred to break out the screen printing and write-file procedures to make for easier troubleshooting and knowing that I could replicate the logic down once the output file was initialized.

## PyPoll
Script file: main.py

Output:

![PyPoll Voting Summary](https://github.com/pulliam-chris/Python-Challenge/blob/main/images/PyPoll_output.JPG "PyPoll Voting Summary")

Resources file was too large to upload the voting.csv file as instructed.  Using a modified/truncated file would alter the vote counts and could alter the "winner" designation.

![Election csv file size](https://github.com/pulliam-chris/Python-Challenge/blob/main/images/election_data_csv_filesize.jpg "Election csv file size")

The data file at the following location was used to create the screen and file outputs:

[Resources\election_data.csv](https://oregon.bootcampcontent.com/Oregon_Coding_Bootcamp/uofo-por-data-pt-12-2020-u-c/-/blob/master/02-Homework/03-Python/PyPoll/Resources/election_data.csv "election_data")

A defined function was created 

```python
def candidate_in_list(candidateList, aCandidate):
```

to check whether a candidate was already being tracked in the candidate list[] data structure.  This function returned a boolean value and simplified the loop through the voting rows.  It also helped prevent trying to retrieve a .index() value for a candidate that didn't exist and would cause the script to error.

I preferred to break out the screen printing and write-file procedures to make for easier troubleshooting and knowing that I could replicate the logic down once the output file was initialized.