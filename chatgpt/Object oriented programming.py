"""
Object-Oriented Programming:

Classes and Objects: Understand the principles of object-oriented programming (OOP), create classes, and instantiate
objects.

Inheritance and Polymorphism: Explore inheritance, subclassing, method overriding, and polymorphism to build more
complex class hierarchies.

Advanced OOP Concepts: Learn about encapsulation, abstraction, class methods, static methods, and properties.


"""
"""
Classes and Objects:
Create a class with attributes and methods.
Instantiate objects from the class and access their attributes and methods.
"""

# Class example
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
#
# # Instantiate objects
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)
#
# # Access object attributes and methods
# print(person1.name)       # Output: Alice
# person2.greet()           # Output: Hello, my name is Bob and I'm 30 years old.

"""
Inheritance and Polymorphism:
Create subclasses that inherit properties and methods from a base class.
Override methods in the subclass for specialized behavior.
Utilize polymorphism to use objects of different classes interchangeably.
"""

# Base class
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def sound(self):
#         print("Generic animal sound")
#
# # Subclass inheriting from Animal
# class Dog(Animal):
#     def sound(self):
#         print("Woof!")
#
# # Subclass inheriting from Animal
# class Cat(Animal):
#     def sound(self):
#         print("Meow!")
#
# # Polymorphism in action
# animals = [Dog("Buddy"), Cat("Whiskers"), Dog("Max")]
#
# for animal in animals:
#     animal.sound()
# # Output:
# # Woof!
# # Meow!
# # Woof!


"""Advanced OOP Concepts: Encapsulation: Use access modifiers (public, protected, private) to control access to 
attributes and methods. Abstraction: Define abstract classes or methods that provide a common interface for 
subclasses. Class methods and static methods: Use @classmethod and @staticmethod decorators to define methods that 
are associated with the class rather than instances. Properties: Implement getter and setter methods using the 
@property decorator. 
"""

# Encapsulation and Abstraction
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number     # Protected attribute
        self._balance = balance                   # Protected attribute

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self._balance

# Class methods and static methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        return cls.add(a, a) * cls.add(b, b)

# Properties
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

# Usage examples
account = BankAccount("123456", 1000)
# account.deposit(500)
account.withdraw(500)
print(account.get_balance())        # Output: 1500


print(MathUtils.multiply(2, 3))     # Output: 20

circle = Circle(5)
circle.radius = 10
print(circle.radius)                # Output: 10
