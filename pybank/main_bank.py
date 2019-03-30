#import OS and CSV libraries
import os
import csv

#create variables for calculations
month_counter = 0
sum_revenue = 0
sum_revenue_change = 0

#Insert file location here
file = os.path.join('..',"pythonHW", "bank_data.csv")
file_output=os.path.join('..',"pythonHW", "bank_data.txt")
    
#open file and create file handle
with open(file,newline="") as csv_file:
        csv_reader = csv.reader(csv_file)

        #skip header row
        line = next(csv_reader,None)

        #grab data from first line
        line = next(csv_reader,None)
        max_month = line[0]
        min_month = line[0]
        revenue = float(line[1])
        min_revenue = revenue
        max_revenue = revenue
        previous_revenue = revenue
        month_counter = 1
        sum_revenue = float(line[1])
        sum_revenue_change = 0

        #read one line at a time
        for line in csv_reader:

            #increase counter for number of months in dataset
            month_counter = month_counter + 1

            revenue = int(line[1])

            #add to sum of revenue for data set
            sum_revenue = sum_revenue + revenue

            #find change in revenue between this month and last month
            revenue_change = revenue - previous_revenue

            #add change in revenue to net change in revenue for data set
            sum_revenue_change = sum_revenue_change + revenue_change

            #determine if change in revenue is a max or min for data set thus far
            if revenue_change > max_revenue:
                max_month = line[0]
                max_revenue = revenue_change

            if revenue_change < min_revenue:
                min_month = line[0]
                min_revenue = revenue_change

            #set previous revenue to revenue
            previous_revenue = revenue

       
  #Average change
    average_revenue_change = round(sum_revenue_change/(month_counter-1),2)
        
#print analysis to terminal

output= (
            f"\nFinancial Analysis \n"
            f"-------------------------------------------------------\n"
            f"Total Months: {month_counter}\n"
            f"Total : {sum_revenue}\n"
            f"Average  Change: {average_revenue_change}\n"
            f"Greatest Increase in Profit: {max_month} {max_revenue}\n"
            f"Greatest Decrease in Profit: {min_month} {min_revenue}\n")
            
      
print(output)
        
#write a text file in order to export results to text file

with open (file_output, "w") as txt_file:
    txt_file.write(output)