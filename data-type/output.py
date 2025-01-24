# Introduction to Output

# We have previously used print() to display a single value or variable.
# Now, you'll learn how to print multiple values and variables. You'll also explore f-strings, which makes it easier to print multiple data in the desired format.

# Print Multiple Values
# We can print multiple pieces of data at once by separating them with commas. For example:

# Display two numbers
print(67, -5, 19)
 
# Display two strings
print("Hey.", "Are you enjoying the course?")
 
# Display numbers and strings
print("Rating:", 8.5)


# Print Newline (Enter Key)
# It's possible to use a single print() function to display output in multiple lines.

# To do this, we use the newline character \n in the position where we want to break the line:

print("Welcome to Programiz\nThe Amazing Spider-Man")

# Output

# Welcome to Programiz
# The Amazing Spider-Man

# Python f-strings
# Python offers another way to format and print strings: f-strings, which simplify printing multiple values and variables.

# To specify an f-string, simply put an f before the starting quotation marks. For example,

print(f"Hello") 

# Print Variables Using f-strings
# To print variables using f-strings, you need to wrap them inside curly braces {}. For example:

name = "Alice"
location = "Wonderland"
 
print(f"My name is {name} and I live in {location}.")

# Output

# My name is Alice and I live in Wonderland.


# Common Mistakes (I)
# 1. Spelling Error
# 2. Adding Spaces at the Beginning