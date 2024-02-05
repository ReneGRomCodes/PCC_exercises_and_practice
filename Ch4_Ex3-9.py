# Exercise 4-3 Counting to Twenty: Use a 'for' loop to print the numbers from 1 to 20, inclusive.


for n in range(1, 21):
    print(n)


# Exercise 4-4 One Million: Make a list of numbers from one to one million, then use a 'for' loop to print the numbers.


numbers = list(range(1, 1000001))

for number in numbers:
    print(number)


# Exercise 4-5 Summing a Million: use the list of numbers from one to one million, then use 'min()' and 'max()' to make
# sure your list actually starts at one and ends at one million. Also, use the 'sum()' function to see how quickly
# Python can add a million numbers.


print(min(numbers))
print(max(numbers))

n = sum(numbers)
print(n)


# Exercise 4-6 Odd Numbers: Use the third arguments of the 'range()' function to a list of odd numbers from 1 to 20,
# then use a 'for' loop to print each number.


odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)


# Exercise 4-7 Threes: Make a list of the multiples of 3 from 3 to 30. Use a 'for' loop to print the numbers in your
# list.


multiples_three = []

for value in range(1, 30):
    if value % 3 == 0:
        multiples_three.append(value)

for multiple in multiples_three:
    print(multiple)


# Variation printing the value after adding it to the list instead of printing it from the finished list later.
for value in range(1, 30):
    if value % 3 == 0:
        multiples_three.append(value)
        print(value)


# Exercise 4-8 Cubes: Make a list of the cube of each integer from 1 through 10, then use a 'for' loop to print out the
# value of each cube.


cubes = []

for cube in range(1, 11):
    cubes.append(cube ** 3)

for cube in cubes:
    print(cube)


# Variation printing the value of each cube after adding it to the list instead of printing it from the finished list
# later.
for cube in range(1, 11):
    cubes.append(cube ** 3)
    print(cube)


# Exercise 4-9 Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes = [value**3 for value in range(1, 11)]
