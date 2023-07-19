# Import modules to be used
import os
import csv

# Access correct file to be used & create file for output info
electionpath = os.path.join(".", "Resources", "election_data.csv")
electionoutput = os.path.join("Analysis", "Election_Analysis.txt")

# Assign variables
total_votes = 0
candidates_list = []
d_candidates = {}
votes1 = 0
votes2 = 0
votes3 = 0

# Open file & Analyze info by reading each column as a list
with open(electionpath) as electionfile:
    csvreader = csv.reader(electionfile, delimiter=",")
    csv_header = next(csvreader)

# Calculate Total Votes, find name of candidates, total votes per candidate and calculate percentage votes per candidate
    for row in csvreader:
        total_votes = total_votes + 1
        candidates = row[2]
        if candidates not in candidates_list:
            candidates_list.append(candidates)
            d_candidates[candidates] = 0
        d_candidates[candidates] += 1
    for x in d_candidates:
        c1 = "Charles Casper Stockham"
        c2 = "Diana DeGette"
        c3 = "Raymon Anthony Doane"
        votes1 = d_candidates.get(c1)
        votes2 = d_candidates.get(c2)
        votes3 = d_candidates.get(c3)
        c1_percentage = round(float(votes1) / float(total_votes) * 100, 3)
        c2_percentage = round(float(votes2) / float(total_votes) * 100, 3)
        c3_percentage = round(float(votes3) / float(total_votes) * 100, 3)

# Prints the results to terminal
    print("Election Results")
    print("----------------------------")
    print("Total Votes:", total_votes)
    print("----------------------------")
    print("Charles Casper Stockham: ", c1_percentage, "%  ",
          "votes:", d_candidates['Charles Casper Stockham'])
    print("Diana DeGette: ", c2_percentage, "%            ",
          "votes:", d_candidates['Diana DeGette'])
    print("Raymon Anthony Doane: ", c3_percentage, "%      ",
          "votes:", d_candidates['Raymon Anthony Doane'])
    print("----------------------------")

# Finds the winner and prints winner results
    a = d_candidates['Charles Casper Stockham']
    b = d_candidates['Diana DeGette']
    c = d_candidates['Raymon Anthony Doane']

    if a > b and a > c:
        print("Winner: Charles Casper Stockham")
    elif b > a and b > c:
        print("Winner: Diana DeGette")
    elif c > a and c > b:
        print("Winner: Raymon Anthony Doane")

# Writes printed values & results into a text file
with open(electionoutput, "a") as txtfile:
    txtfile.write(f"Election Results \n"
                  f"---------------------------- \n"
                  f"Total Votes: {total_votes} \n"
                  f"---------------------------- \n"
                  f"Charles Casper Stockham:  {c1_percentage}%      votes: {d_candidates['Charles Casper Stockham']}\n"
                  f"Diana DeGette:            {c2_percentage}%      votes: {d_candidates['Diana DeGette']} \n"
                  f"Raymond Anthony Doane:    {c3_percentage}%       votes: {d_candidates['Raymon Anthony Doane']} \n"
                  f"---------------------------- \n"
                  f"Winner: Diana DeGette")
