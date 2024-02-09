# Exercise 8-15 Printing Models: Put the functions from the example in 'printing_models.py' in a separate file called
# 'Ch_printing_functions.py'. Write an import statement and use the imported functions.


import Ch8_printing_functions


unprinted = ["iphone case", "robot pendant", "dodecahedron"]
completed = []

Ch8_printing_functions.print_models(unprinted, completed)
Ch8_printing_functions.show_completed_models(completed)
