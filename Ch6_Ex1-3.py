# Exercise 6-1 Person: Use a dictionary to store information about a person. Store their first name, last name, age and
# the city in which they live. You should have keys such as 'first_name', 'last_name', 'age' and 'city'. Print each
# piece of information stored in your dictionary.


person = {"first_name": "john", "last_name": "cleese", "age": 84, "city": "santa barbara"}

print(person["first_name"].title(), person["last_name"].title())
print(person["age"])
print(person["city"].title())


# Exercise 6-2 Favorite Number: Use a dictionary to store people's favorite numbers. Choose five names and use them as
# keys, then choose of a favorite number for each person and store them as values. Print each person's name and their
# favorite number.


favorite_numbers = {"jasmine": 4, "ethan": 9, "maya": 2, "sebastian": 42, "lily": 13}
message = "'s favorite number is"

print("Jasmine" + message, favorite_numbers["jasmine"])
print("Ethan" + message, favorite_numbers["ethan"])
print("Maya" + message, favorite_numbers["maya"])
print("Sebastian" + message, favorite_numbers["sebastian"])
print("Lily" + message, favorite_numbers["lily"])


# Variant using user input and loops to poll people for their favorite number and then prints the dictionary. I also
# added exceptions for good measure:
prompt_1 = "Enter name: "
prompt_2 = "Enter favorite number: "
prompt_3 = "Do you want to another person to the poll? (y/n) "

while True:
    try:
        k = input(prompt_1)
        v = input(prompt_2)
        favorite_numbers[k.lower()] = int(v)
    except ValueError:
        break

    proceed = input(prompt_3)
    if proceed == "y":
        continue
    else:
        break

for key, value in favorite_numbers.items():
    print(key.title() + message, value)


# Exercise 6-3 Glossary: Think of five programming words from the previous chapters and store their meaning as values.
# Print each word as a neatly formatted output.


glossary = {
    "list": "Ordered collections of items, allowing for easy storage and manipulation of multiple values",
    "dictionaries": "Key-value pairs that allow for efficient storage and retrieval of data based on unique identifiers"
                    "(keys)",
    "variables": "Containers for storing data values that can be referenced and manipulated throughout a program",
    "strings": "Sequences of characters enclosed within quotation marks, used to represent textual data",
    "if-statements": "Conditional statements that allow for branching in code execution based on the evaluation of a"
                     "specified condition",
    }

word = "list"
print(word.title() + ":")
print("\t", glossary[word], "\n")

word = "dictionaries"
print(word.title() + ":")
print("\t", glossary[word], "\n")

word = "variables"
print(word.title() + ":")
print("\t", glossary[word], "\n")

word = "strings"
print(word.title() + ":")
print("\t", glossary[word], "\n")

word = "if-statements"
print(word.title() + ":")
print("\t", glossary[word], "\n")
