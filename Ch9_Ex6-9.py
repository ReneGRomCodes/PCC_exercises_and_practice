# Exercise 9-6 Ice Cream Stand: An ice cream stand is a specific kind of restaurant . Write a class called 'IceCreamStand'
# that inherits from the 'Restaurant' class form Exercise 9-1 or 9-4. Add an attribute called 'flavors' that stores a
# list of ice cream flavors and write a method that displays these flavors. Create an instance called 'IceCreamStand'
# and call this method.


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


class IceCreamStand(Restaurant):
    """Represents aspects of restaurants, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes attributes from parent class."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def show_flavors(self):
        """Prints 'self.flavors' in neat format."""
        print("Following flavors are available:")
        for flavor in self.flavors:
            print("\t", flavor)


icecreamstand = IceCreamStand("scoops & smiles", "ice cream")
icecreamstand.show_flavors()


# Exercise 9-7 Admin: An Admin is a special kind of user. Write a class called 'Admin' that inherits from the 'User'
# class from Exercise 9-3 or 9-5. Add an attribute 'privilege' that stores a list of strings like "can add post", "can
# delete post" and "can ban user". Write a method called 'show_privileges()' that lists the privileges, create an
# instance of 'Admin' and call your method.


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


class Admin(Users):
    """Represents aspects of users specific to admins."""

    def __init__(self, first_name, last_name, username, password):
        """Initializes attributes from parent class."""
        super().__init__(first_name, last_name, username, password)
        self.privileges = ["can add posts", "can delete posts", "can ban users"]

    def show_privileges(self):
        """Prints formatted list of admins privileges."""
        print("The admin has the following privileges:")
        for privilege in self.privileges:
            print("\t", privilege)


admin = Admin("ava", "johnson", "SkySurfer23", "stellarpulse76")
admin.show_privileges()


# Exercise 9-8 Privileges: Write a separate 'Privileges' class that should have one attribute 'privileges', which stores
# strings as describe in Exercise 9-7. Move the 'show_privileges()' method to this class and make a 'Privileges'
# instance as an attribute in the 'Admin' class, then create a new instance of 'Admin' and use your method to show its
# privileges.


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


admin = Admin("ethan", "ramirez", "QuantumCoder77", "crimsoncascade28")
admin.privileges.show_privileges()


# Exercise 9-9 Battery Upgrade: Use the final version of 'electric_car.py' from this section and add a method to the
# 'Battery' class called 'upgrade_battery()'. This method should check the battery size and set the capacity to 85 if it
# isn't already. Make an electric car with a default battery size, call 'get_range()' before and after upgrading the
# battery.


# Streamlined classes from 'electric_car.py':
class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class ElectricCar(Car):
    """Represents aspects of a car specific to electric cars."""

    def __init__(self, make, model, year):
        """Initializes attributes of parent class and attributes specific to electric cars."""
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initializes the battery's attributes."""
        self.battery_size = battery_size

    def get_range(self):
        """Prints statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrades battery to the largest size."""
        self.battery_size = 85


car = ElectricCar("tesla", "model s", 2016)

car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()
