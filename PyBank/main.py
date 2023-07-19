# Import modules to be used
import os
import csv

# Access correct file to be used & create file for output info
budgetpath = os.path.join("Resources", "budget_data.csv")
budgetoutput = os.path.join("Analysis", "Budget_Analysis.txt")

# Assign variables
Total_Months = 0
Net_Profit = 0
Average_Change = 0
Net_Change_List = []
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 0]

# Open file & Analyze info by reading each column as a list, while passing over the header
with open(budgetpath) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader)

# Calculate Total Months & Net Profit
    for Row in csvreader:
        Total_Months = Total_Months + 1
        Net_Profit += int(Row[1])

# Open file & Analyze info by reading each column as a list, while passing over the header, and establishing the first line value for calculating Net Change
with open(budgetpath) as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=",")
    csv_header = next(csvreader)
    Row1 = next(csvreader)
    Prev_Net = int(Row1[1])

# Calculate Total Net Change & Average Change
    for Row in csvreader:
        Net_Change = int(Row[1]) - Prev_Net
        Net_Change_List.append(Net_Change)
        Prev_Net = int(Row[1])

        Total_Net_Change = Net_Change
        Average_Change = sum(Net_Change_List) / len(Net_Change_List)
        round(Average_Change, 2)

# Find Greatest Increase & Greatest Decrease in Profits
        if Total_Net_Change > Greatest_Increase[1]:
            Greatest_Increase[0] = Row[0]
            Greatest_Increase[1] = Total_Net_Change
        if Total_Net_Change < Greatest_Decrease[1]:
            Greatest_Decrease[0] = Row[0]
            Greatest_Decrease[1] = Total_Net_Change

# Print all calculated values to terminal

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", Total_Months)
    print("Total: $", Net_Profit)
    print("Average Change: $", round(Average_Change, 2))
    print("Greatest Increase in Profits: ", Greatest_Increase)
    print("Greatest Decrease in Profits: ", Greatest_Decrease)

# Writes the printed values & results into a text file
    with open(budgetoutput, "a") as txtfile:
        txtfile.write(f"Financial Analysis \n"
                      f"--------------------------- \n"
                      f"Total Months: {Total_Months} \n"
                      f"Total: $ {Net_Profit} \n"
                      f"Average Change: $ {round(Average_Change, 2)} \n"
                      f"Greatest Increase in Profits: {Greatest_Increase} \n"
                      f"Greatest Decrease in Profits: {Greatest_Decrease} \n")
