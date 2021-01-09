# import the modules that you will be using 
import os
import csv

# Create the file paths you will use
CSV_path = os.path.join("Resources", "election_data.csv")

# Create the variables that you will be using
total_v = 0
candidates = []
total_count = []
percent_votes = []
count = 0

# Open the CSV file and read in the data into a list
with open(CSV_path) as csv_file:
    election_data = csv.reader(csv_file, delimiter=",")
    
    # Skip the Header row in the CSV file
    next(election_data)


    # Start the for loop to get the total number of votes
    for row in election_data:
        total_v += 1

        # Create a list of the candidates/total vote/ and percent_votes of equal length to be zipped later
        if row[2] not in candidates:
            candidates.append(row[2])
            total_count.append(0)
            percent_votes.append(0)
        for i, candidate in enumerate(candidates):
            if candidate == row[2]:
                total_count[i] += 1
    # cerate a list for total_count and percent_votes with the same lenght as the candidates list
    #or row in election_data:
        #count += 1
       
print(total_v)
print(candidates)
print(total_count)
print(percent_votes)
#print(count)    

