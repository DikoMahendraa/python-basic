# In Python, you can create a class using the class keyword.
# A class is a blueprint for creating objects (instances).
# To define a constructor for the class, you use the __init__ method. The constructor is automatically called when
# you create an instance of the class.


# Example 1: Simple Class with Constructor
class Person:
    # self in python constructor is mandatory, its mean like "this." if on nodejs
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 30)
person1.greet()  # Output: Hello, my name is Alice and I am 30 years old.



# Example 2: Class with Default Values in Constructor
class Person1:
    def __init__(self, name="Guest", age=0):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person1()  # Uses default values
person1.greet()  # Output: Hello, my name is Guest and I am 0 years old.

person2 = Person1("Bob", 25)
person2.greet()  # Output: Hello, my name is Bob and I am 25 years old.



# Example 3: Class with Methods
class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, x):
        self.value += x

    def subtract(self, x):
        self.value -= x

    def get_value(self):
        return self.value

# OUTPUT flow
# 10 + 5 - 3 = 12    
calc = Calculator(10)
calc.add(5)
calc.subtract(3)
print(calc.get_value())  


# Example 5: Class Inheritance
# You can create a subclass that inherits from a parent class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def talk_to_friend(self, friend):
        print(f"{friend} allright I understand.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

    def try_to_talk(self):
        self.talk_to_friend("Oke lisa, ")

animal = Animal("Generic Animal")
animal.speak()  # Output: Generic Animal makes a sound.

dog = Dog("Buddy")
dog.speak()  # Output: Buddy barks.
dog.try_to_talk()  # Output: Oke list, allright I understand.



# Key Points:
# Use class to define a class.

# Use __init__ to define the constructor.

# Use self to refer to the instance and access its attributes and methods.

# You can add methods to define the behavior of the class.

# Use __str__ to provide a string representation of the object.

# Use inheritance to create subclasses.