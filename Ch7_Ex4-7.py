# Exercise 7-4 Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter
# 'quit'. Print a message saying you'll add that topping to their pizza after each input.


prompt = "What topping would you like on your pizza? "

topping = input(prompt)

while topping.lower() != "quit":
    print("Adding", topping.lower(), "to your pizza.")
    topping = input(prompt)


# Variant adding the user input to a list and printing the entire list at the end:
message = "Enter toppings or type 'quit' at any point during your order"
prompt = "What topping would you like on your pizza? "
finished_order = "\nFinishing you pizza with the following toppings:"
toppings = []

print(message)
topping = input(prompt)

while topping.lower() != "quit":
    print("Adding", topping.lower(), "to your pizza.\n")
    topping = input(prompt)
    toppings.append(topping)

print(finished_order)
for t in toppings:
    print("\t-", t.lower())


# Exercise 7-5 Movie Tickets: A movie theater charges different prices depending on a person's age. Write a loop
# prompting users for their age and tells them their ticket price:
# - Under the age of 3, the ticket is free.
# - Between 3 and 12, the ticket is $10.
# - Over the age of 12, the ticket is $15.


prompt = "Enter your age or type 'quit' to exit: "
message = "Your ticket is $"
age_1 = 3
age_2 = 12
price_1 = "free"
price_2 = 10
price_3 = 15


while True:
    age = input(prompt)
    if age.lower() == "quit":
        break
    elif int(age) < age_1:
        print(message[:-1] + price_1 + ".")  # Using string slicing to remove the '$' from the 'message' string.
    elif int(age) < age_2:
        print(message + str(price_2) + ".")
    else:
        print(message + str(price_3) + ".")


# Exercise 7-6 Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at
# least once:
# - Conditional test in the 'while' statement to stop the loop.
# - 'active' variable to control how long the loop runs.
# - 'break' statement to exit the loop when user enters 'quit'.


# From Exercise 7-4. Already using conditional test:
prompt = "What topping would you like on your pizza? "

topping = input(prompt)

while topping.lower() != "quit":
    print("Adding", topping.lower(), "to your pizza.")
    topping = input(prompt)


# With 'active' variable:
topping = input(prompt)

active = True
while active:
    if topping.lower() == "quit":
        active = False
    else:
        print("Adding", topping.lower(), "to your pizza.")
        topping = input(prompt)


# Using 'break' statement:
topping = input(prompt)

while True:
    if topping.lower() == "quit":
        break
    else:
        print("Adding", topping.lower(), "to your pizza.")
        topping = input(prompt)
        continue


# Exercise 7-7 Infinity: Write a loop that never ends and run it (press 'ctrl-C' to end the loop).


n = 1
while True:
    if n == 0:
        break
    else:
        n += 1
