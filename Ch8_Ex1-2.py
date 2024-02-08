# Exercise 8-1 Message: Write a function called 'display_messages' that prints one sentence telling everyone what you
# are learning in this chapter, then call the function.


def display_messages():
    """Prints string about this chapter."""
    print("In this chapter I am learning how to use functions in Python.")


display_messages()


# Exercise 8-2 Favorite Block: Write a function called 'favorite_book' that accepts on parameter, 'title'. The function
# should print a message, such as "One of my favorite books is 'Alice in Wonderland'.". Then call the function.


def favorite_book(title):
    """Prints a message that includes parameter 'title'."""
    message = "One of my favorite books is"
    print(message, title.title())


favorite_book("alice in wonderland")
