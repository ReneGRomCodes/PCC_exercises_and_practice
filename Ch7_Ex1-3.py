# Exercise 7-1 Rental Car: Prompt the user what kind of rental car they would like and print a message, such as "Let me
# see if I can find you a Subaru.".


prompt = "What car would you like? "
message = "Let me see if I can find you a"
vowels = ["a", "e", "i", "o", "u"]

car = input(prompt)

if car[0].lower() in vowels:  # Special case to account for grammar.
    print(message + "n", car.title())
else:
    print(message, car.title())


# Exercise 7-2 Restaurant Seating: Prompt the user about the number of people in their dinner group. If the answer is
# more than eight, print a message saying they'll have to wait for a table. Otherwise, report that their table is ready.


prompt = "How many people are in your dinner group? "
message_wait = "I am sorry, but you'll have to wait for a table."
message_ready = "Your table is ready."

group = int(input(prompt))
if group > 8:
    print(message_wait)
else:
    print(message_ready)


# Exercise 7-3 Multiples of Ten: Ask the user for a number and report whether the number is a multiple of 10 or not.


prompt = "Enter a number to check for multiple on ten: "
multiple = "is a multiple of ten."
not_multiple = "is not a multiple of ten."


n = int(input(prompt))

if n % 10 == 0:
    print(n, multiple)
else:
    print(n, not_multiple)
