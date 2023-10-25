import csv

#path to collect data
budget_data = "Resources/budget_data.csv" 

#output to text file
output = "Analysis/budget_homework.txt"

total_profits = 0
total_months = 0
previous_profit = 0
profit_changes = []
months = []

#open datafile and get totals
with open(budget_data) as infile:

        rows=csv.reader(infile)

        header = next(rows)

        for row in rows:
                
                total_profits += int(row[1])

                total_months += 1

                profit_change = int(row[1]) - previous_profit
                
                previous_profit = int(row[1])

                profit_changes.append(profit_change)

                months.append(row[0])

profit_changes=profit_changes[1:]


average_change = sum(profit_changes) / len(profit_changes)

months = months[1:]

largest_increase = max(profit_changes)

index = profit_changes.index(largest_increase)

#print(index)

#print(profit_changes)

print(largest_increase)

#print(months)

#print(months[index])

#print(profit_changes[index])

#print(len(months))

#print(len(profit_changes))


#largest_increase_date = str()




                
