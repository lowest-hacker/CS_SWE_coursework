# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 2/12/23
# Description: Write a function named add_surname that takes as a parameter a list of first names.
# It should use a list comprehension to return a list that contains only those names that start with a "K",
# but with the surname "Kardashian" added to each one, with a space between the first and last names.
# You may assume that all names in the list begin with a capital letter.

"""Setting up function to add the "surname" to the first name in the list provided by the user"""


def add_surname(forenames_list):
    fullname_list = [name+' Kardashian' for name in forenames_list if name[0] == 'K']
    """ name specifies the forename in the list provided by the user so that it can be used in the for/in 
    function while checking that the first letter in the name is a upper case K"""
    # looks through the provided list to add "Kardashian" to the end of the name
    # if and ONLY if the name starts with a K
    return fullname_list
