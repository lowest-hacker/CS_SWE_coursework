# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 2/12/23
# Description: Write a function named find_median that takes as a parameter a list of numbers.
# The function should return the statistical median of those numbers, which will require it to sort the list.
# If you're not familiar with calculating the median, please look at the definition.
# Remember that the calculation is different for odd and even groups of values.
# Also remember that the same group of numbers should always have the same median,
# regardless of what order the numbers were listed in.

"""Setting up program function for finding the median value of a list the user inputs"""
"""Definition of median is The median is the value in the middle of a data set, 
meaning that 50% of data points have a value smaller or equal to the median and 50% of data points 
have a value higher or equal to the median."""


def find_median(num_list):
    """Returns the median value of the numbers in num_list"""
    num_list.sort()
    if len(num_list) % 2 == 1:
        # verifies the length of the list and changes the setup dependent on the size including the given thoughts
        # even if the median needs to calculate based on the 2 middle numbers
        return num_list[len(num_list) // 2]
        # using floor division to return the rounded up value
    else:
        return (num_list[(len(num_list) // 2) - 1] + num_list[len(num_list) // 2]) / 2
        # using floor division to return the rounded up value

