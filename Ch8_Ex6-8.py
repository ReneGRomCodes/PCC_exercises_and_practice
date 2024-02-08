# Exercise 8-6 Names: Write a function called 'city_country()' that takes in the name of a city and its country. It
# should return a string formatted like "Santiago, Chile". Call your function with at least three city-country pairs and
# print the returned value.


def city_country(city, country):
    """Takes variables 'city' and 'country' and returns formatted string."""
    city_country_string = city.title() + ", " + country.title()
    return city_country_string


print(city_country("tokyo", "japan"))
print(city_country("paris", "france"))
print(city_country("rome", "italy"))


# Exercise 8-7 Album: Write a function called 'make_album()' that builds a dictionary describing a music album. It
# should take in an artist name and album title, then return a dictionary containing these two pieces of information.
# Use the function to create three dictionaries and print each return value to show that you have stored the information
# correctly.
# Add an optional parameter to you function that allows you to store the number of tracks and call your new function at
# least once.


def make_album(artist, title):
    """Takes variables 'artist' and 'title' and returns a dictionary."""
    album = {"artist": artist, "title": title}
    return album


album_1 = make_album("symphony x", "paradise lost")
album_2 = make_album("dream theater", "images and words")
album_3 = make_album("operation mindcrime", "queensryche")

print(album_1)
print(album_2)
print(album_3)


def make_album(artist, title, number_tracks=""):
    """Takes variables 'artist', 'title' and 'number_tracks' and returns a dictionary. 'number_tracks' being
    optional."""
    if number_tracks:
        album = {"artist": artist, "title": title, "number_tracks": int(number_tracks)}
    else:
        album = {"artist": artist, "title": title}

    return album


album_4 = make_album("divine wings of tragedy", "symphony x")
album_5 = make_album("still life", "opeth", "7")

print(album_4)
print(album_5)


# Exercise 8-8 User Albums: Start with your program from Exercise 8-7. Write a 'while' loop that allows users to enter
# an album's artist and title and print the created dictionary. Be sure to include a 'quit' value in the while loop.


while True:
    artist = input("Enter name of the artist: ")
    title = input("Enter name of the album: ")
    number_tracks = input("Enter number of tracks (press enter to skip): ")

    album = make_album(artist.lower(), title.lower(), number_tracks)
    print(album)

    proceed = input("Do you want to enter another album? (y/n) ")
    if proceed == "y":
        continue
    else:
        break
