# Author: William Casey Bellew
# GitHub username: psykibear
# Date: 1/22/2023
# Description: Write a program that prompts the user for an integer that the player
# (maybe the user, maybe someone else) will try to guess.
# If the player's guess is higher than the target integer,
# the program should display "too high" If the user's guess is lower than the target integer,
# the program should display "too low" The program should use a loop
# that repeats until the user correctly guesses the integer.
# Then the program should print how many guesses it took.

# ask for initial value for additional user to guess value
print("Enter the integer for the player to guess.")
game = float(input())

# ask for initial guess from user
print("Enter your guess.")
guess = float(input())

# define initial number of tries for counter
tries = 1

# begin guessing game loop
while guess != game:
    if guess > game:
        # if the user guess is greater than the game value, print the necessary message while increasing counter
        tries = (tries + 1)
        print("Too high - try again:")
        guess = float(input())
    elif guess == game:
        # if the user guess is greater than the game value, print the necessary message while increasing counter
        tries = (tries + 1)
        print("you guessed it right in", tries, "tries.")
    else:
        tries = (tries + 1)
        print("Too low - try again:")
        guess = float(input())
print("You guessed it in", tries, "tries.")