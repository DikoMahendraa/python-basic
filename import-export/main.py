# Importing the entire module
import math_utils

result = math_utils.add(5, 3)
print(f"Addition: {result}")
print(f"PI: {math_utils.PI}")

# Importing specific components
from math_utils import subtract, PI

difference = subtract(10, 4)
print(f"Subtraction: {difference}")
print(f"PI: {PI}")


# Relative vs Absolute Imports

# 1. Absolute Import: Use the full path from the project root.
# import myproject.mymodule

# 2. Relative Import: Use . or .. to navigate relative to the current module.
# from .mymodule import myfunction


