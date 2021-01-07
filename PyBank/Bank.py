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

with open(csv_path) as csv_file:
    budget_data = csv.reader(csv_file, delimiter = ",")
    next(budget_data)

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

            # Check to see if the current is greater than the past and if so update greatest_increase
            if current > greatest_increase:
                month_increase = row[0]
                greatest_increase = current
            
            # Check to see if the current is less than the past and if so update greatest_decrease
            elif current < greatest_decrease:
                month_decrease = row[0]
                greatest_decrease = current
            past = int(row[1])
        else:
            past = int(row[1])
avg_change = round(sum(avg_change)/len(avg_change), 2)
print(avg_change)
print(month_increase)
print(greatest_increase)
print(month_decrease)
print(greatest_decrease)

   
          









