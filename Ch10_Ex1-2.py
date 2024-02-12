# Exercise 10-1 Learning Python: Write a few lines summarizing what you have learning in Python so far into a new txt
# file ('Ch10_learning_python.txt'). Write a program that reads the file and prints what you wrote three times. Print
# the contents once by reading the entire file, once by looping over it and once by storing the lines in a list and then
# working with them outside the 'with' block.


with open("Ch10_learning_python.txt") as f_object:  # Reading entire file.
    learning_python = f_object.read()
    print(learning_python)


with open("Ch10_learning_python.txt") as f_object:  # Looping over file.
    for line in f_object:
        print(line.rstrip())


with open("Ch10_learning_python.txt") as f_object:  # Storing file in list.
    learning_python = f_object.readlines()

for line in learning_python:  # Working with list outside the 'with' block.
    print(line.rstrip())


# Exercise 10-2 Learning C: Use the 'replace()' method to replace any word in a string with a different word.
# Read each line from the file you just created and replace the word 'Python' with the name of another language such as
# 'C'. Print each modified line to the screen.


with open("Ch10_learning_python.txt") as f_object:
    learning_python = f_object.readlines()
    for line in learning_python:
        c_line = line.replace("Python", "C")
        print(c_line.rstrip())
