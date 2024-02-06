# Exercise 5-8 Hello Admin: Make a list of five usernames, including the name 'admin'. Write code that will loop through
# the list and print a greeting to each user . If the username is 'admin' print a special greeting, such as "Hello
# admin, would you like to see a status report?", otherwise print a greeting, such as "Hello Eric, thank you for logging
# in again.".


usernames = ["admin", "eric", "john", "michael", "graham", "terry"]

for user in usernames:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello", user + ", thank you for logging in again.")


# Exercise 5-9 No Users: Add an 'if' test to the previous program to make sure the list of users is not empty. If the
# list is empty print the message "We need to find some users!". Use an empty list to make sure the correct message is
# printed.


usernames = []

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello", user + ", thank you for logging in again.")
else:
    print("We need to find some users!")


# Exercise 5-10 Checking Usernames: Do the following to create a program that simulates how websites ensure that
# everyone has a unique username:
# - Make a list of five usernames called 'current_users'.
# - Make another list of five usernames called 'new_users'. Make sure one or two of the new usernames are also in the
#   'current_users' list.
# - Loop through the 'new_users' list to see if any new username has already been used. If it has, print message that
#   the person will need to enter a new username, if not print a message saying that the username is available.
# - Make sure your comparison is case-insensitive.


current_users = ["admin", "eric", "john", "michael", "graham", "terry"]
new_users = ["king arthur", "eric", "brian", "john", "lumberjack"]

for user in new_users:
    if user.lower() in current_users:
        print("'" + user + "'", "is already in use. Choose another username.")
    else:
        print("The username", user, "is available.")


# Variant prompting the user to input a new username if given username is already in use and adds new username to list
# 'current_users', as well as names from list 'new_users' that are not in use:
current_users = ["admin", "eric", "john", "michael", "graham", "terry"]
new_users = ["king arthur", "eric", "brian", "john", "lumberjack"]

for user in new_users:
    if user.lower() in current_users:
        print("'" + user + "'", "is already in use. Choose another username.")
        new_username = input("Enter new username: ")

        while new_username.lower() in current_users:
            print("'" + new_username + "'", "is already in use. Choose another username.")
            new_username = input("Enter new username: ")

        print("The username", new_username, "is available.")
        current_users.append(new_username.lower())

    else:
        print("The username", user, "is available.")


# Exercise 5-11 Ordinal Numbers: Most ordinal numbers end in 'th', except 1, 2 and 3. Store the numbers 1 through 9 in a
# list. Then loop through the list using an 'if-elif-else' chain to print the proper ordinal ending for each number.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in numbers:
    if n == 1:
        print(str(n) + "st")
    elif n == 2:
        print(str(n) + "nd")
    elif n == 3:
        print(str(n) + "rd")
    else:
        print(str(n) + "th")


# Variant using string slicing to expand the programs capabilities beyond 9:
numbers = list(range(1, 26))

for n in numbers:
    n_s = str(n)
    if n_s[-2:] == "11":
        print(str(n) + "th")
    elif n_s[-2:] == "12":
        print(str(n) + "th")
    elif n_s[-2:] == "13":
        print(str(n) + "th")
    elif n_s[-1] == "1":
        print(str(n) + "st")
    elif n_s[-1] == "2":
        print(str(n) + "nd")
    elif n_s[-1] == "3":
        print(str(n) + "rd")
    else:
        print(str(n) + "th")
