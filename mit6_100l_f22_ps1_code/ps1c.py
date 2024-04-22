## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))
portion_down_payment = 0.25
cost_of_dream_home = 800000
cost_of_down_payment = cost_of_dream_home * portion_down_payment
months = 36
#########################################################################
## Initialize other variables you need (if any) for your program below ##
######################################################################### 
lower_bound = 0
upper_bound = 1
tolerance = 100
steps = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
while steps < 36:
    # Calculates the rate midpoint
    r = (lower_bound + upper_bound) / 2

    # Determines the amount of savings needed
    savings_needed = initial_deposit * (1 + r / 12) ** months

    # Detrmines if the savings is withing the tolerance
    if abs(savings_needed - cost_of_down_payment) <= tolerance:
        print(f"Savings amount achieved within tolerance: {savings_needed:.2f}")
        break
    elif savings_needed < cost_of_down_payment:
        # There is then a need to increase the rate, by shifting towards the upper bound i.e.,
        lower_bound = r
    else:
        # The rate decreases towards the lower bound
        upper_bound = r
    # Increase steps
    steps += 1

    # This checks if the amount is not achievable within the tolerance. In this case r is set to None
    if savings_needed < cost_of_down_payment - tolerance and steps == 36:
        r = None

print(f"Steps taken: {steps}")
print(f"Minimum rate of return needed: {r:.4f}" if r is not None else "Best savings rate: None \nCannot achieve savings goal")
