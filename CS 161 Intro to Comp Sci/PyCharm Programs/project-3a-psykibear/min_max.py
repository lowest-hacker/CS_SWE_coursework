# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 1/22/2023
# Description: Write a program that asks the user how many integers they would like to enter.
# You can assume that this initial input will be an integer >= 1.
# The program will then prompt the user to enter that many integers.
# After all the numbers have been entered, the program should display the largest and smallest of those numbers
# (no, you cannot use lists, or any other material we haven't covered).
# Your code should work correctly no matter what integers the user enters.

# define number of integers that the user would like to put in for comparison
print("How many integers would you like to enter?")
user_input = int(input())

# initial definition of min/max as zero prior to while loop re defining the value during the loop conditions
user_max = 0
user_min = 0
comparison_value = 0

# Print initial request for necessary number of integers
print("Please enter ", user_input, "integers.")

# While loop defining the min and max values during each input from the user
while user_input > 0:
    comparison_value = int(input())
    # comparing user inputs to define minimum value of integers
    if comparison_value < user_min:
        user_min = comparison_value
    else: user_min = user_min
    # comparing user inputs to define maximum value of integers
    if comparison_value > user_max:
        user_max = comparison_value
    else: user_max = user_max
    user_input = user_input - 1

# output the min and max values found during the comparison loop
print("min:", user_min)
print("max:", user_max)