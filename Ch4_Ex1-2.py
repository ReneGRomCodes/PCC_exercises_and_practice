# Exercise 4-1 Pizzas: Store the names of at least 3 kinds of pizza in a list and then use a 'for' loop to print the
# name of each pizza.
# Modify your loop to print a sentence that uses the name of the pizza like "I like pepperoni pizza", then add a line at
# end, outside the 'for' loop, that states how much you like pizza.


pizzas = ["pepperoni", "cheese", "veggie", "buffalo chicken"]

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("I like", pizza, "pizza.")

print("I really like pizza a lot!")


# Exercise 4-2 Animals: Store the names of at least 3 animals that have a common characteristic in a list and then use a
# 'for' loop to print the name of each animal.
# Modify your loop to print a sentence that uses the name of the animal like "A dog would make a great pet", then add a
# line at the end, outside the 'for' loop, that states something like 'Any of these animals would make a great pet!'.


animals = ["dog", "cat", "hamster", "shark"]

for animal in animals:
    print(animal)

for animal in animals:
    print("A", animal, "would make a great pet.")

print("All of these animals would make a great pet!")


# Variation including an 'if' statement, considering that sharks don't make for great pets.
for animal in animals:
    if animal == "shark":
        print("A", animal, "would make an excellent pet!!!")
    else:
        print("A", animal, "would make a great pet.")

print("All of these animals would make a great pet!")
