"""
Error Handling and Exceptions:

Exception Handling: Learn how to handle exceptions using try-except blocks and handle different types of exceptions.

Exception Hierarchy: Understand the hierarchy of Python exceptions and when to catch specific types of exceptions.
"""
# try:
#     # Code that may raise an exception
#     result = 10 / 0
#     print(result)
# # except ZeroDivisionError:
# #     # Code to handle the ZeroDivisionError exception
# #     print("Error: Division by zero!")
# except Exception as e:
#     # Code to handle any other exception
#     # print(f"An error occurred: {str(e)}")
#     print(f"An error occurred: {e}")

# Handling Multiple Exceptions:

# try:
#     # Code that may raise an exception
#     age = int(input("Enter your age: "))
#     print(f"You entered age is : {age}")
# except ValueError:
#     # Code to handle the ValueError exception
#     print("Error: Invalid input!")
# except KeyboardInterrupt:
#     # Code to handle the KeyboardInterrupt exception
#     print("Error: Keyboard interrupt occurred!")

# Handling Exceptions with Finally:
#
# try:
#     # Code that may raise an exception
#     file = open("myfile.txt", "r")
#     # Perform some operations
# except FileNotFoundError:
#     # Code to handle the FileNotFoundError exception
#     print("Error: File not found!")
# finally:
#     # Code that always executes, regardless of whether an exception occurred
#     file.close()


"""
Exception Hierarchy:

Catching Specific Exceptions:
"""
# try:
#     # Code that may raise an exception
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     # Code to handle the ZeroDivisionError exception
#     print("Error: Division by zero!")
# except TypeError:
#     # Code to handle the TypeError exception
#     print("Error: Invalid operation!")
# except Exception:
#     # Code to handle any other exception
#     print("An error occurred!")

# Raising Exceptions:
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {str(e)}")

"""
Exception Hierarchy:
Python's exceptions are organized in a hierarchy, with the base class Exception at the top. 
More specific exception classes inherit from Exception. You can catch specific types of exceptions by specifying their class in the except block.
"""
# try:
#     # Code that may raise an exception
#     # ...
# except FileNotFoundError:
#     # Code to handle FileNotFoundError
#     # ...
# except ValueError:
#     # Code to handle ValueError
#     # ...
# except Exception:
#     # Code to handle any other exception
#     # ...
