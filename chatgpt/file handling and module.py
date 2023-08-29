"""
File Handling and Modules:

File I/O: Discover how to read from and write to files using Python's file handling mechanisms.

Modules: Understand how to create and use modules to organize your code into reusable components.

Standard Library: Explore Python's extensive standard library modules for common tasks like working with dates, regular expressions, math operations, and more.
"""

# Reading from a File:
# Open file in read mode
# with open('Sylabus', 'r') as file:
#     content = file.read()
#     print(content)

# Writing to a File:
# Open file in write mode
# with open('Sylabus', 'w') as file:
#     file.write('Hello, World!')
#
# with open('Sylabus', 'r') as file:
#     content = file.read()
#     print(content)
#

# Open file in append mode
# with open('Sylabus', 'a') as file:
#     file.write('\nAppending new content!')

"""
Creating and Importing Packages:

Create a directory structure as follows:
"""
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py
#

"""
Add code to module1.py and module2.py.

Import and use the package in another Python file:
"""
# import my_package.module1
# import my_package.module2
#
# my_package.module1.function1()
# my_package.module2.function2()

"""
Standard Library:

Working with Dates and Times (datetime module):
"""
# from datetime import datetime
#
# current_time = datetime.now()
# print(current_time)  # Output: 2023-06-02 14:30:00.123456
#
# formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_time)  # Output: 2023-06-02 14:30:00


# Regular Expressions (re module):
import re

# text = "Hello, i am good in python both programming  and scripting language , gkrishnarm@gmail.com so you can contact " \
#        "for mail id is gkrm970@gmail.com "
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# text = "Please contact me at john.doe@example.com or jane_smith@gmail.com"
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# text = "You can reach us at info@company.com or support@company.com"
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# text = "You can reach us at this phone number 8123114970"
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# matches = re.findall(pattern, text)
# print(matches)  # Output: ['example@example.com']

#
# import re
#
# text = "Contact us at 8123453849 or 8123114970 for assistance."
# pattern = r'\b(?:\+?\d{1,3}[-.])?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b'
#
# matches = re.findall(pattern, text)
# print(matches)  # Output: ['+1-123-456-7890', '555-1234']
#
# import re
#
# text = "I am an active member of the community. keep moving!"
# pattern = r'\bactive\b'
# matches = re.findall(pattern, text, flags=re.IGNORECASE)
# print(matches)  # Output: ['active']
#
#
# # Math Operations (math module):
# import math
#
# square_root = math.sqrt(25)
# print(square_root)  # Output: 5.0
#
# logarithm = math.log10(100)
# print(logarithm)  # Output: 2.0
