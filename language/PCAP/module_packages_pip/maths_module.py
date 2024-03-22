"""
What is a module in Python?

The total of Python's built-in functions

An abstract function which can be used in many cases

A file that groups related code for specific operations-->correct

External Python code that we have to install ourselves

Answer: A file that group related code for specific operations


What is a namespace in Python?


A. The variables contained within a module

B. The names of a module's files

C. The names of a module's entities

D. Names contained in our code and modules --> correct

Answer: Names contained in our code and modules.


What methods does Python offer to work with modules?


the import module


the import function


the import variable


the import keyword

Answer: the import module
so that we can use function/methods/variables/keywords etc from the module


Which of the following statements are correct?

import math

from math import pi, sin

import math as m

All options are correct

Answer: All options are correct



from math import * -->also correct but not reccomendated
Some useful math functions are the following:


       ceil(x) => rounds the number x up to the nearest integer


       floor(x) => rounds the number x down to the nearest integer


       trunc(x) => the value of x truncated to an integer


       pow(x, y, z) => returns the value of (x ** y) % z. z is optional


       hypot(x1, x2, x3, ..,xn) => calculates the Euclidean form. For n-dimensional cases, the coordinates passed are assumed to be like (x1, x2, x3, …, xn). It is calculated by sqrt(x1*x1 + x2*x2 +x3*x3 …. xn*xn).


       factorial(x) => returns the factorial of a number, it only accepts positive integers. The factorial of a number is the sum of the multiplication, of all the whole numbers, from our specified number down to 1. E.x the factorial of 4 would be 4 x 3 x 2 x 1 = 24


Which of the following expressions return False?

A.print(math.hypot(9,12) == math.sqrt(225))

B.print(math.trunc(7.3) == math.floor(7.4))

C.print(math.floor(10.8) > math.ceil(10.8))

Answer: C

Which of the following answers is correct for the statement:

import math
math.ceil(math.pi)

3.0

4.0

4

3

Answer: 4

def is_triangle(a, b, c):
    if math.pow(a, 2) + math.pow(b,2) == math.pow(c,2):
        return True
    return False

print("The program checks if three sides form a right-angled triangle.")
inp1 = input("Enter first side value: ")
inp2 = input("Enter second side value: ")
inp3 = input("Enter third side value: ")
print("Is triangle?", is_triangle(inp1, inp2, inp3))

# Do any necessary imports here

# Complete the function
def circle_area(r):


inp = float(input("Enter the radius of a circle:"))
print("Area of circle =", circle_area(inp))

Answer:
def circle_area(r):
    return 3.14 * r * r


inp = float(input("Enter the radius of a circle:"))
print("Area of circle =", circle_area(inp))


"""