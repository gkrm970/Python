"""
What is the output of the following snippet:

def my_function(*ages):
  print("The older friend is " + ages[0] + " years")

my_function("13", "12", "11")

The older friend is 13 years

multiple arguments respresents as a list of arguments

What is the output of the following snippet:

def my_function(arg1, *argv):
    print ("First argument:", arg1)
    for arg in argv:
        print("Next argument:", arg)

my_function('Welcome', 'to', 'Python!')

First argument: Welcome
Next argument: to
Next argument: Python

What is the output of the following snippet:

def division(a,b):
    return a/b

division(8,2)

4.0

What is the output of the following snippet:

def my_function(*argv):
  print(argv)

my_function('Hello', 'World!')

('Hello', 'World!') ---> tuple

What is the output of the following snippet:

def my_function(*argv):
    for arg in argv:
        print(arg)

my_function('Hello', 'World!')

Hello
World!

What is the output of the following snippet:

def sum(a,b):
    return a+b

print(sum(2,3))

5

What is the output of the following snippet:

def my_function(*argv):
  print(argv[0])

my_function('Hello', 'World!')

Hello

What is the output of the following snippet:

def sum(*args):
    for arg in args:
        result += arg
    return result

print(sum(2,3,1))

error




"""


# def my_function(*argv):
#     print(argv)
#
#
# my_function('Hello', 'World!')
#
# def my_function(*argv):
#     for arg in argv:
#         print(arg)
#
# my_function('Hello', 'World!')

# def sum(a, b):
#     return a + b
#
#
# print(sum(2, 3))

# def sum(*args):
#     """Calculates the sum of an arbitrary number of arguments."""
#
#     result = 0  # Initialize the sum to 0
#     for arg in args:
#         result += arg
#     return result
