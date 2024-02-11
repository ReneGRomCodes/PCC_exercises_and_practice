"""Collection of functions used for exercises in chapter 9."""


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


class Privileges():
    """Represents privileges for admins."""

    def __init__(self):
        """Initializes privileges."""
        self.privileges = ["can add posts", "can delete posts", "can ban users"]

    def show_privileges(self):
        """Prints formatted list of admins privileges."""
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print("\t", privilege)


class Admin(Users):
    """Represents aspects of users specific to admins."""

    def __init__(self, first_name, last_name, username, password):
        """Initializes attributes from parent class."""
        super().__init__(first_name, last_name, username, password)
        self.privileges = Privileges()
