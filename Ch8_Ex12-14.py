# Exercise 8-12 Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. It should have
# one parameter that collects as many items as the call provides and print a summary of the ordered sandwich. Call the
# function three times, using different arguments each time.


def sandwich(*items):
    """Takes arbitrary number of parameters 'items' and prints them in a neat format."""
    print("Sandwich with the following toppings:")
    for item in items:
        print("\t-", item)


sandwich("mayonnaise", "salami")
sandwich("cheese", "tomatoes", "bacon")
sandwich("avocado")


# Exercise 8-13 User Profile: Start with a copy of 'user_profile.py' from page 153. Build a profile of yourself by
# calling 'build_profile()', using your first and last name and three other key-value pairs that describe you.


# user_profile.py:
def build_profile(first, last, **user_info):
    """Builds a dictionary containing everything we know about a user."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("mr", "sandwich",
                             topping_1="bacon",
                             topping_2="tomato",
                             bread="fluffy bread")


# Exercise 8-14 Cars: Write a function that stores information about a car in a dictionary. It should always receive a
# manufacturer and a model name, then accept an arbitrary number of keyword arguments. Call the function with the
# required information and two other key-value pairs, such as color or optional feature. Then print the dictionary to
# make sure all the information was stored correctly.


def build_car_info(manufacturer, model, **misc):
    """Builds and returns a dictionary about a car containing 'manufacturer', 'model' and arbitrary number of kwargs."""
    car_info = {}
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    for k, v in misc.items():
        car_info[k] = v

    return car_info


car = build_car_info("mazda", "2", year="2016", color="red")
print(car)
