# Day 2: 30 Days of python programming
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
country = "USA"
city = "New York"
age = 30
year = 2023
is_married = False
is_true = True
is_light_on = False
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Compare the length of your first name and your last name
print(len(first_name) == len(last_name))

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
radius = 30

# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = 3.14 * radius ** 2

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * radius

# Take radius as user input and calculate the area.
radius = float(input("Enter the radius of the circle: "))
area_of_circle = 3.14 * radius ** 2
print("The area of the circle is:", area_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
print(first_name)
print(last_name)
print(country)
print(age)


# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
