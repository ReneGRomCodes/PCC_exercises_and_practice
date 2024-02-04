# Exercise 3-4 Guest List: Make a list that includes 3 people you'd like to invite to diner, then use your list to print
# a message to each person, inviting them to dinner.


guests = ["eric", "terry", "john"]
message = ", I would like to invite you to dinner."

print("Hello", guests[0].title() + message)
print("Hello", guests[1].title() + message)
print("Hello", guests[2].title() + message)


# Alternative using a 'for' loop:
for guest in guests:
    print("Hello", guest.title() + message)


# Exercise 3-5 Changing Guest List: One of your guests can't make the dinner, so you need to send out a new set of
# invitations and think of someone else to invite.
# Print a message stating who can't make it, modify the list to replace the name with the new person you are inviting,
# then send out a new set of invitations.


print(guests[1].title(), "can't make it to our dinner.")
guests[1] = "graham"

print("Hello", guests[0].title() + message)
print("Hello", guests[1].title() + message)
print("Hello", guests[2].title() + message)


# Alternative using a 'for' loop:
for guest in guests:
    print("Hello", guest.title() + message)


# Exercise 3-6 More Guests: You found a bigger dinner table. Think of three more guests to invite. Add a print statement
# to inform people that you have found a bigger dinner table.
# Use the 'insert()' method to add one new guest to the beginning and one to the middle of the list, the 'append()'
# method to add a new guest to the end of the list. Then send out a new set of invitation messages.


print("I have found a bigger dinner table.")
guests.insert(0, "terry")
guests.insert(1, "monty")
guests.append("arthur")

print("Hello", guests[0].title() + message)
print("Hello", guests[1].title() + message)
print("Hello", guests[2].title() + message)
print("Hello", guests[3].title() + message)
print("Hello", guests[4].title() + message)
print("Hello", guests[5].title() + message)


# Alternative using a 'for' loop:
for guest in guests:
    print("Hello", guest.title() + message)


# Exercise 3-7 Shrinking Guest List: Your table won't arrive in time, and you have space for only two guest. Print a
# message that you can only invite two people for dinner.
# Use 'pop()' to remove guests from your list one at a time until only two names remain in your list. Each time print
# a message to that person letting them know you're sorry you can't invite them to dinner. Then print a message to the
# two people still on your list, letting them know they're still invited.
# Use 'del' to remove the last two names from the list. Print the list to make sure that it is empty.


print("The big table won't arrive in time, so i can only invite two people.")

print("Hello", guests.pop().title() + ", I am sorry, but I can't invite you to dinner.")
print("Hello", guests.pop().title() + ", I am sorry, but I can't invite you to dinner.")
print("Hello", guests.pop().title() + ", I am sorry, but I can't invite you to dinner.")
print("Hello", guests.pop().title() + ", I am sorry, but I can't invite you to dinner.")

del guests[:]
print(guests)


# Alternative solution:
guests = ["eric", "terry", "john", "graham", "monty", "arthur"]  # Recreating the necessary list.
n = len(guests) - 2  # Establishing the number of people that can't be invited.

print("The big table won't arrive in time, so i can only invite two people.")

for i in range(n):
    print("Hello", guests.pop().title() + ", I am sorry, but I can't invite you to dinner.")

del guests[:]
print(guests)
