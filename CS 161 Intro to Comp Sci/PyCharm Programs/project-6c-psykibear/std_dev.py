# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 2/12/23
# Description:Write a class called Person that has two private data members - the person's name and age.
# It should have an init method that takes two values and uses them to initialize the data members.
# It should have a get_age method.


# Write a separate function (not part of the Person class) called std_dev that takes as a parameter
# a list of Person objects and returns the standard deviation of all their ages
# (the population standard deviation that uses a denominator of N, not the sample standard deviation,
# which uses a different denominator).


# To calculate the standard deviation, you'll need to take a square root, which you can do by just using an
# exponent of 0.5. For example, the result of 9 ** 0.5 would be 3.0. Python does have a specific sqrt() function,
# but that involves importing a module, which we haven't covered yet.

"""setting up the class defined as Person with the initial function to grab the name and age of the person"""
"""The following are the necessary steps for calculating the standard deviation:
Step 1: Find the mean
Step 2: Find each score’s deviation from the mean
Step 3: Square each deviation from the mean
Step 4: Find the sum of squares
Step 5: Find the variance
Step 6: Find the square root of the variance
"""


class Person:

    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age
        # initialization function to define into variable the person's name and age from the list the user provides

    def get_age(self):
        return self.person_age
        # get function to the specific person's age for calculating out the standard deviation


"""setting up the secondary function that returns the standard deviation of all their ages
(the population standard deviation that uses a denominator of N, not the sample standard deviation,
which uses a different denominator)."""


def std_dev(person_list):
    # setting up the function to calculate out the standard deviation using the list provided by the user
    total_person_ages = 0
    # creating the initial variable regarding the total that is required to calculate the standard deviation
    for person in person_list:
        # for in function using the variable person to get from the person list
        total_person_ages += person.get_age()
        # combining the age's listed in the list provided by the user
    person_mean_age = total_person_ages / len(person_list)
    # calculating the average (mean) of all the ages in the list provided by the user

    ages_squared_sum = 0
    # setting up the initial variable for the squared sum of the ages that are going to be calculated
    for person in person_list:
        ages_squared_sum += (person_mean_age - person.get_age()) ** 2

    return (ages_squared_sum / len(person_list)) ** 0.5
    # returns the squared sum of the ages so that it can be divided by the number of people in the list
    # followed by finding the square root of the value


