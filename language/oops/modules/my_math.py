""" This is my_math module  where I have defined some math functions."""
import math
from builtins import print


# for name in dir(math):
#     print(name, end="\t")
#

# ceil()	Returns the smallest integer greater than or equal to a number.
# floor()	Returns the largest integer less than or equal to a number.
# trunc()	Returns the integer part of a number (no rounding).

print(math.ceil(5.4))
print(math.ceil(5.4))
print(math.ceil(5.4))

print(math.floor(5.1))
print(math.floor(5.9))
print(math.floor(5.0))
print(math.floor(-5.6))

print(math.trunc(5.9))
print(math.trunc(5.9))
print(math.trunc(5.9))


# factorial()	Returns the factorial of a number.
print(math.factorial(5))
print(math.factorial(6))

print(math.sqrt(16))
print(math.sqrt(25))

# Right-angle triangle
print(math.hypot(3, 4))
print(math.hypot(5, 12))
