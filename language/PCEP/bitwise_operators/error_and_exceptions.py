"""
What mechanisms does Python provide to deal with errors?

1. Exceptions raising
2. User defined exceptions
3. Built-in exceptions
4. User defined and built-in exceptions
5. The special keywords try and except


What is the error thrown by the following code snippet?

3 // 0 == 3 % 3   ----> zero division error

What is the order of the try/except code blocks?

the except codeblock only gets executed if the try codeblock fails

Which of the following code snippet would raise an unhandled exception?

The code snippet that would raise an unhandled exception is C.

Here's the explanation for each snippet:

A. This code handles a NameError exception. If y is not defined, it will catch the exception and print "y is not defined."

B. This code handles an IndexError exception. If the index 7 is out of bounds for the string 'seasalt', it will catch the exception and print "No character found in that index."

C. This code, however, tries to concatenate a string ('y') with an integer (1). This operation raises a TypeError, not a ValueError. Since the except block is looking for a ValueError, the exception will

What is the error thrown by the following code snippet?

list1 = [1, 2, 3, 4]
list1[4]

IndexError: list index out of range

What is the output of the following python code?

x = 5
y = "Sally"
print(str(x) + y)

output: 5Sally

We can build specific exceptions for certain errors.

True

What is the output of the following code block?

try:
      print("my_string"[1/0])
except IndexError:
      print("index error")
except ZeroDivisionError:
      print("zero error")
except:
      print("other error")

output: zero error

When does Python throw a TypeError?

for wrong data types passed in operation and functions

At most one

When does Python throw a ValueError?

wrong values passed in operation and functions

What may happen if our Python program does not handle errors?

our program will crash
our programme stop running, and an error appears in console
the console return error








"""
