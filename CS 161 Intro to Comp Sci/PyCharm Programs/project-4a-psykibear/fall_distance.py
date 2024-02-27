# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 1/30/2023
# Description: The following formula can be used to determine the distance an
# object falls due to gravity in a specific time period:
#
# d = (1/2)gt2
#
# where d is the distance in meters, g is 9.8, and t is the time in seconds that the object has been falling.
# Write a function named fall_distance that takes the time in seconds as an argument.
# The function should return the distance in meters that the object has fallen in that time.
# For example if the function is passed the value 3.2, then it should return the value 50.176.
# Your function does not need to print anything out - just return a value.

gravity = 9.8


def fall_distance(defined_time):
    """Function is aiming to output the distance that an item is falling based on timing and gravitational pull"""
    dist = (1/2)*gravity*defined_time**2
    return dist
