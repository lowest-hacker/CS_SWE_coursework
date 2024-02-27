# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 2/4/2023
# Description: Write a recursive function named multiply that takes two positive integers as parameters and
# returns the product of those two numbers (the result from multiplying them together).
# Your program should not use multiplication - it should find the result by using addition.


# recursive function to calculate
# multiplication of two numbers
def multiply(multiplyer, multiplicand):
    """sets up recursion for stepping into the multiplyer number multiplied by the multiplicand using addition only"""
    # initial setup of if statement in order to set up the recursive function for each time needing to add the multiplyer
    if multiplicand != 0:
        return multiplyer + multiply(multiplyer, multiplicand - 1)
    # sets up additional check for if the value of the multiplicand variable is zero
    else:
        return 0

