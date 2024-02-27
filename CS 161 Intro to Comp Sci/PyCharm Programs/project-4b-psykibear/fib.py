# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 1/30/2023
# Description: The first and second numbers in the Fibonacci sequence are both 1.
# After that, each subsequent number is the sum of the two preceding numbers.
# The first several numbers in the sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, etc.
# Write a function named fib that takes a positive integer parameter and
# returns the number at that position of the Fibonacci sequence.
# For example fib(1) = 1, fib(3) = 2, fib(10) = 55, etc.
# Your function does not need to print anything out - just return a value.


def fib(sequence):
    """
    Function to output the number at the positive integer parameter that the user puts in for the Fibonacci sequence
    """
# setting up the initial sequence of the fibonacci sequence with the first 2 values equalling 1
    fibonacci_sequence1 = 1
    fibonacci_sequence2 = 1
# setting up an if else statement so that if the user puts 1 it will output the initial value
    if sequence == 1:
        return fibonacci_sequence1
    else:
        # a for loop created to setup the range based off the sequence input that the user would use
        for fibonacci_sequence in range(1, sequence):
            term = fibonacci_sequence1 + fibonacci_sequence2
            fibonacci_sequence1 = fibonacci_sequence2
            fibonacci_sequence2 = term
            return term
