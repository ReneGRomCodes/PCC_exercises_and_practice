# Exercise 3-1 Names: Store a few names in a list called 'names'. Print each person's name by accessing each element in
# the list, one at a time.


names = ["eric", "terry", "john", "graham"]

print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())


# Alternative using a 'for' loop:
for name in names:
    print(name.title())


# Exercise 3-2 Greetings: Start with the list from exercise 3-1, but instead of printing each person's name, print a
# message to them. The text of each message should be the same, but each message should be personalized with the
# person's name.


message = "And now back to you,"

print(message, names[0].title())
print(message, names[1].title())
print(message, names[2].title())
print(message, names[3].title())


# Alternative using a 'for' loop:
for name in names:
    print(message, name.title())


# Exercise 3-3 Your Own List: Store examples of you favorite mode of transportation, such as motorcycles or cars, in a
# list. Use your list to store several statements about these items, such as "I would like to own a Honda motorcycle".


cars = ["mitsubishi evo", "mazda 626", "mazda 2"]

print("My first car was a used", cars[1].title(), "and what a car it was.")
print("Now I am driving a",  cars[2].title() + ", which is pretty nice.")
print("But one day I'll treat myself to a", cars[0].title() + ".")
