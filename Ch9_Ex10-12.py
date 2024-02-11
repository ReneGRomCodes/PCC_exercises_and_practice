# Exercise 9-10 Imported Restaurant: Store your latest 'Restaurant' class in a module and import it. Make a 'Restaurant'
# instance and call one of the methods to show that the import statement is working.


from Ch9_modules_1 import Restaurant


restaurant = Restaurant("mamma mia's trattoria", "italian")
restaurant.describe_restaurant()


# Exercise 9-11 Imported Admin: Store your 'User', 'Privileges' and 'Admin' classes from Exercise 9-8 in a module. Make
# an 'Admin' instance and call show 'show_privileges()' to show that everything is working.


from Ch9_modules_1 import Admin


admin = Admin("maya", "patel", "StarSeeker42", "sapphirewhisper49")
admin.privileges.show_privileges()


# Exercise 9-12 Multiple Modules: Store the 'User' class in one module and the 'Privileges' and 'Admin' class in a
# separate module. Then create an 'Admin' instance and call 'show_privileges()' to show that everything is working.
# - 'User' class used from 'Ch9_modules_1.py', 'Privileges' and 'Admin' class from 'Ch9_modules_2.py'.


from Ch9_modules_2 import Admin


admin = Admin("oliver", "thompson", "EchoEngineer99", "thunderforge12")
admin.privileges.show_privileges()
