# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 2/20/23
# Description: Write a function named square_list that takes as a parameter a list of numbers and
# replaces each value with the square of that value. It should not return anything -
# it should mutate the original list.

def square_list(nums):
    """writing a function that takes the list provided by the user "nums" and
    produces the same length list with each value "squared" """
    for square in range(len(nums)):
        nums[square] = nums[square]*nums[square]

