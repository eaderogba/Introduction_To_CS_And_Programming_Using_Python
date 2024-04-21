## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:
import time

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Record start time
start_time = time.time()

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
cost_of_down_payment = cost_of_dream_home * portion_down_payment
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
"""Here, the program loops until the"""
while amount_saved <= cost_of_down_payment:
    amount_saved += (yearly_salary / 12 * portion_saved) + (amount_saved * r / 12)
    if months % 6 == 0 and months != 0:
        yearly_salary = yearly_salary + (yearly_salary * semi_annual_raise)
    months += 1

print(f"At this rate, it will take you {months} to save up for the down payment")

# Record the end time
end_time = time.time()
# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.5f} seconds")