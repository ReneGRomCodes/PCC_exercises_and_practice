# Exercise 10-11 Favorite Number: Write a program that prompts for the user's favorite number. Use 'json.dump()' to
# store this number in a file ('Ch10_favorite_number.txt'), then write a separate program that reads in this value and
# prints the message "I know your favorite number! It's ___ .".


import json

filename = "Ch10_favorite_number.json"

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


def get_stored_username():
    """Gets stored username if available."""
    filename = "Ch10_username.json"
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompts for a new username."""
    username = input("What is your name? ")
    filename = "Ch10_username.json"
    with open(filename, "w") as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greets the user by name."""
    username = get_stored_username()

    if username:
        check_user = input("Is " + username + " your username? (y/n) ")
        if check_user.lower() == "y":
            print("Welcome back,", username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back,", username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back,", username + "!")


greet_user()
