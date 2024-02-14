"""Contains function for Exercises 11-1 and 11-2."""


def city_country(city, country, population=""):
    """Takes parameters 'city', 'country' and optional parameter 'population' and returns a formatted string."""
    if population:
        city_country_s = city.title() + ", " + country.title() + " - population: " + population
        return city_country_s
    else:
        city_country_s = city.title() + ", " + country.title()
        return city_country_s
