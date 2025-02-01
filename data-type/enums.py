from enum import Enum

# What is an Enum?
# Enum (short for enumeration) is a data type used to define a set of named constant values. By using enum, you can make your code more readable and maintainable because the values have descriptive names instead of just raw numbers or strings.

# Why Use Enums?
# Clarity: Descriptive names make the code easier to understand.

# Safety: Restricts valid values, reducing the chance of errors.

# Maintainability: If you need to change a value, you only need to update it in one place.



class Categories(Enum):
  AKTIF = "aktif"
  NONAKTIF = "nonaktif"
  PENDING = "pending"


class Hari(Enum):
    SENIN = 1
    SELASA = 2
    RABU = 3
    KAMIS = 4
    JUMAT = 5
    SABTU = 6
    MINGGU = 7

print(Categories.AKTIF)

x = Hari.SENIN


print(x)