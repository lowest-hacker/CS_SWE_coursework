# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 2/4/2023
# Description: Write a class named Taxicab that has three private data members: one that holds the current x-coordinate,
# one that holds the current y-coordinate, and one that holds the current odometer reading. An odometer simply measures
# the distance a car or bicycle has traveled by keeping track of how many times its wheels have turned.
# So if you travel one unit left, and then one unit right, you'll be back where you started, but your odometer
# will tell you that you've traveled 2 units. All three data members should be updated as needed
# so that they are always current.
#
# The class should have an init method that takes two parameters and uses them to initialize the coordinates,
# and also initializes the odometer to zero.
#
# The class should have get methods for each data member: get_x_coord, get_y_coord, and get_odometer.
# The class does not need any set methods.
#
# It should have a method called move_x that takes a parameter that tells how far the Taxicab should
# shift left or right. It should have a method called move_y that takes a parameter that tells how far
# the Taxicab should shift up or down.

class Taxicab:
    """Defining the class for Taxicab;
    specific data sets for x coordinate, y coordinate, and odometer reading"""

    def __init__(self, x_coordinate, y_coordinate):
        """initialize x and y coordinate with the odometer set at zero"""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.odometer = 0

    def get_x_coord(self):
        """get method for x_coordinate of starting point for the taxicab"""
        return self.x_coordinate

    def get_y_coord(self):
        """get method for y_coordinate of starting point for the taxicab"""
        return self.y_coordinate

    def get_odometer(self):
        """get method for the taxicab's odometer"""
        return self.odometer

    def move_x(self, vertical):
        """moves taxi cab to the left or right. left if a negative value with right being a positive value.
        absolute value of the distance moved gets added to the odometer"""
        self.x_coordinate += vertical
        self.odometer += abs(vertical)

    def move_y(self, horizontal):
        """moves taxi cab to the up or down. down if a negative value with up being a positive value.
        absolute value of the distance moved gets added to the odometer"""
        self.y_coordinate += horizontal
        self.odometer += abs(horizontal)


