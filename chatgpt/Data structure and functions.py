"""
Lists and Tuples:
Create a list and perform basic operations like appending, accessing elements by index, slicing, and modifying elements.
Iterate over a list using loops and list comprehensions.
Explore built-in list methods like append(), remove(), sort(), and reverse().
Work with tuples, which are similar to lists but immutable.
"""

# # List example
# fruits = ['apple', 'banana', 'orange']
# print(fruits[0])  # Output: apple
# print(fruits[1:])  # Output: ['banana', 'orange']
#
# # Looping through a list
# for fruit in fruits:
#     print(fruit)
#
# # List comprehension
# squared_nums = [num ** 2 for num in range(1, 5)]
# print(squared_nums)  # Output: [1, 4, 9, 16]
#
# # Tuple example
# point = (3, 7)
# x, y = point
# print(x, y)  # Output: 3 7

"""
Dictionaries:
Create dictionaries and access values using keys.
Add, modify, and remove key-value pairs.
Iterate over dictionaries using loops and dictionary comprehensions.
Utilize dictionary methods like keys(), values(), and items().
"""
# # Dictionary example
# student = {'name': 'John', 'age': 20, 'grade': 'A'}
# print(student['name'])  # Output: John
# print(student.get('age'))  # Output: 20
#
# # Modify dictionary
# student['age'] = 21
# student['school'] = 'XYZ School'
#
# # Looping through a dictionary
# for key, value in student.items():
#     print(key, value)
#
# # Dictionary comprehension
# squared_nums = {num: num ** 2 for num in range(1, 5)}
# print(squared_nums)  # Output: {1: 1, 2: 4, 3: 9, 4: 16}

# example
# my_dict = {'apple': 5, 'banana': 2, 'orange': 3, 'grape': 1}
# result = {k: v for k, v in my_dict.items() if v > 2}
# print(result)
# Output: {'apple': 5, 'orange': 3}


"""
Functions:
Define and call functions with and without parameters.
Understand the concept of return values.
Utilize default parameter values and keyword arguments.
Explore the scope of variables (global vs. local).
"""

# # Function example
# def greet(name):
#     print(f"Hello, {name}!")
#
#
# greet('Alice')  # Output: Hello, Alice!
#
#
# # Function with return value
# def add_numbers(a, b):
#     return a + b
#
#
# result = add_numbers(3, 4)
# print(result)  # Output: 7
#
#
# # Function with default parameter value
# def power_of(x, power=2):
#     return x ** power
#
# print(power_of(3))  # Output: 9
# print(power_of(3, 3))  # Output: 27
#
#
# # Function with keyword arguments
# def create_person(name, age, city):
#     print(f"Name: {name}, Age: {age}, City: {city}")
#
#
# create_person(name='John', city='New York', age=25)
# # Output: Name: John, Age: 25, City: New York

#####################################################################################################################

"""
Certainly! Let's explore some more complex examples of data structures and functions:

Lists and Tuples:
Combine multiple lists using the zip() function.
Sort a list of dictionaries based on a specific key using the sorted() function and lambda functions.
"""
# Combining lists using zip()
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# countries = ['USA', 'Canada', 'Australia']
#
# combined = list(zip(names, ages, countries))
# combined1 = zip(names, ages, countries)
# print(combined)
# print(combined1)
# Output1: [('Alice', 25, 'USA'), ('Bob', 30, 'Canada'), ('Charlie', 35, 'Australia')]
# Output2: <zip object at 0x000001F79D163240>

# Sorting a list of dictionaries based on a key
# students = [
#     {'name': 'Alice', 'age': 25, 'grade': 'A'},
#     {'name': 'Bob', 'age': 30, 'grade': 'B'},
#     {'name': 'Charlie', 'age': 35, 'grade': 'A'}
# ]
#
# sorted_students = sorted(students, key=lambda x: x['age'] ,reverse=False)
# print(sorted_students)
# Output: [{'name': 'Alice', 'age': 25, 'grade': 'A'}, {'name': 'Bob', 'age': 30, 'grade': 'B'}, {'name': 'Charlie', 'age': 35, 'grade': 'A'}]

# or another way to get solution
# import operator
#
# students = [
#     {'name': 'Alice', 'age': 25, 'grade': 'A'},
#     {'name': 'Bob', 'age': 30, 'grade': 'B'},
#     {'name': 'Charlie', 'age': 35, 'grade': 'A'}
# ]
#
# sorted_students = sorted(students, key=operator.itemgetter('age'), reverse=False)
# print(sorted_students)

# another way
# import operator

# def sort_students_by_age(students):
#     sorted_students = sorted(students, key=operator.itemgetter('age'), reverse=False)
#     return sorted_students
#
# students = [
#     {'name': 'Alice', 'age': 25, 'grade': 'A'},
#     {'name': 'Bob', 'age': 30, 'grade': 'B'},
#     {'name': 'Charlie', 'age': 35, 'grade': 'A'}
#      ]
#
# sorted_students = sort_students_by_age(students)
# print(sorted_students)

