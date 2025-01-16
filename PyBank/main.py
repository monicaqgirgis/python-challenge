# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join('Analysis', 'budget_analysis.txt')

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_profit = None
changes = []
dates = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    for row in readerpy

    # Track the total and net change


    # Process each row of data
    #for row in reader:

        # Track the total


        # Track the net change