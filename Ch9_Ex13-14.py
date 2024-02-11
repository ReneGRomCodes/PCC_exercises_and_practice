# Exercise 9-13 OrderedDict Rewrite: Start with Exercise 6-4, where you used a standard library to represent a glossary.
# Rewrite the program using the 'OrderedDict' class and make sure the order of the output matches the order in which the
# key-value pairs were added to the dictionary.

# EXERCISE IS OBSOLETE SINCE PYTHON 3.7 AND DOESN'T WORK ANYMORE


# Exercise 9-14 Dice: The 'random' module contains functions that generate random numbers in a variety of ways.
# 'randint' returns an integer in the range you provide. The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class 'Die' with one attribute called 'sides', which has a default value of 6. Write a method called
# 'roll_die()' that prints a random number between 1 and the number of sides the die has. Make a 6-sided, 10-sided and
# 20-sided die and roll each 10 times.


from random import randint


class Die():
    """Represents a series of dice."""

    def __init__(self, sides=6):
        """Initializes attributes for die."""
        self.sides = sides

    def roll_die(self):
        """Rolls a default 6-sided die."""
        print(randint(1, self.sides))


die_6 = Die()
die_6.roll_die()

die_10 = Die(10)
die_10.roll_die()

die_20 = Die(20)
die_20.roll_die()
