# Exercise 5-3 Alien Colors #1: An Alien was just shot down in a game. Create a variable 'alien_color' and assign it a
# value of 'green', 'yellow' or 'red'. Write an 'if' statement to test whether the alien's color is green and print a
# message that the player earned 5 points if it is.
# Write a version of the program that passes the 'if' test and one that fails.


message = "You earned 5 points"

alien_color = "green"

if alien_color == "green":
    print(message)

if alien_color == "yellow":
    pass


# Exercise 5-4 Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3 and write an 'if-else' chain.
# If the aliens color is green, print a statement that the player earned 5 points for shooting the alien and 10 points
# if it isn't green.
# Write one version of the program that runs the 'if' block and one that runs the 'else' block.


message_green = "You earned 5 points"
message_other = "You earned 10 points"

alien_color = "green"  # Color green to run the 'if' block

if alien_color == "green":
    print(message_green)
else:
    print(message_other)


alien_color = "yellow"  # Color yellow to run the 'else' block

if alien_color == "green":
    print(message_green)
else:
    print(message_other)


# Alternative to multiple 'if-else' blocks using a list for alien colors and a 'for' loop. Bear in mind that it doesn't
# check the variable anymore. Its purpose is to cycle through the 'if-else' chain:
alien_colors = ["green", "yellow", "red"]

for color in alien_colors:
    if color == "green":
        print(message_green)
    else:
        print(message_other)


# Exercise 5-5 Alien Colors #3: Turn your 'if-else' chain from Exercise 5-4 into an 'if-elif-else' chain.
# 5 points if the alien is green, 10 if it is yellow and 15 if it is red.
# Write three versions of the program, making sure each message is printed for the appropriate color.


message_green = "You earned 5 points"
message_yellow = "You earned 10 points"
message_red = "You earned 15 points"

alien_color = "green"  # Color green to run the 'if' block

if alien_color == "green":
    print(message_green)
elif alien_color == "yellow":
    print(message_yellow)
else:
    print(message_red)


alien_color = "yellow"  # Color yellow to run the 'elif' block

if alien_color == "green":
    print(message_green)
elif alien_color == "yellow":
    print(message_yellow)
else:
    print(message_red)


alien_color = "red"  # Color red to run the 'else' block

if alien_color == "green":
    print(message_green)
elif alien_color == "yellow":
    print(message_yellow)
else:
    print(message_red)


# Alternative to multiple 'if-elif-else' blocks using a list for alien colors and a 'for' loop. Bear in mind that it
# doesn't check the variable anymore. Its purpose is to cycle through the 'if-elif-else' chain:
alien_colors = ["green", "yellow", "red"]

for color in alien_colors:
    if color == "green":
        print(message_green)
    elif color == "yellow":
        print(message_yellow)
    else:
        print(message_red)


# Exercise 5-6 Stages of Life: Write an 'if-elif-else' chain that determines a person's stage of life. Set a value for
# valuable 'age' and print a message stating the stage of life:
# - Less than 2 years old, a baby.
# - At least 2 but less than 4 years old, a toddler.
# - At least 4 but less than 13, a child.
# - At least 13 but less than 20, a teenager.
# - At least 20 but less than 65, an adult.
# - At least 65, an elder.


message = "This person is"
baby = "a baby"
toddler = "a toddler"
child = "a child"
teenager = "a teenager"
adult = "an adult"
elder = "an elder"

age = int(input("Enter person's age: "))  # Alternative: user input to set a value for variable 'age'.

if age < 2:
    print(message, baby)
elif age < 4:
    print(message, toddler)
elif age < 13:
    print(message, child)
elif age < 20:
    print(message, teenager)
elif age < 65:
    print(message, adult)
else:
    print(message, elder)


# Exercise 5-7 Favorite Fruit: Choose three of your favorite fruits and add them to a list called 'favorite_fruits, then
# write a series of five 'if' statements that check for certain fruits in your list. If the fruit is in your list, the
# 'if' block should print a statement such as "You really like bananas!".


favorite_fruits = ["strawberries", "bananas", "cherries"]

if "apples" in favorite_fruits:
    print("You really like apples!")
if "blueberries" in favorite_fruits:
    print("You really like blueberries!")
if "strawberries" in favorite_fruits:
    print("You really like strawberries!")
if "bananas" in favorite_fruits:
    print("You really like bananas!")
if "cherries" in favorite_fruits:
    print("You really like cherries!")


# Variant using a second list 'fruits' containing the fruits to check for in list 'favorite_fruits' and a 'for' loop:
fruits = ["apples", "blueberries", "strawberries", "bananas", "cherries"]

for fruit in fruits:
    if fruit in favorite_fruits:
        print("You really like", fruit + "!")
