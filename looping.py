# Looping is a fundamental concept in Python that allows you to repeat
# a block of code multiple times. Python provides several ways to loop, including:

# 1. for loops: Used to iterate over a sequence (e.g., list, tuple, string, etc.).
# 2. while loops: Used to repeat a block of code as long as a condition is true.
# 3. Loop control statements: break, continue, and pass to control the flow of loops.

# 1. for Loops
# for item in sequence:
#     # Code to execute for each item



print("======== start looping list condition ======")

# Example 1: Looping Over a List
# A for loop is used to iterate over a sequence (like a list, tuple, string, or range).

fruits = ["apple", "banana", "cherry\n"]
for fruit in fruits:
    print(fruit)

print("======== end looping list condition ====== \n")

print("======== start looping range condition ======")

# Example 2: Looping Over a Range
# The range() function generates a sequence of numbers.


for i in range(5):
    print(i + 1)

print("======== end looping range condition ====== \n")


print("======== start looping string condition ======")

# Example 3: Looping Over a String
# You can loop over each character in a string.

for char in "Hello World\n":
    print(char)

print("======== end looping string condition ====== \n")


print("======== start while condition ======")

# 2. while Loops
# A while loop repeats a block of code as long as a condition is True.

# while condition:
#     # Code to execute while the condition is true

count = 0
down = 10

while count <= 5:
    print(f"{count}")
    count += 1

print("\n")

while down > 0:
    print(down)
    down -= 1

print("======== end while condition ======\n")

# 3. Loop Control Statements
# These statements allow you to control the flow of loops.

print("======== start break condition ======")

# a. break
# The break statement exits the loop immediately.

for a in range(10):
    if a > 5:
        break
    
    print(f"{a}")


print("======== end break condition ======\n")

print("======== start continue condition ======")

# b. continue
# The continue statement skips the rest of the code in the loop and moves to the next iteration.

for i in range(10):
    if i % 2 == 0:
        continue # Skip the rest of the code for i % 2 == 0
    
    print(i)
print("======== end continue condition ======\n")


print("======== start pass condition ======")

# c. pass
# The pass statement is a placeholder that does nothing. It’s used when you need a statement
# for syntax reasons but don’t want to execute any code.

for j in range(10):
    if j == 2:
        pass #Do nothing in here
    
    print(j)

print("======== end pass condition ====== \n")


print("======== start nested condition ======")
# 4. Nested Loops
# You can place one loop inside another loop. This is called nesting.

for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")


print("======== end nested condition ====== \n")



print("======== start enumerate condition ====== \n")
# 5. Looping with enumerate
# The enumerate() function allows you to loop over a sequence while keeping track of the index.

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"index {index}: {fruit}")

print("======== end enumerate condition ====== \n")