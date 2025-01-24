# In this lesson, you'll learn to:

# Create variables
# Print variables
# Change the values assigned to variables

greeting = "Merry Christmas"
salary = 10000

# 1. greeting is a variable.
# 2. greeting is assigned the string value "Merry Christmas".
# 3. The = sign is used to assign values to variables.

print(greeting)
print(salary)


# Change Values Stored in Variables
# The value of a variable can change as the program runs, which is why it is called a variable. For example,

age = 25
print(age)
 
#  Reassigning values
age = 100
print(age)

# Output

# 25
# 100

# The initial value of age is 25. So, the first print(age) prints 25.
# Its value is then changed to 100. So, the second print(age) prints 100.

# Assign Value of One Variable to Another

color1 = "blue"
print(color1)   # Output: blue
 
color2 = "pink"
 
# Assign the value stored in color2 to color1
color1 = color2
 
print(color1)  # Output: pink
print(color2)  # Output: pink

# Output

# blue
# pink
# pink


# NOTES
# Legal Variables Name
# There are certain rules for naming variables. Let's learn about them.

# A variable name can only consist of three elements:

# alphabets
# numbers
# underscores
# Do not use spaces or any other symbols when naming a variable. If a variable name consists of two words, separate them with an underscore, _ or use camelCase.
# For example, first name and first-name are not valid variable names, but first_name and firstName are valid.