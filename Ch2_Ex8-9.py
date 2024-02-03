# Exercise 2-8 Number Eight: Write addition, subtraction, multiplication and division operations that each result in the
# number 8. Be sure to enclose your operations in 'print' statements.


print(5 + 3)
print(11 - 3)
print(4 * 2)
print(int(16 / 2))  # Used 'int()' function because division results in a floating point number.


# Exercise 2-9 Favorite Number: Store your favorite number in a variable, create a message that reveals your favorite
# number and print that message.


fav_number = 7

message = "My favorite number is " + str(fav_number) + "."  # Added str() function to avoid 'TypeError'.
print(message)
