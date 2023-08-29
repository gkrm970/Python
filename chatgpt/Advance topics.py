"""
Advanced Topics:

Generators and Iterators: Discover how to create generators and iterators for efficient memory usage and working with large datasets.

Decorators: Learn about decorators, a powerful Python feature used to modify the behavior of functions or classes.

Context Managers: Understand how to use context managers to properly manage resources, such as files, using the with statement.
"""


# Generators and Iterators:
# Creating a Generator:
# def my_generator():
#     for i in range(5):
#         yield i
#
# gen = my_generator()
# for item in gen:
#     print(item)
#
# # or can also write like this
# def my_generator():
#     values = []
#     for i in range(5):
#         values.append(i)
#         print(i)
#     return values
#
# values_list = my_generator()
# for item in values_list:
#     print(item)
#

# Iterating over a Generator:
# def squares(n):
#     for i in range(n):
#         yield i**2
#
# for num in squares(5):
#     print(num)
# # or comprehension method.
# abc = [i**2 for i in range(5)]
# print(abc)

# Using Generator Expressions:
# gen = (x**2 for x in range(5))
# # print(list(gen))
# for num in gen:
#     print(num)
#

"""
Decorators:

Creating a Decorator:
"""
# def my_decorator(func):
#     def wrapper():
#         print("Before function execution")
#         func()
#         print("After function execution")
#     return wrapper
#
# @my_decorator
# def my_function():
#     print("Inside the function")
#
# my_function()

# Decorating Functions with Arguments:
# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             # global result
#             for _ in range(n):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Alice")

# Context Managers:
# Using the with Statement:
# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)

# Creating a Custom Context Manager:
# class MyContextManager:
#     def __enter__(self):
#         # Code to set up resources
#         print("Entering the context")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # Code to clean up resources
#         print("Exiting the context")
#
# with MyContextManager():
#     # Code inside the context
#     print("Doing some work")

# Continue real world example
# class MyContextManager:
#     def __init__(self, file_path, mode):
#         self.file_path = file_path
#         self.mode = mode
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.file_path, self.mode)
#         print(f"File '{self.file_path}' opened in mode '{self.mode}'")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#             print(f"File '{self.file_path}' closed")
#         if exc_type is not None:
#             print(f"An exception of type {exc_type} occurred: {exc_val}")
#
# # Usage example
# with MyContextManager("example.txt", "w") as file:
#     file.write("Hello, World!")
#     # Perform more operations on the file
#
# print("Outside the context")

# Using contextlib for Context Managers:

from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Code to set up resources
    print("Entering the context")

    try:
        yield  # Code inside the context
    finally:
        # Code to clean up resources
        print("Exiting the context")

with my_context_manager():
    # Code inside the context
    print("Doing some work")
