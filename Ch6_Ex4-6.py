# Exercise 6-4 Glossary 2: Clean up the code from Exercise 6-3 by replacing your series of 'print' statements with a
# loop that runs through the dictionary, then add five more words and meanings to your glossary.


glossary = {
    "list": "Ordered collections of items, allowing for easy storage and manipulation of multiple values",
    "dictionaries": "Key-value pairs that allow for efficient storage and retrieval of data based on unique identifiers"
                    "(keys)",
    "variables": "Containers for storing data values that can be referenced and manipulated throughout a program",
    "strings": "Sequences of characters enclosed within quotation marks, used to represent textual data",
    "if-statements": "Conditional statements that allow for branching in code execution based on the evaluation of a"
                     "specified condition",
    }

for k, v in glossary.items():
    print("\n", k.title() + ":")
    print("\t", v)


key = "comments"
value = "Non-executable text used to annotate code, providing explanations and context for humans reading the code"
glossary[key.lower()] = value

key = "index"
value = "Positional reference within a data structure, such as a list or string, indicating the location of an item"
glossary[key.lower()] = value

key = "loops"
value = "Control structures that repeatedly execute a block of code as long as a specified condition is true"
glossary[key.lower()] = value

key = "slice"
value = "Subsets of a sequence (e.g., list, string) extracted by specifying a start and end index"
glossary[key.lower()] = value

key = "keys"
value = "Unique identifiers used in dictionaries to access and retrieve associated values"
glossary[key.lower()] = value


# Exercise 6-5 Rivers: Create a dictionary containing three major rivers and the country they are in. Use a loop to
# print a sentence about each river (example: "The Nile runs through Egypt."), one loop to print the name of each river
# and one loop to print the name of each country included in the dictionary.


rivers = {"amazon": "brazil", "nile": "egypt", "yangtze": "china"}
message = "river runs through"

for k, v in rivers.items():
    print("The", k.title(), message, v.title() + ".")


# Exercise 6-6 Polling: Use the code in 'favorite_languages.py'. Create a list of people who should take the poll and
# include names that are already in the dictionary and some that are not. Then loop through the list, checking if they
# already have taken the poll. If they did, print a message thanking them for responding and if they have not yet taken
# the poll, print a message inviting them to take the poll.


favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

people = ["jen", "john", "edward", "phil", "eric"]

for name in people:
    if name in favorite_languages:
        print("Thank you,", name.title() + ", for participating in the poll.")
    else:
        print("Come on,", name.title() + ", take the poll!")


# Variant prompting the user to take the poll and adds their name and answers to the dictionary if they agree:
prompt_1 = "Do you want to participate in the poll, "
prompt_2 = "Please enter your favorite programming language, "

for name in people:
    if name in favorite_languages:
        print("Thank you,", name.title() + ", for participating in the poll.")
    else:
        partake = input(prompt_1 + name.title() + "? (y/n) ")

        if partake == "y":
            v = input(prompt_2 + name.title() + ": ")
            favorite_languages[name.lower()] = v.lower()
            continue
        else:
            continue
