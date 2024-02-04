# Exercise 3-8 Seeing the World: Think of at least five places in the world you'd like to visit and store the locations
# in a list. Make sure the list is not in alphabetical order and print it in its original order as a raw Python list.
# Use 'sorted()' to print your list in alphabetical order without modifying the actual list, then print the list again
# to show that it is still in its original form.
# Use 'sorted()' to print the list in reverse alphabetical order without changing the original list and then print the
# original list again.
# Use 'reverse()' to change the order of your list and print it, then use 'reverse()' again to revert it back to its
# original order.
# User 'sort()' to change your to alphabetical order, print it, then use 'sort()' again to change it to reverse
# alphabetical order and print it again.


places = ["tokyo", "tanegashima", "reykjavik", "nuuk", "torshavn"]

print(places)  # Printing as raw python list.
print(sorted(places))  # Printing in alphabetical order without changing the actual list.
print(places)  # Printing the list again to show that it's still in its original form.

print(sorted(places, reverse=True))  # Printing list in reverse alphabetical order without changing the original list.
print(places)  # Printing the list again to show that it's still in its original form.

places.reverse()  # Reversing the list.
print(places)
places.reverse()  # Reversing back to original order.
print(places)

places.sort()  # Sorting the list in alphabetical order.
print(places)
places.sort(reverse=True)  # Sorting the list in reverse alphabetical order.
print(places)


# Exercise 3-9 Dinner Guests: Working with one of the programs from Exercise 3-4 through 3-7, use 'len()' to print a
# message indicating the number of people you are inviting to diner.


guests = ["eric", "terry", "john"]

print(len(guests), "people are invited to dinner.")

print("I have found a bigger dinner table.")
guests.insert(0, "terry")
guests.insert(1, "monty")
guests.append("arthur")

print(len(guests), "people are invited to dinner.")


# Exercise 3-10 Every Function: Write a list containing items you thought of like mountains, rivers, countries, etc. and
# use each function introduced in this chapter at least once.


languages = ["english", "german", "french", "italian"]

# Functions to change, add or remove items:
print(languages[-1].title())
languages[2] = "spanish"
languages.append("french")
languages.insert(0, "dutch")
del languages[3]
popped_language = languages.pop()
print(popped_language.title())
languages.remove("dutch")

# Functions to organize lists:
print(sorted(languages))
print(sorted(languages, reverse=True))
languages.sort()
languages.sort(reverse=True)
print(len(languages))
