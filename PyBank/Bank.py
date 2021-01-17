# import libraries 
import os
import csv

# Declare the variable that you think you might be using 

months = 0
net_total = 0
avg_change = []
greatest_increase = 0
greatest_decrease = 0
current = 0
past = 0
month_increase = ""
month_decrease = ""

# Read in the data into a list

csv_path = os.path.join( "Resources", "budget_data.csv")
txt_outpath = os.path.join("Analysis", "bank.txt")

with open(csv_path) as csv_file:
    budget_data = csv.reader(csv_file, delimiter = ",")
    header = next(budget_data)

    # Create a for statements that will go thorugh each row in the dataset that was read in
    for  i, row in enumerate(budget_data):

        # Increase the  month counter for to receive the total number of months
        months += 1

        # Start adding the profit losses to net_total to get the final net_total
        net_total += int(row[1])

        # Create the list of profit/losses changes month to month for the entire data set
        if i > 0:
            current = int(row[1])
            avg_change.append(current - past)
            monthly_change = current - past

            # Check to see if the monthly_change is greater than the greatest_increase thus far and if so update.
            if monthly_change > greatest_increase:
                month_increase = row[0]
                greatest_increase = monthly_change
            
            # Check to see if the monthly_change is less than the greatest_decrease thus far and if so update.
            elif monthly_change < greatest_decrease:
                month_decrease = row[0]
                greatest_decrease = monthly_change
            past = int(row[1])
        else:
            past = int(row[1])

# Calculate the avg_change using sum and len
avg_change = round(sum(avg_change)/len(avg_change), 2)

# Open a new file where we will write our Analysis to and start writing
with open(txt_outpath, "w") as outfile:
    outfile.write("Financial analysis\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"Total Months: {months}\n")
    outfile.write(f"Total: ${net_total}\n")
    outfile.write(f"Average Change: ${avg_change}\n")
    outfile.write(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})\n")

# Open the new file you just created and also print the results on the terminal 
with open(txt_outpath) as print_file:
    print(print_file.read())
