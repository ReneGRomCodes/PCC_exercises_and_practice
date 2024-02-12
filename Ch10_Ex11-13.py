# Exercise 10-11 Favorite Number: Write a program that prompts for the user's favorite number. Use 'json.dump()' to
# store this number in a file ('Ch10_favorite_number.txt'), then write a separate program that reads in this value and
# prints the message "I know your favorite number! It's ___ .".


import json

filename = "Ch10_favorite_number.txt"

with open(filename, "w") as f_object:
    n = input("What is your favorite number? ")
    json.dump(n, f_object)

with open(filename) as f_object:
    m = json.load(f_object)
    print("I know your favorite number! It's", m + ".")


# Exercise 10-12 Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number
# is already stored, report the favorite number to the user. If not, prompt for the user's favorite number and store it
# in a file.


try:
    with open(filename) as f_object:
        m = json.load(f_object)
except:
    with open(filename, "w") as f_object:
        n = input("What is your favorite number? ")
        json.dump(n, f_object)
else:
    print("I know your favorite number! It's", m + ".")


# Exercise 10-13 Verify User: The final listing for 'remember_me.py' assumes either that the user has already entered
# their username or that the program is running for the first time. Modify it in case the current user is not the person
# last used the program.
# Before printing a welcome back message in 'greet_user()', ask the user if this is the correct username. If it is not,
# call 'get_new_username()' to get the correct username.
