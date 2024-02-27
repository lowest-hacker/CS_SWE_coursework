# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 2/20/23
# Description: Write a function named reverse_list that takes as a parameter a list and reverses the order
# of the elements in that list. It should not return anything - it should mutate the original list.
# This can be done trivially using slices, but your function must not use any slicing (you may use indexing,
# but not slicing).

def reverse_list(vals):
    """defines a function that uses the initial position of a value in a set then reverses the position based off
    the length of the set provided by the user"""

    beginning_position = 0
    new_position = len(vals)-1
    # initial values of the positions of first number in the set with the last being the total length
    # minus 1 since the initial value is at position zero

    while beginning_position < new_position:
        step_change = vals[beginning_position]
        vals[beginning_position] = vals[new_position]
        vals[new_position] = step_change
        beginning_position += 1
        new_position -= 1
    # while function to continue the loop until the user has gotten to the center of the list.
