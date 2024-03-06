import csv

                        # SPECIFY THE FILE TO READ FROM
csvpath = "budget_data.csv"

with open(csvpath, encoding="utf-8") as csvfile:
                        # INITIALIZE CSV READER
    csvreader = csv.reader(csvfile, delimiter=",")

                        # SKIP THE HEADER ROW
    next(csvreader)

                        # INITIALIZE VARIABLES
    months = 0
    total_net = 0
    changes = []
    previous_profit = 0

                        # STORE DATA FOR THE GREATEST INCREASE AND DECREASE
    max_change_index = None
    max_loss_index = None
    max_change_month = None
    max_loss_month = None

                        # LOOP THROUGH THE ENTIRE COLUMN
    for index, row in enumerate(csvreader, start=2):  
        months += 1
        total_net += int(row[1])

        if months > 1:
            profit_change = int(row[1]) - previous_profit
            changes.append(profit_change)

            if profit_change == max(changes):
                max_change_index = index
                max_change_month = row[0]  

            if profit_change == min(changes):
                max_loss_index = index
                max_loss_month = row[0]  

        previous_profit = int(row[1])

                        # CALCULATE RESULTS
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)

print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(" ")

print("Total Months:", months)
print("Total Net Amount:", total_net)
print(f"Average Change: {average_change:.2f}")

                        # DISPLAY THE MONTH OF GREATEST INCREASE
print("Greatest Increase in Profits:", max_change_month, "($", greatest_increase, ")")

                        # DISPLAY THE MONTH OF GREATEST DECREASE
print("Greatest Decrease in Profits:", max_loss_month, "($", greatest_decrease, ")")

                        #CREATES THE TXT FILE
output = "Pybank_results.txt"

                        #PRINTS THE RESULTS IN A TXT FILE
with open(output, "w+") as file:
    file.write("Financial Analysis\n")
    file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n\n")
    file.write(f"Total Months: {months}\n")
    file.write(f"Total Net Amount: ${total_net}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {max_change_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {max_loss_month} (${greatest_decrease})\n")
