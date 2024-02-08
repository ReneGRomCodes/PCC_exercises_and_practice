# Exercise 8-3 T-Shirt: Write a function called 'make_shirt()' that accepts size and text of a message that reads "I
# love Python!", then prints a sentence summarizing the shirt size and message printed on it.
# Call the function once using positional and once using keyword arguments.


def make_shirt(size, text):
    """Takes variables 'text' and 'size' and prints a string including them."""
    print("T-shirt in size", size.upper(), "with '" + text + "' printed on it.")


make_shirt("m", "I love Python!")
make_shirt(size="m", text="I love Python!")


# Exercise 8-4 Large Shirts: Modify 'make_shirt()' so that shirts are large by default with a message that reads "I love
# Python!". Make a large and medium shirt with the default message and a shirt of any size with a different message.


def make_shirt(size="l", text="I love Python!"):
    """Takes variables 'text' and 'size' and prints a string including them. 'l' and 'I love Python' are default
    values for 'size' and 'text'."""
    print("T-shirt in size", size.upper(), "with '" + text + "' printed on it.")


make_shirt()
make_shirt(size="m")
make_shirt(text="Python is alright")
make_shirt(size="m", text="Python is alright")


# Exercise 8-5 Cities: Write a function called 'describe_city()' that accepts the name of a city and its country. It
# should print a simple sentence, such as "Reykjavik is in Iceland". Give the parameter for country a default value and
# call your function for three different cities, at least one of which is not in the default country.


def describe_city(name, country="japan"):
    """Takes variables 'name' and 'country' and prints a string including them. 'japan' is default value for
    'country'."""
    print(name.title(), "is in", country.title() + ".")


describe_city(name="tokyo")
describe_city(name="paris", country="france")
describe_city(name="osaka")
