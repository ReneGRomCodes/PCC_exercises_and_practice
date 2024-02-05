# Exercise 5-1 Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your
# prediction for the test result. Create at least 10 test and have 5 tests evaluate to 'True' and 5 evaluate to 'False'.


car = "subaru"
car_2 = "Subaru"

print("Is car=='subaru'? I predict True.")
print(car == "subaru")

print("Is car=='audi'? I predict False.")
print(car == "audi")

print("Is car.title()=='Subaru'? I predict True.")
print(car.title() == "Subaru")

print("Is car.upper()=='subaru'? I predict False.")
print(car.upper() == "subaru")

print("Is car.upper()=='SUBARU'? I predict True.")
print(car.upper() == "SUBARU")

print("Is car.upper()=='SuBaRu'? I predict False.")
print(car.upper() == "subaru")

print("Is car.lower()=='subaru'? I predict True.")
print(car.lower() == "subaru")

print("Is car.title()=='subaru'? I predict False.")
print(car.title() == "subaru")

print("Is car==car_2? I predict False.")
print(car == car_2)

print("Is car.title()==car_2? I predict True.")
print(car.title() == car_2)


# Exercise 5-2 More Conditional Tests: Write more tests, have at least one 'True' and one 'False' result for each of the
# following.

# Equality and inequality with strings:
s_1 = "This Is A String"
s_2 = "this is a string"
print(s_1 == s_2)  # False: Case-sensitive comparison.
print(s_1 == s_2.title())  # True: both sides titlecase after '.title()' method.

# Using the 'lower()' function:
print(s_1.lower() == s_2)  # True: both sides lowercase after '.lower()' method.
print(s_1 == s_2.lower)  # False: Case-sensitive comparison.

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, less than or
# equal to:
n = 4
m = 9

print(n == m)
print(n != m)

print(n < m)
print(n > m)

print(n >= m)
print(n <= m)

# Using the 'and' keyword and the 'or' keyword:
car = "subaru"
car_2 = "Subaru"

print(car == car_2 and "Subaru" == car_2)  # False: only '"Subaru" == car_2' returns 'True' BUT NOT 'car == car_2'.
print(car == car_2 or "Subaru" == car_2)  # True: ONE side returns 'True' therefor the entire statement returns 'False'.

# Whether an item is in a list:
pizzas = ["pepperoni", "cheese", "veggie", "buffalo chicken"]

print("pepperoni" in pizzas)
print("pineapple" in pizzas)

# Whether an item in not in a list:
print("pepperoni" not in pizzas)
print("pineapple" not in pizzas)
