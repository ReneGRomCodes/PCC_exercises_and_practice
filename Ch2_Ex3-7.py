# Exercise 2-3 Personal Message: Store a person's name in a variable and print a message to that person.


person = "Monty"
print("Hello", person + ", would you like to learn some Python today?")


# Exercise 2-4 Name Cases: Store a person's name in a variable and print that person's name in lowercase, uppercase
# and titlecase.


person = "eric"
print(person.lower())
print(person.upper())
print(person.title())


# Exercise 2-5 Famous Quote: Find a quote from a famous person, print the quote and the name of its author.


print('Albert Einstein once said: "A person who never made a mistake, never tried anything new."')


# Exercise 2-6 Famous Quote 2: Repeat exercise 2-5, but this time store the name in a variable, compose your message
# and store it in a variable called 'message'. Print your message.


quote = "A person who never made a mistake, never tried anything new"
person = "albert einstein"
message = person.title() + ' once said: "' + quote + '."'
print(message)


# Exercise 2-7: Stripping Names: Store a person's name and include some whitespace characters at the beginning and the
# end of the name. Make sure you use '\t' and '\n' at least once.
# Print the name once, so the whitespace around the name is displayed, then print the name using of the three stripping
# functions.


name = "\n\t   monty  "

print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
