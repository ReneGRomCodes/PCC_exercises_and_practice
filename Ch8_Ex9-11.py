# Exercise 8-9 Magicians: Make a list of magician's names and pass the list to a function called 'show_magicians()',
# which prints the name of each magician in the list.


magicians = ["david copperfield", "penn & teller", "derren brown", "lance burton"]


def show_magicians(names_list):
    """Takes list 'names_list' and prints each item from that list."""
    for name in names_list:
        print(name.title())


show_magicians(magicians)


# Exercise 8-10 Great Magicians: Starting with your program from Exercise 8-9, create a function called 'make_great()'
# that modifies the list of magicians by adding the phrase "the Great" to each magician's name. Call it to see that the
# list has actually been modified.


def make_great(names_list):
    """Adds phrase 'the great' to each name in list 'names_list'."""
    the_greats = []
    for name in names_list:
        the_greats.append("the great " + name)

    magicians[:] = the_greats


make_great(magicians)
print(magicians)


# Exercise 8-11 Unchanged Magicians: Start with your work from Exercise 8-10. Call 'make_great()' with a copy of the
# list of magicians' names. Because the original list will be unchanged, return the new list and store it in a separate
# list. Call 'show_magicians()' with each list to show that you have on original list and one with 'the Great' added to
# each name.


magicians = ["david copperfield", "penn & teller", "derren brown", "lance burton"]
the_greats = []


def make_great(names_list, the_great_list):
    """Adds phrase 'the great' to each name in list 'names_list', adds them to 'the_great_list' and returns the
    latter."""
    for name in names_list:
        the_great_list.append("the great " + name)

    return the_great_list


make_great(magicians, the_greats)
show_magicians(magicians)
show_magicians(the_greats)
