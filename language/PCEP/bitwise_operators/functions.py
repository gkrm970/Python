"""
Method is called by its name, but it is associated with an object.

You're absolutely right! In object-oriented programming (OOP), methods are functions that are associated with objects. Here's a breakdown of this concept:

1. Objects and Classes:

Object: An object is an instance of a class. It represents a specific entity with its own set of properties (data) and behaviors (methods).
Class: A class is a blueprint that defines the properties and methods that objects of that class will have. It serves as a template for creating objects.

What is the output of the following snippet:

def my_function(*students):
  print("The tallest student is " + students[2])

my_function("James", "Ella", "Jackson")

The tallest student is Jackson

The output of the following snippet of the code will be:

a = 0
def add_one(a):
	return a+1

result = add_one(a)
print(result)

1

Choose the correct answer which defines a function to get numeric input from the user:

def my_function():
  return int(input("Enter a number: "))

my_function()

int(input("Enter a number: ")) is numeric input type

Regarding the definition of the function and the sample input, Choose the correct value of the output.

Function :  def multi_func(num1,num2):
                      return num1 *num2
Sample input: print ( multi_func(5 , num1= 10) )

error
The correct input should be print ( multi_func(5 , 10) )
Or
print ( multi_func(num1=5 , num2=10) )

What will be the result of calling the print_info function with the arguments 'john' and 19?

def print_info(name, age=18):
    print(name, age)

print_info('john', 19)

john 19

What is the output of the following snippet:

def my_function(*students):
  print("The tallest student is " + students[2])

my_function("James", "Ella", "Jackson")

The tallest student is Jackson

Define a function that gets the user input and multiply it by a number we passed to the function.

Sample input:  6
Sample output:

print( multi_num(5) )
30

def multi_num(num):
    return int (input()) * num


The function can have only one parameter. If any data (parameters) are passed, they are passed explicitly.

False

Key Points:

Even with default arguments, the function definition itself only has one parameter.
When calling the function, you can either provide the argument explicitly or rely on the default value if no argument is passed.
These approaches ensure that your function consistently works with a single parameter, promoting clarity and avoiding confusion with multiple arguments.

What is the error in the following snippet code:

def multi_func():
  result = int(input()) * 5
  return result

print(result)

the first thing is to call the function
the result is not defined as a global variable

The output of the following snippet of the code will be:

a = 0
def add_one(a):
	return a+1

result = add_one(a)
print(result)





"""

# def my_function(*students):
#   print("The tallest student is " + students[5])
#
# my_function("James", "Ella", "Jackson")

a = 0


# def add_one(a):
#     return a + 1
#
#
# result = add_one(a)
# print(result)

# def multi_func(num1, num2):
#     return num1 * num2
#
#
# print(multi_func(5, num1=10))
