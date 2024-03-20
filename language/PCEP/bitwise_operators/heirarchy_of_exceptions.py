"""
When can we use the raise keyword?
Inside the except block, but unnamed
Inside the try block together with a named exception

Which of the below code snippets is correct?

A.
a = input("Enter a number: ")
try:
    float(a) / 0
except Exception:
    print("Hmm an error occurred.")
except TypeError, ZeroDivisionError:
    print("Please enter valid numbers, besides 0.")

B.
a = input("Enter a number: ")
try:
    float(a) / 0
except TypeError, ZeroDivisionError:
    print("Please enter valid numbers, besides 0.")

C.
a = input("Enter a number: ")
try:
    float(a) / 0
except (TypeError, ZeroDivisionError):
    print("Please enter valid numbers, besides zero.")

C

What are the abstract exceptions?

General exceptions that they include other exceptions.

In the following snippet, which exception could replace the existing one? try:

try:
    y = 5 / 0
except ZeroDivisionError:
    print("Can't divide with zero.")

BaseException

What is the output of the following code snippet? try:

try:
    z = 3 // 0
except ZeroDivisionError:
    print("Zero won't work!")
except ArithmeticError:
    print("We have a problem!")

Zero won't work!

What is common between AssertionError and ArithmeticError?

They both stem from Execption

ZeroDivisionError is a special case of:

ArithmeticError
Exception

Why shouldn't we put more general exceptions before specific ones?

Because the specific exception would never excuted and become useless

What are the specific exceptions included in the LookupError?
keyError
IndexError




"""
