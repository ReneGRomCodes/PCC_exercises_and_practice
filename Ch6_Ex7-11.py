# Exercise 6-7 People: Start with the program from Exercise 6-1. Make two new dictionaries representing different,
# people, store all three dictionaries in a list called 'people' and loop through the list of people, printing
# everything you know about each person.


person_1 = {"first_name": "john", "last_name": "cleese", "age": 84, "city": "santa barbara"}
person_2 = {"first_name": "eric", "last_name": "idle", "age": 80, "city": "los angeles"}
person_3 = {"first_name": "terry", "last_name": "gilliam", "age": 83, "city": "los angeles"}
people = [person_1, person_2, person_3]

for person in people:
    print("\nName:", person["first_name"].title(), person["last_name"].title())
    print("Age:", person["age"])
    print("City:", person["city"].title())


# Exercise 6-8 Pets: Create several dictionaries, with each dictionary's name being the name of a pet. Include the kind
# of animal and the owner's name. Store these dictionaries in a list called 'pets', then loop through your list,
# printing everything you know about each pet.


fluffy = {"type": "cat", "owner": "samantha"}
rocky = {"type": "dog", "owner": "mark"}
nibbles = {"type": "hamster", "owner": "emily"}
squiggles = {"type": "parrot", "owner": "alex"}
pets = [fluffy, rocky, nibbles, squiggles]

for pet in pets:
    print("\nPet information:")
    for k, v in pet.items():
        print("\t", k.title() + ":", v.title())


# Exercise 6-9 Favorite Places: Make a dictionary called 'favorite_places', add three names to use as keys and store
# between one and three favorite places for each person. Print each person's name and their favorite places.


favorite_places = {
    "eleanor": ["paris, france", "kyoto, japan", "santorini, greece"],
    "declan": ["dublin, ireland", "queenstown, new zealand"],
    "aria": ["venice, italy"],
    }

for k, v in favorite_places.items():
    if len(v) == 1:  # Special case to account for grammar if only one favorite place is given.
        print("\n" + k.title() + "'s favorite place is:")
        print("\t", v[0].title())
    else:
        print("\n" + k.title() + "'s favorite places are:")
        for place in v:
            print("\t", place.title())


# Exercise 6-10 Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite
# number and print each person's name and favorite number.


favorite_numbers = {
    "jasmine": [4, 25, 40],
    "ethan": [9, 18],
    "maya": [2],
    "sebastian": [42, 21, 3],
    "lily": [1],
    }

for k, v in favorite_numbers.items():
    if len(v) == 1:  # Special case to account for grammar if only one favorite number is given.
        print("\n" + k.title() + "'s favorite number is:")
        print(v[0])
    else:
        print("\n" + k.title() + "'s favorite numbers are:")
        for number in v:
            print(number)


# Exercise 6-11 Cities: Create a dictionary called 'cities' and use the name of three cities as keys in your dictionary.
# Then make a dictionary for each city, containing information such as country, population and one fact about the city.
# Print the name of each city and all the information you have stored about them.


cities = {
    "tokyo": {
        "country": "japan",
        "population": "14 million",
        "fact": "Tokyo is known for its efficient public transportation system, including the famous Shinkansen bullet"
        "trains.",
    },
    "paris": {
        "country": "france",
        "population": "2.2 million",
        "fact": "Paris is home to the iconic Eiffel Tower, which was completed in 1889 as the centerpiece of the 1889"
        "World's Fair.",
    },
    "sydney": {
        "country": "australia",
        "population": "5.3 million",
        "fact": "Sydney is home to the Sydney Opera House, one of the most famous and distinctive buildings in the"
                "world, renowned for its unique architecture and stunning waterfront location.",
    },
}


for city, info in cities.items():
    print("\n" + city.title().upper() + ":")
    for k, v in info.items():
        if k == "country":  # Special case to print only the country in titlecase in the following line.
            print("\t" + k.title() + ":", v.title())
        else:
            print("\t" + k.title() + ":", v)
