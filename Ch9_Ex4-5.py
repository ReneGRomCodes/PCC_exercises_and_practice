# Exercise 9-4 Number Served: Start with your program from Exercise 9-1 and add an attribute called 'number_served' with
# a default value of 0. Create an instance called 'restaurant' from this class, print the number of customers the
# restaurant has served, then change the value and print it again.
# Add a method called 'set_number_served()' that lets you set the number of customers that have been served. Call this
# method with a new number and print the value again.
# Add another method called 'increment_number_served()' that lets you increment the number of customers that have been
# served. Call that method with any number.


class Restaurant():
    """Represents a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints 'restaurant_name' and 'cuisine_type'."""
        print(self.restaurant_name.title(), "presents it's guests with the finest", self.cuisine_type, "cuisine.")

    def open_restaurant(self):
        """Prints message stating that restaurant is open."""
        print(self.restaurant_name, "is open!")

    def set_number_served(self, n):
        """Sets 'number_served' to value 'n'."""
        self.number_served = n

    def increment_number_served(self, n):
        """Raises value of 'number_served' by value 'n'."""
        self.number_served += n


restaurant = Restaurant("kitsune udonya", "japanese udon")

print(restaurant.number_served)
restaurant.set_number_served(50)
print(restaurant.number_served)

restaurant.increment_number_served(50)
print(restaurant.number_served)


# Exercise 9-5 Login Attempts: Add an attribute called 'login_attempts' to your 'User' class from Exercise 9-3 and
# write a method called 'increment_login_attempts()' that increments the value of 'login_attempts' by 1. Write another
# method called 'reset_login_attempts()' that resets the value of login attempts to 0.
# Make an instance of the 'User' class and call 'increment_login_attempts()' several times. Print the value of 'login_
# attempts()' to make sure it was incremented properly and then call 'reset_login_attempts()'. Print 'login_attempts()'
# again to make sure it was reset to 0.


class Users():
    """Represents a user."""

    def __init__(self, first_name, last_name, username, password):
        """Initiates attributes for names and password."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.full_name = first_name + " " + last_name
        self.login_attempts = 0

    def describe_user(self):
        """Prints user information in a neat format."""
        print("\n", self.full_name.title() + ":")
        print("\tUsername:", self.username)
        print("\tPassword:", self.password)

    def greet_user(self):
        """Prints personalized greeting to user."""
        print("\nWelcome back,", self.username)

    def increment_login_attempts(self):
        """Raises value of 'login_attempts' by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset 'login_attempts' to 0."""
        self.login_attempts = 0


user = Users("ava", "johnson", "SkySurfer23", "stellarpulse76")

print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)
