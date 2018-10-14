#import the necessary modules
import os
import csv

#file to output
file_to_output = os.path.join("PyBank.txt")
#read in csv file
budget_csv = os.path.join("budget_data.csv") 
with open(budget_csv, 'r') as budgetcsv:
    DifferencesFromPrevious = []
    budgetreader = csv.reader(budgetcsv, delimiter = ",")
    csv_header = next(budgetreader)
    first_row = next(budgetreader)
    Previous = int(first_row[1])
    TotalMonths = 1
    TotalProfitLoss = int(first_row[1])


    for row in budgetreader:   
        TotalMonths = TotalMonths + 1
        TotalProfitLoss += int(row[1])
        differenceFromPrevious = int(row[1]) - Previous
        Previous = int(row[1])
        DifferencesFromPrevious.append(int(differenceFromPrevious))
        AverageChange = sum(DifferencesFromPrevious)/len(DifferencesFromPrevious)
        Max = max(DifferencesFromPrevious)
        Min = min(DifferencesFromPrevious)
       
   
    
output = (
    f"\nPyBank Analysis\n"
    f"-------------------------\n"
    f"Total Months: {TotalMonths}\n"
    f"Total Net Profit/Loss: {TotalProfitLoss}\n"
    f"Average Change in Profit/Loss: {AverageChange}\n"
    f"Greatest Increase in Profits: {Max}\n"
    f"Greatest Decrease in Losses: {Min}\n")
 
 
print(TotalMonths)
print(TotalProfitLoss)
print(AverageChange)
print(Max)
print(Min)
print(output)    

#Save the results to analysis text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(output)

    
    
