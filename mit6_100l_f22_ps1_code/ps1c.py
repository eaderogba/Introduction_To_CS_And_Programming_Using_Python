## 6.100A PSet 1: Part C
## Name: Adebowale Aderogba
## Time Spent: Nil
## Collaborators: Solo

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
portion_down_payment = float(input("Enter the portion for down payment in decimals: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
######################################################################### 
cost_of_down_payment = cost_of_dream_home * portion_down_payment
months = 36
tolerance = 100  # Tolerance for savings amount
max_iterations = 36  # Maximum number of iterations

lower_bound = 0
upper_bound = 1
steps = 0
rate_of_return = None

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
# Perform bisection search
while lower_bound <= upper_bound and steps < max_iterations:
    # Calculate the midpoint rate
    rate = (lower_bound + upper_bound) / 2

    # Calculate predicted savings amount
    savings_needed = initial_deposit * (1 + rate / 12) ** months

    # Check if savings amount is within tolerance
    if abs(savings_needed - cost_of_down_payment) <= tolerance:
        rate_of_return = rate
        break
    elif savings_needed < cost_of_down_payment:
        # Increase the rate (move towards upper bound)
        lower_bound = rate
    else:
        # Decrease the rate (move towards lower bound)
        upper_bound = rate

    # Increase steps
    steps += 1

# Output results
if rate_of_return is not None:
    print(
        f"Best savings rate: {rate_of_return:.4f}\nSteps in bisection search: {steps}")
else:
    print(f"Best savings rate: {rate_of_return:.4f}\nSteps in bisection search: {steps}\nFailed to achieve savings goal within allowed months.")
