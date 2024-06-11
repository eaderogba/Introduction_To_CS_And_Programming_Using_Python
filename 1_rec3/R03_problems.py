# Problem 1 - Bisection Search Practise
# Write a program using bisection search to find the forth root of a number inputted by the 
# user. Print the forth root calculated with max error of 0.01. 

# x = float(input("Using bisection search calculate the forth root of: " ))
# epsilon = 0.01
# low = 0
# high = x

# # Find the midsection of the interval between low and high
# ans = (low + high)/2

# while abs((ans**4) - x) >= epsilon:
#     if ans**4 > x:
#         high = ans
#     else:
#         low = ans
#     ans = (low + high)/2
# print(f"The forth root of {x} is {ans}")





# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range.
# num = int(input("Enter your number: "))
# lower = int(input("Enter lower: "))
# higher = int(input("Enter higher: "))

# def falls(number, x, y):
#     if num in range(number, x, y+1):
#         print(f"Yes {num} in range")
#     else:
#         print(f"{num} not in range")

# falls(num, lower, higher)





# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).
x = int(input("Enter a number: "))

def perfect_num(value):
    result = 0
    for num in range(1, x):
        if x%num == 0:
            result += num
    return result == value
print(perfect_num(x))
    




# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the forth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.

# example initial parameters
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0



