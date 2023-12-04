# Python program to demonstrate working of a map.
# Return double of n
# def addition(n):
#     return n + n
#
#
# # We double all numbers using map()
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# # Double all numbers using a map and lambda
#
# numbers = [1, 2, 3, 4]
# result = map(lambda x: x * 2, numbers)
# print(list(result))

# # Add two lists using map and lambda

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
# #
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))
#
# # List of strings
# l = ['sat', 'bat', 'cat', 'mat']
#
# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)
#
# # let's code it in comprehensions
# test = [list(s) for s in l]
# print(test)
#
#
# # Define a function that doubles even numbers and leaves odd numbers as is
# def double_even(num):
#     if num % 2 == 0:
#         return num * 2
#     else:
#         return num


#
#
# print(double_even(6))
#
# # Create a list of numbers to apply the function to
# numbers = [1, 2, 3, 4, 5]
# #
# # # Use a map to apply the function to each element in the list of numbers
# result = list(map(double_even, numbers))
# print(result)  # [1, 4, 3, 8, 5] only even numbers are doubled.

# Converting characters to their uppercase equivalents:
# characters = ['a', 'b', 'c', 'd', 'e']
# uppercase_characters = list(map(lambda char: char.upper(), characters))
# print(uppercase_characters)  # Output: ['A', 'B', 'C', 'D', 'E']

# Filtering and transforming a list of employee objects based on their salaries:
# employees = [
#     {"name": "Alice", "salary": 50000},
#     {"name": "Bob", "salary": 40000},
#     {"name": "Charlie", "salary": 60000},
# ]
#
# salary_increases = list(map(lambda emp: {"name": emp["name"], "raise": emp["salary"] * 0.1,
#                                          "total_sal": emp["salary"] * 0.1 + emp["salary"]}, employees))
# print(salary_increases)
# Output: [{'name': 'Alice', 'raise': 5000.0}, {'name': 'Bob', 'raise': 4000.0}, {'name': 'Charlie', 'raise': 6000.0}]
# The map() function and lambda expressions provide a powerful combination for manipulating and transforming data
# in an expressive and concise manner.

