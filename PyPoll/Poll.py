# import the modules that you will be using 
import os
import csv

# Create the file paths you will use
CSV_path = os.path.join("Resources", "election_data.csv")
txt_path = os.path.join("Analysis", "Poll.txt")

# Create the variables that you will be using
total_v = 0
candidates = []
total_count = []
percent_votes = []
highest_total = 0
winner = ""

# Open the CSV file and read in the data into a list
with open(CSV_path) as csv_file:
    election_data = csv.reader(csv_file, delimiter=",")
    
    # Skip the Header row in the CSV file
    next(election_data)


    # Start the for loop to get the total number of votes
    for row in election_data:
        total_v += 1

        # Create a list of the candidates/total vote/ and percent_votes 
        if row[2] not in candidates:
            candidates.append(row[2])
            total_count.append(0)
            percent_votes.append(0)

        # Check to see which candidate was voted for in the current row and add to its counter
        for i, candidate in enumerate(candidates):
            if candidate == row[2]:
                total_count[i] += 1     
# Use the candidates respective total votes and divide by total overall votes to get percentage won
for i in range(len(candidates)):
    percent_votes[i] = "{:.3%}".format(total_count[i]/total_v)

    #check to see who has the highest total count and set the winner variable to that candidate
    if total_count[i] > highest_total:
        highest_total = total_count[i]
        winner = candidates[i]

names = [f'{candidates[i]}: {percent_votes[i]} ({total_count[i]})' for i in range(len(candidates))]

# Open the new text file you will write the final analysis into
with open(txt_path, "w") as txt_file:
    txt_file.write("Election Reults\n")
    txt_file.write("--------------------------\n")
    txt_file.write(f"Total Votes: {total_v}\n")
    txt_file.write("--------------------------\n")
    for name in names:
        txt_file.write(f"{name}\n")
    txt_file.write("--------------------------\n")
    txt_file.write(f'Winner: {winner}\n')
    txt_file.write("--------------------------")
  
with open(txt_path) as path:
    print(path.read())
    


