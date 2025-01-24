# Data can come to you in the incorrect format. 
# You can use the type() instruction to check the data type stored in a variable.

balance1 = "780" #string
balance2 = 780 #int
balance3 = 5.6 #float

print(type(balance1))
print(type(balance2))
print(type(balance3))

# NOTES
# The division of two integers always produces a float.

a = 4
b = 2
c = 4/2
print(c) #displays the result
print(type(c)) #displays data type


# NOTES
# The input() instruction always turns the user input into a string, no matter what the user enters.

birth_year=input() #takes an input from users
print(type(birth_year)) #displays the data type


# NOTES
# The int() instruction converts any type of value into an integer

x = "55" # x is a string
print(type(x))
y = int(x) # y is an integer
print(type(y))



# NOTES
# The float() instruction converts values into floats.
a = 15
b = float(a)


# NOTES
# In a similar way, you can ensure that values are converted into strings with the str() instruction.
a = 2.9
b = str(a)