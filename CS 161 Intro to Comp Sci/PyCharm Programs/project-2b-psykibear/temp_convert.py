# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 1/15/2023
# Description: Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is:
# F = (9/5)C + 32
# where F is the Fahrenheit temperature and C is the Celsius temperature.
# The program should prompt the user to input a Celsius temperature and
# should display the corresponding Fahrenheit temperature.
# It should display only the converted temperature on its own line without additional text (such as an 'F').


C_value = float(input("Please enter a Celsius Temperature."))
# captures the user's celsius temperature
F_value = float(((9/5)*C_value)+32)
# creates a variable for the converted temperature to Fahrenheit
print("The equivalent Fahrenheit temperature is:")
print(F_value)
# prints the converted Fahrenheit temperature
