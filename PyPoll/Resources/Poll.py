import csv

# SPECIFY THE FILE TO READ FROM
csvpath = "election_data.csv"

with open(csvpath, encoding="utf-8") as csvfile:
    # INITIALIZE CSV READER
    csvreader = csv.reader(csvfile, delimiter=",")

    # SKIP THE HEADER ROW
    next(csvreader)

    # Initialize variables
    candidatelist = []
    votes = {}

    for row in csvreader:
        candidate = row[2]

        # If the candidate is not in the list, add them and initialize their vote count to 0
        if candidate not in candidatelist:
            candidatelist.append(candidate)
            votes[candidate] = 0

        # Increment the vote count for the candidate
        votes[candidate] += 1

    # Calculate the total number of votes
    total_votes = sum(votes.values())
    winner=max(votes, key=votes.get)

    print("Election Results\n")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
    print(f"Total votes: {total_votes}\n")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
    for i in votes:
        percentvotes= (votes[i]/total_votes)*100
        print(f"{i}: {percentvotes:.3f}% ({votes[i]})\n")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
    print("Winner: ", winner )

output= "PyPoll_results.txt"

with open(output, "w+") as file:
    file.write("Election Results\n")
    file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
    file.write(f"Total votes: {total_votes}\n")
    file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
    
    for i in votes:
        percentvotes = (votes[i] / total_votes) * 100
        file.write(f"{i}: {percentvotes:.3f}% ({votes[i]})\n")
    
    file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
    file.write(f"Winner: {winner}\n")