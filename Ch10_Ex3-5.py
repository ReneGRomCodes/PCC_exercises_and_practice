# Exercise 10-3 Guest: Write a program that prompts the user for their name. When they respond, write their name to a
# file called 'Ch10_guest.txt'.


filename = "Ch10_guest.txt"

with open(filename, "w") as f_object:
    user_name = input("Please enter you name: ")
    f_object.write(user_name.lower())


# Exercise 10-4 Guest Book: Write a 'while' loop that prompts users for their name. When they enter their name, print a
# greeting to the screen and add a line recording their visit in a file called 'Ch10_guest_book.txt'. Make sure each
# entry appears on a new line in the file.


filename = "Ch10_guest_book.txt"

with open(filename, "a") as f_object:
    while True:
        user_name = input("Please enter you name or press 'enter' to exit: ")

        if user_name == "":
            break
        else:
            print("Hello", user_name.title() + "!")
            f_object.write(user_name.lower() + "\n")
            continue


# Exercise 10-5 Programming Poll: Write a 'while' loop that asks people why they like programming. Each time someone
# enters a reason, add their reason to a file 'Ch10_programming_poll.txt' that stores all the responses.


filename = "Ch10_programming_poll.txt"

with open(filename, "a") as f_object:
    while True:
        poll_answer = input("Why do you like programming (press 'enter' to exit)? ")

        if poll_answer == "":
            break
        else:
            f_object.write(poll_answer + "\n")
            continue
