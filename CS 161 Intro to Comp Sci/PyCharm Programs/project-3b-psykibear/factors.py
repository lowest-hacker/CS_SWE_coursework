# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 1/22/2023
# Description: Write a program that asks the user to enter a positive integer,
# then prints a list of all positive integers that divide that number evenly,
# including itself and 1, in ascending order.

# get users initial input for the positive integer to define the factors values
positive = int(input("Please enter a positive integer:"))
# display user inputted value for the necessary factors
print("The factors of", positive, "are:")
factor_check = positive
# while loop to determine and print all factors of user positive integer
while factor_check > 0:
    # calculate division factor
    factor = (positive / factor_check)
    # if else statement that verifies even number without any decimals for factor
    if factor in range(1, positive+1, 1):
        # prints factor
        print(int(factor))
    else:
        factor = 0
    # continue loop through each check
    factor_check = factor_check - 1