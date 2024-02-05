# Exercise 4-10 Slices: Using one of the lists from this chapter, add several lines that print the following using
# slices:
# Print the first the items in the list and the message "The first three items in the list are: ".
# Print the three items the middle of the list and the message "Three items from the middle of the list are: ".
# Print the last the items in the list and the message "The last three items in the list are: ".


players = ["charles", "martina", "michael", "florence", "eli"]

print("The first three items in the list are:", players[:3])
print("Three items from the middle of the list are:", players[1:4])
print("The last three items in the list are:", players[-3:])


# Variation using a 'for' loop for a neat printout.
print("\nThe first three items in the list are:")
for player in players[:3]:
    print("\t", player.title())

print("\nThree items from the middle of the list are:",)
for player in players[1:4]:
    print("\t", player.title())

print("\nThe last three items in the list are:")
for player in players[-3:]:
    print("\t", player.title())


# Variation for printing three items from the approximate middle of a list, regardless of the length of the list.
players = [
    "emma", "liam", "olivia", "noah", "ava", "william", "sophia", "james", "isabella", "oliver", "charles", "florence",
    "charlotte", "benjamin", "amelia", "elijah", "mia", "lucas", "harper", "mason", "evelyn", "logan", "martina",
    "abigail", "alexander", "emily", "ethan", "elizabeth", "jacob", "avery", "michael", "sofia", "daniel", "eli"
]

middle_of_list = int(len(players) / 2)  # Getting the approximate middle of the list and returning an integer.
n = middle_of_list - 1  # Calculating first index 'n' to be slightly before the middle of the list.
m = middle_of_list + 2  # Calculating the second index 'm' to be slightly after the middle of the list.

print("\nThree items from the middle of the list are:",)
for player in players[n:m]:  # Using 'n' and 'm' to print the items around the middle of the list.
    print("\t", player.title())


# Exercise 4-11 My Pizzas, Your Pizzas: Start with your program from Exercise 4-1, make a copy of the list of pizzas and
# call it 'friend_pizzas'.
# Then, add a new pizza to the original list and add a different pizza to the list 'friend_pizzas'. Prove that you have
# two separate lists by printing the messages "My favorite pizzas are: " and "My friend's favorite pizzas are: " and
# use 'for' loops to print the contents of each list.


pizzas = ["pepperoni", "cheese", "veggie", "buffalo chicken"]
friend_pizzas = pizzas[:]

pizzas.append("margherita")
friend_pizzas.append("pineapple")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print("\t", pizza.title(), "pizza")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    if pizza == "pineapple":  # Couldn't help myself here, it had to be done. Sorry.
        print("\t", pizza.title(), "pizza and they actually think that it is a valid choice.")
    else:
        print("\t", pizza.title(), "pizza")


# Exercise 4-12 More Loops: All versions of 'foods.py' in this chapter have avoided using 'for' loops when printing to
# save space. Choose a version of 'foods.py' and write two 'for' loops to print each list of foods.


my_foods = ["pizza", "falafel", "carrot cake", "cannoli"]
friend_foods = ["pizza", "falafel", "carrot cake", "ice cream"]

for food in my_foods:
    print(food)

for food in friend_foods:
    print(food)


# Exercise 4-13 Buffet: A buffet-style restaurant offers only five basic foods. Think of 5 basic foods and store them in
# a tuple.
# The restaurant changes its menu, replacing two of the items with different food. Add a block of code that rewrites the
# tuple, then use a 'for' loop to print each item on the revised menu.


foods = ("rice", "chicken", "broccoli", "pasta", "bread")

print("\nOriginal buffet:")
for food in foods:
    print("\t", food.title())

old_buffet = foods  # Stored the old tuple before reassigning new values to it, so it doesn't get lost in the process.
foods = ("rice", "chicken", "tomatoes", "pasta", "potatoes")

print("\nNew buffet:")
for food in foods:
    print("\t", food.title())
