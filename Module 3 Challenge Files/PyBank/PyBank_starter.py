# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_profit_losses = 0
changes = []
months = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit_losses = int(first_row[1])


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - previous_profit_losses
        changes.append(net_change)
        months.append(row[0])

         # Track the total and net change
    
        previous_profit_losses = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(changes)
        greatest_increase_month = months[changes.index(greatest_increase)]

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(changes)
        greatest_decrease_month = months[changes.index(greatest_decrease)]

# Calculate the average net change across the months
average_change = sum(changes) / len(changes)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"-------------------"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change: .2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
