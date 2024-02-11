"""Collection of functions used for exercises in chapter 9."""
from Ch9_modules_1 import Users


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