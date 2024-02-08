# Exercise 7-8 Deli: Make a list called 'sandwich_orders', fill it with the names of various sandwiches and  make
# another list called 'finished_sandwiches'. Then loop through the list of sandwich orders and print a message for each
# order, such as "I made your tuna sandwich.". As each sandwich is made, move it to the list of finished sandwiches,
# then print a message listing each sandwich.


sandwich_orders = ["club", "reuben", "turkey", "tuna", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I made your", sandwich, "sandwich.")


# Exercise 7-9 No Pastrami: Using the list 'sandwich_orders' from Exercise 7-8 and make sure the sandwich 'pastrami'
# appears at least three times in the list. Add code near the beginning of your program, printing a message that the
# deli has run out of pastrami and use a 'while' loop to remove all occurrences of 'pastrami' from 'sandwich_orders'.
# Make sure no pastrami sandwiches end up in 'finished_sandwiches'.


sandwich_orders = ["club", "pastrami", "reuben", "pastrami", "turkey", "tuna", "veggie", "pastrami"]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print("I made your", sandwich, "sandwich.")

print(finished_sandwiches)


# Exercise 7-10 Dream Vacation: Write a program polling users for their dream vacation using a prompt similar to "If you
# could visit one place in the world, where would you go?". Include a block of code that prints the result of the poll.


prompt_1 = "Please enter name: "
prompt_2 = "If you could visit one place in the world, where would you go? "
prompt_3 = "Do you want to add another person to the poll? (y/n) "

dream_vacation = {}

while True:
    name = input(prompt_1)
    location = input(prompt_2)
    dream_vacation[name.lower()] = location.lower()

    proceed = input(prompt_3)
    if proceed == "y":
        continue
    elif proceed == "n":
        break

for k, v in dream_vacation.items():
    print(k.title() + "'s favorite place is", v.title())