"""
Dictionaries:
Count the frequency of elements in a list using a dictionary.
Merge two dictionaries using the update() method.
"""
# # Counting the frequency of elements in a list
# numbers = [1, 2, 3, 2, 1, 3, 4, 2, 1]
# frequency = {}
#
# for num in numbers:
#     frequency[num] = frequency.get(num, 0) + 1
#
# print(frequency)
# # Output: {1: 3, 2: 3, 3: 2, 4: 1}
#
# # Merging two dictionaries
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
#
# dict1.update(dict2)
# print(dict1)
# # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


"""
Functions:
Use recursion to implement the Fibonacci sequence.
Create a higher-order function that returns a function.
"""
# Recursive Fibonacci sequence
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(6))
# # Output: 8
#
# # Higher-order function
# def multiplier(n):
#     def multiply(x):
#         return x * n
#     return multiply
#
# double = multiplier(2)
# print(double(5))
# Output: 10

"""
Lists and Tuples:
Use list comprehension to filter and transform elements based on specific conditions.
Flatten a nested list using recursion.
"""

# List comprehension with condition
# numbers = [1, 2, 3, 4, 5, 6]
# even_squares = [num ** 2 for num in numbers if num % 2 == 0]
# print(even_squares)
# # Output: [4, 16, 36]

# Flattening a nested list
# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
#
# def flatten_list(nested):
#     flattened = []
#     for item in nested:
#         if isinstance(item, list):
#             flattened.extend(flatten_list(item))
#         else:
#             flattened.append(item)
#     return flattened
#
#
# flat_list = flatten_list(nested_list)
# print(flat_list)
# # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
Dictionaries:
Group a list of dictionaries based on a specific key using defaultdict.
Find the key corresponding to the maximum value in a dictionary.
"""
from collections import defaultdict

# Grouping dictionaries by a key
# students = [
#     {'name': 'Alice', 'grade': 'A'},
#     {'name': 'Bob', 'grade': 'B'},
#     {'name': 'Charlie', 'grade': 'A'},
#     {'name': 'Dave', 'grade': 'B'},
#     {'name': 'gk', 'grade': 'A'},
# ]
#
# grouped_students = defaultdict(list)
# for student in students:
#     grouped_students[student['grade']].append(student['name'])
#
# print(dict(grouped_students))
# # Output: {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'Dave']}
#
# # Finding the key with the maximum value in a dictionary
# grades = {'Alice': 90, 'Bob': 80, 'Charlie': 95, 'Dave': 85}
# best_student = max(grades, key=grades.get)
# print(best_student)
# # Output: Charlie

"""
Functions:
Use recursion to implement the factorial of a number.
Create a decorator to measure the execution time of a function.
"""
import time

# Recursive factorial function
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(6))
# Output: 720

# Decorator to measure execution time
# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Execution time: {execution_time} seconds")
#         return result
#     return wrapper
#
# @measure_time
# def process_data(data):
#     # Code to process the data
#     time.sleep(2)
#
# process_data("dummy data")
# # Output: Execution time: 2.000227928161621 seconds


"""
Nested Data Structures:
Create a nested list or dictionary to represent hierarchical data.
Access and modify elements in the nested structure.
"""

# Nested list example
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][2])      # Output: 6
#
# # Nested dictionary example
# students = {
#     'Alice': {'age': 20, 'grade': 'A'},
#     'Bob': {'age': 18, 'grade': 'B'}
# }
# print(students['Alice']['grade'])    # Output: A

"""
Lambda Functions and Higher-Order Functions:
Define and use lambda functions (anonymous functions) for concise and one-time use cases.
Utilize higher-order functions that take other functions as arguments or return functions as results.
"""
# Lambda function example
# add = lambda x, y: x + y
# print(add(3, 4))       # Output: 7
#
# # Higher-order function example
# def apply_operation(func, x, y):
#     return func(x, y)
#
# result = apply_operation(add, 3, 4)
# print(result)          # Output: 7

"""
Sorting and Filtering:
Sort a list using the built-in sorted() function or by specifying custom sorting criteria.
Filter elements from a list based on specific conditions using list comprehensions or the filter() function.
"""
# Sorting a list
numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers,reverse=True)
print(sorted_numbers)       # Output: [1, 2, 3, 5, 8, 9]

# Custom sorting criteria
words = ['apple', 'catlllllllllllll', 'ball', 'dog']
sorted_words = sorted(words, key=len)
print(sorted_words)         # Output: ['cat', 'dog', 'ball', 'apple']

# Filtering elements from a list
# even_numbers = [num for num in numbers if num % 2 == 0]
even_numbers = filter(lambda num : num % 2 ==0 , numbers)
print(list(even_numbers))         # Output: [2, 8]
