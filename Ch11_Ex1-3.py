import unittest
from Ch11_city_functions import city_country  # Function for Exercises 11-1 and 11-2.


# Exercise 11-1 City, Country: Write a function that accepts two parameters: a city name and a country. the function
# should return a single string of the form "City, Country" such as "Santiago, Chile". Store the function in a module
# called 'Ch11_city_functions.py'.
# Write a method called 'test_city()' to verify that calling your function with values such as 'santiago' and
# 'chile' results in the correct string.
# Exercise 11-2 Population: Modify your function to use a third parameter 'population'. It should now return a string
# like 'Santiago, Chile - population: 500000". Run 'test_city_()' again. Make sure it fails this time.
# Write a second test called 'test_city_population()' and make sure it passes this time.


class TestCityCountry(unittest.TestCase):
    """Tests 'Ch11_city_functions.py"""

    def test_city(self):  # For Exercise 11-1.
        """Tests 'city_country()' function with two parameters."""
        formatted_city = city_country("santiago", "chile")
        self.assertEqual(formatted_city, "Santiago, Chile")

    def test_city_population(self):  # For Exercise 11-2.
        """Tests 'city_country()' function with optional parameter."""
        formatted_city = city_country("santiago", "chile", population="500000")
        self.assertEqual(formatted_city, "Santiago, Chile - population: 500000")


# Exercise 11-3 Employee: Write a class called 'Employee'. the '__init__()' method should take in a first name, last
# name and annual salary and stores each of them as attributes. Write a method called 'give_raise()' that add $5000 to
# the annual salary by default but also accepts a different raise amount.
# Write a test case for 'Employee' with two test methods, 'test_give_default_raise()' and 'test_give_custom_raise()'.
# Use the 'setUp()' method so don't have to create a new employee instance in each test method. Run your test case and
# make sure both tests pass.


class Employee():
    """Represents an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """"Initializes attributes to describe an employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Raises and returns 'annual_salary' by value 'amount'. Default is 5000."""
        self.annual_salary += amount
        return self.annual_salary


class TestEmployee(unittest.TestCase):
    """Tests 'Employee' class."""

    def setUp(self):
        """Creates an employee instance to use in test methods."""
        self.employee = Employee("king", "arthur", 150000)

    def test_give_default_raise(self):
        """Tests 'give_raise()' function with default value for 'amount'."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 155000)

    def test_give_custom_raise(self):
        """Tests 'give_raise()' function with custom value for 'amount'."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 160000)
