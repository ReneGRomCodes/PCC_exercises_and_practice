# Exercise 10-6 Addition: one common problem when prompting for numerical input occurs when people provide text instead
# of numbers. When trying to convert the input to an 'int' you will get a 'ValueError'. Write a program that prompts for
# two numbers, adds them together and prints the result. Catch the 'ValueError' if either input value is not a number
# and print a friendly error message.


n = input("Enter first integer: ")
m = input("Enter second integer: ")

try:
    print(int(n) + int(m))
except ValueError:
    print("Friendly message that you you are supposed to enter integers.")


# Exercise 10-7 Addition Calculator: Wrap your code from Exercise 10-6 in a 'while' loop so the user can continue
# entering numbers even if they make a mistake and enter text instead of a number.


while True:
    n = input("Enter first integer or 'q' to exit: ")
    if n == "q":
        break
    m = input("Enter second integer or 'q' to exit: ")
    if m == "q":
        break

    try:
        print(int(n) + int(m))
    except ValueError:
        print("Friendly message that you you are supposed to enter two integers.")


# Exercise 10-8 Cats and Dogs: Make two files, 'Ch10_cats.txt' and 'Ch10_dogs.txt'. Store at least three names of cats
# and dogs in each file respectively. Write a program that reads these file and prints the contents of the files to the
# screen. Then wrap you code in a 'try-except' block to catch the 'FileNotFound' error and print a friendly message if a
# file is missing.


cats_file = "Ch10_cats.txt"
dogs_file = "Ch10_dogs.txt"

try:
    with open(cats_file, encoding="utf-8") as f_object:
        for line in f_object:
            print(line.title().rstrip())
except FileNotFoundError:
    print("Friendly message that the file is missing.")

try:
    with open(dogs_file, encoding="utf-8") as f_object:
        for line in f_object:
            print(line.title().rstrip())
except FileNotFoundError:
    print("Friendly message that the file is missing.")


# Exercise 10-9 Silent Cats and Dogs: Modify your 'except' block from Exercise 10-8 to fail silently if either file is
# missing.


try:
    with open(cats_file, encoding="utf-8") as f_object:
        for line in f_object:
            print(line.title().rstrip())
except FileNotFoundError:
    pass

try:
    with open(dogs_file, encoding="utf-8") as f_object:
        for line in f_object:
            print(line.title().rstrip())
except FileNotFoundError:
    pass


# Exercise 10-10 Common Words: Visit Project Gutenberg (http://gutenberg.org/) and find a few texts you'd like to
# analyze and download the text files for these works.
# You can use the 'count()' method to find out how many times a word or phrase appears in a string. Write a program that
# reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text.


beowulf = "Ch10_beowulf.txt"
faustus = "Ch10_faustus.txt"
moby_dick = "Ch10_moby_dick.txt"


with open(beowulf, encoding="utf-8") as f_object:
    file = f_object.read()
    print(file.lower().count("the"))

with open(faustus, encoding="utf-8") as f_object:
    file = f_object.read()
    print(file.lower().count("the"))

with open(moby_dick, encoding="utf-8") as f_object:
    file = f_object.read()
    print(file.lower().count("the"))


# Variant checking the files for a word prompted from user:
word = input("What word would you like to count in 'Beowulf', 'the Tragedy of Doctory Faustus' and 'Moby Dick'? ")

with open(beowulf, encoding="utf-8") as f_object:
    file = f_object.read()
    print("The word '" + word + "' appears", file.lower().count(word.lower()), "times in Beowulf")

with open(faustus, encoding="utf-8") as f_object:
    file = f_object.read()
    print("The word '" + word + "' appears", file.lower().count(word.lower()), "the Tragedy of Doctor Faustus")

with open(moby_dick, encoding="utf-8") as f_object:
    file = f_object.read()
    print("The word '" + word + "' appears", file.lower().count(word.lower()), "Moby Dick")
