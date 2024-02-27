# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 1/15/2023
# Description: Write a program that asks the user for a (integer) number of cents, from 0 to 99, and
# outputs how many of each type of coin would represent that amount with the fewest total number of coins.
# starting by defining the necessary coin variables
q_value = 25
d_value = 10
n_value = 5
p_value = 1

# ask the user to input a number of cents.
cents = int(input("Please enter an amount in cents less than a dollar."))

# create variables for the output of necessary coins to give to the user
quarters = int(cents/q_value)
dimes = int((cents - quarters*q_value)/d_value)
nickels = int((cents - quarters*q_value - dimes*d_value)/n_value)
pennies = int((cents - quarters*q_value - dimes*d_value - nickels*n_value)/p_value)

# printing out the appropriate phrase
print("Your change will be:")

# output the necessary coins to give to the user
print("Q: " + str(quarters))
print("D: " + str(dimes))
print("N: " + str(nickels))
print("P: " + str(pennies))


