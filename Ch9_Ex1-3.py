# Exercise 9-1 Restaurant: Create a class called 'Restaurant'. The '__init__()' method for 'Restaurant' should store two
# attributes: a 'restaurant_name' and a 'cuisine_type'. Make a method called 'describe_restaurant()' that prints these
# two pieces of information and a method called 'open_restaurant' that prints a message indicating that the restaurant
# is open. Create an instance called 'restaurant' from your class, print the two attributes individually and then call
# both methods.


class Restaurant():
    """Represents a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints 'restaurant_name' and 'cuisine_type'."""
        print(self.restaurant_name.title(), "presents it's guests with the finest", self.cuisine_type, "cuisine.")

    def open_restaurant(self):
        """Prints message stating that restaurant is open."""
        print(self.restaurant_name, "is open!")


restaurant = Restaurant("kitsune udonya", "japanese udon")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


# Exercise 9-2 Three Restaurants: Starting with you class from Exercise 9-1, create three different instances from the
# class and call 'describe_restaurant()' for each instance.


golden_dragon = Restaurant("golden dragon", "chinese")
taj_mahal = Restaurant("taj mahal", "indian")
le_petit_bistro = Restaurant("le petit bistro", "french")

golden_dragon.describe_restaurant()
taj_mahal.describe_restaurant()
le_petit_bistro.describe_restaurant()


# Exercise 9-3 Users: Create a class called 'Users' with two attributes called 'first_name' and 'last_name' and then add
# several other attributes that are typically stored in a user profile. Make a method called 'describe_user()' that
# prints a summary of the users information and another method called 'greet_user()' that prints a personalized greeting
# to each user.
# Create several instances representing different users and call both methods for each.


class Users():
    """Represents a user."""

    def __init__(self, first_name, last_name, username, password):
        """Initiates attributes for names and password."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.full_name = first_name + " " + last_name

    def describe_user(self):
        """Prints user information in a neat format."""
        print("\n", self.full_name.title() + ":")
        print("\tUsername:", self.username)
        print("\tPassword:", self.password)

    def greet_user(self):
        """Prints personalized greeting to user."""
        print("\nWelcome back,", self.username)


user_1 = Users("ava", "johnson", "SkySurfer23", "stellarpulse76")
user_2 = Users("ethan", "ramirez", "QuantumCoder77", "crimsoncascade28")
user_3 = Users("maya", "patel", "StarSeeker42", "sapphirewhisper49")
user_4 = Users("oliver", "thompson", "EchoEngineer99", "thunderforge12")

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_4.describe_user()
user_4.greet_user()
