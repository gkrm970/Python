"""
Certainly! Here are some examples of lambda functions in Python, starting from simple to more complex scenarios:

"""
# Simple Addition:
# add = lambda x, y: x + y
# print(add(5, 3))  # Output: 8

"""Lambda function with tuples:
Example 1: Multiply elements of a tuple by a constant"""

# my_tuple = (1, 2, 3, 4, 5)
# result = tuple(map(lambda x: x * 2, my_tuple))
# print(result)
# Output: (2, 4, 6, 8, 10)

# Example 2: Filter even numbers from a tuple
# my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# result = tuple(filter(lambda x: x % 2 == 0, my_tuple))
# print(result)
# Output: (2, 4, 6, 8, 10)

# Filtering Even Numbers:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Doubling Numbers in a List:
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(lambda x: x * 2, numbers))
# print(doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# my_list = [1, 2, 3, 4, 5]
# result = list(map(lambda x: x**2, my_list))
# print(result)
# Output: [1, 4, 9, 16, 25]


# Sorting List of Tuples by Second Element:
# students = [("Alice", 90), ("Bob", 80), ("Charlie", 95), ("Dave", 85)]
# sorted_students = sorted(students, key=lambda x: x[1], reverse=False)
# print(sorted_students)
# # Output: [('Charlie', 95), ('Alice', 90), ('Dave', 85), ('Bob', 80)]

# Computing Fibonacci Sequence:
# fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(6))  # Output: 8

# Summing Values from Multiple Lists:
# list1 = [1, 2, 3,4]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9,10]
# sum_lists = lambda *args: sum(args)
# print(sum_lists(*list1, *list2, *list3))  # Output: 45

# Lambda function with dictionaries:
# Example 1: Sort a dictionary by values

# my_dict = {'apple': 5, 'banana': 2, 'orange': 3, 'grape': 1}
# result = dict(sorted(my_dict.items(), key=lambda x: x[1]))
# result = dict(sorted(key=lambda x: x[1]), my_dict.items())  # this is not possible
# print(result)
# Output: {'grape': 1, 'banana': 2, 'orange': 3, 'apple': 5}
