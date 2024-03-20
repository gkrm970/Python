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


Which of the following expressions return True?

A.

print(math.hypot(9,12) == math.sqrt(225))


B.

print(math.trunc(7.3) == math.floor(7.4))


C.

print(math.floor(10.8) > math.ceil(10.8))


Which of the following answers is correct for the statement:


import math
math.ceil(math.pi)


3.0


4.0


4


3

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


What are pseudo-random numbers?



Numbers generated by algorithms that we cannot predict their sequence


Both of the above


Numbers coming from physical processes, which are not predictable

What does the random module do?



Generates actual random numbers


Generates either actual or pseudo numbers, based on the parameters


Generates pseudo-random numbers


All of the above

The module provides several functions, including:

- random(): returns a random float between 0 and 1.
- randint(a, b): returns a random integer between a and b (inclusive).
- randrange(start, stop[, step]): returns a randomly selected element from the range(start, stop, step).
- choice(seq): returns a random element from the given sequence.
- shuffle(seq): shuffles the elements in the given sequence randomly.

The random module is useful in a wide range of applications, including games, simulations, and cryptography.

What is the difference between the randrange and randint methods?


A. randrange() returns a float while randint() returns an integer


B. randrange() requires two parameters


C. randint() may return a value equal to the left and right parameter


D. randrange() may take a step parameter

What is the output of the following print statements?


>>> import random
>>> random.seed(12)
>>> print(random.random())
>>> random.seed(12)
>>> print(random.random())

What is the output of the following code?


>>> from random import randint
>>> print(str(randint(0, 1)) + str(randint(0, 1)), end='')

01 or 10


TypeError


0


10, 00, 01 or 11


What is the output of the following code?


>>> from random import randrange
>>> randrange(0, 1))

Either 0 or 1


ValueError


Only 0


Only 1

What is the output of the following code?


>>> from random import randrange
>>> randrange(0, 20, 5)

it would return one of the numbers in [0, 5, 10, 15, 20]


it would return one of the numbers in [0, 5, 10, 15]


it would return one of the numbers in [5, 10, 15]


it would return one of the numbers in [5, 10, 15, 20]

What is the output of the following code snippet?


>>> from random import choice
>>> name = 'Yoon'
>>> print(choice(name))

one of the name characters but the first


Error


one of the name characters


one of the name characters but the last

What is the output of the following code snippet?


>>> from random import sample
>>> teachers = ('Pak', 'Kim', 'Yoon')
>>> print(sample(teachers))

TypeError: sample() requires a list argument


two of the names in the tuple


one of the names in the tuple


TypeError: sample() missing 1 required positional argument:

Open the file cards.py, and write a function that takes as arguments a list of suits and a list of ranks. Inside the function create the list of the deck and return a random group of 4 cards.


The output should be in the format of <rank>-<suit>, e.g Jack-Hearts


# Add imports here


# Complete the function
def cards_sample(suits, ranks):



suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
ranks = [i for i in range(1, 11)] + ['Jack', 'Queen', 'King']

print(cards_sample(suits, ranks))

What methods does Python provide for printing all entities specific to a module?



The list module


The doc module


The dir module

What date type will get printed where dir module is used?
answer: list of strings containing the names defined by the module and the names of the attributes of the module itself (as string)
print(dir(math))
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

when we use the dir() without passing an argument then
answer: it returns the names in the current scope (global scope if called outside a function), and the names of the attributes of the module itself (as string)

What will the following code return if executed?


>>> import platform
>>> print(len(dir(platform)))

the length of a list


all entities of platform


the length of a dictionary


KeyError

Which of the following statements are true?



dir(os) is list


dir(math) == list(dir(math))


dir(sys) == dir(os)


len(dir(platform)) is a list of numbers

In the following code snippet, which outcome is expected to be True?


>>> number = [1, 2, 3]
>>> l = dir(number)
>>> d = dir()


A. 'append' in l


B. 'number' in l


C. 'number' in d


What does the module platform provide?
answer



Information about the versions of Python available on our computer


Information on where the python files are stored


Information about our hardware, operating system and python interpreter

If you would like to know, which OS (Operating System) you are on:
answer



use platform.machine()


use platform.version()


use platform.system()


What is the difference between the platform's version and python_version functions?
answer :

A. version() returns the system's OS release version as a string


B. version() returns the system's OS release version as a tuple


C. python_version() returns the current interpreter's version as a string


D. python_version() returns all the python versions available in the system in a list



A, D


A, C


B, C


B, D

Which of the following code snippets would return the architecture of your system?


A.

>>> import platform
>>> print(platform.system())

B.

>>> import platform
>>> print(platform.machine())

C.

>>> import platform
>>> print(platform.version())


B


C


A

Which of the following code snippets may return 'CPython'?
answer :


A.

>>> import platform
>>> print(platform.processor())


B.

>>> import platform
>>> print(platform.python_implementation())


C.

>>> import platform
>>> print(platform.python_version())


D.

>>> import platform
>>> print(platform.version())


D


A


B


C

Which of the following code snippets would return the version of the Operating System?


A.

>>> import platform
>>> print(platform.processor())


B.

>>> import platform
>>> print(platform.system())


C.

>>> import platform
>>> print(platform.machine())


D.

>>> import platform
>>> print(platform.version())


C


A


B


D

What is the output of the following code?


from platform import python_version_tuple

for ver in python_version_tuple():
    print(ver, end=" ")

C Python


python 3 9 0


3 9 0


3 8 0

Open the file platform_info.py, and complete the code so that the function returns first the
Operating System (OS), -->
then the architecture, and third the
Python version currently running on the system.


from platform import machine, system, python_version


def platform_info():
    # user_os = platform.system()
    # user_arch = platform.machine()
    # user_python = platform.python_version()
    return user_os, user_arch, user_python


print(platform_info())

Open the file platform_info2.py, and write a function that takes one argument and returns the corresponding information of the user's platform depending on the user's input. Make use of the same methods as in the previous exercise.


from platform import machine, system, python_version

def ask_user_info(spec):
    # Complete the function
    #
    #
    #
    #
    #
    else:
        return "Sorry we couldn't answer your query"


print("Depending on your input we can show relevant info")
inp = input("Enter one of the words in [OS, architecture, python]: ")
print(ask_user_info(inp))


Which of the following statements is not true?



A package contains modules -


A package can be installed


A package contains python files -


A package is an __init__.py file with functions

When a module is imported.:
answer :



all its entities are imported


all its entities are executed implicitly


its entities are ignored until explicitly called in the code


all its entities are executed explicitly

The recommended method is to import just the module. Why?



Because when we import a module's entities, they get executed and mess with our code


Because when we import a module's entities, we risk having namespace conflicts


Because the module's functions are imported faster in this way


How can we prevent a module from executing its functions when imported in our file?



With the __name__ == '__module__' check


With the __name__ == '__main__' check
answer :



By importing specific functions instead of the whole module


We cannot prevent it

What is the Python variable to store the name of a module?



__pycache__


__main__


__module__


__name__

Why do you need to add an __init__.py file when creating a package with some modules?
answer: To distinguish a package from a directory with modules


A. It is needed for uploading to PyPi and emailing the Python community


B. To add inside it any necessary code that needs to run upon the package modules' imports


C. To distinguish a package from a directory with modules


D. To add the licenses and your authorship information



C, D


D, A


A, B


B, C

How can we create a private value in Python?
answer: By adding two underscores before, e.g __value



A. By adding an underscore before and after, e.g _value_


B. By adding an underscore before, e.g _value


C. By adding two underscores before, e.g __value


D. By adding two underscores before and after, e.g __value__



C, D


A, B


B, C


D, A

What would be the output of python module0.py with the following code inside the files module0.py, module1.py, and module2.py?


# module0.py
import module1
import module2

print(2)


# module1.py
import module2


# module2.py

for i in range(2):
      print(2, end="")

Error


2


2222 2


222

What does 'pip' stand for:



python install packager


pip installer for python


python installer for packages


pip installs packages

Where can we find third-party python packages?


A. at py-shop


B. at PyPI repo


C. from our local machine with pip search <name of package>


D. from our local machine with pip list



B, C


D, A


A, B


C, D


When we run 'pip install' which of the following is true?



it prompts the user to select a version for the package


it installs a specific version of a package depending on our Python version


it installs all versions of a package


it installs the newest version of a package


What does the 'pip list' do?



it lists all local packages


it lists all packages available in PyPi


it lists all pip commands


it lists all available updates for the installed packagesWhat does the 'pip list' do?



it lists all local packages


it lists all packages available in PyPi


it lists all pip commands


it lists all available updates for the installed packages

What is true of the pip command?



with the --system option we can install packages system-wide


with the --user option we can install packages to the user’s home directory without root privileges


with the --uninstall option we can remove packages


with the -U option we can uninstall packages


Use of pychace folder is to store the compiled bytecode of our modules.

What is inside the pyc files?
answer: The compiled bytecode of our modules

source code


a list of all packages installed


compiled code


the interpreter


Imagine that you just installed the package puzzles that contains a module quizzes, and you need to work with its quiz function. Which of the following statements is true?



from puzzles.quizzes import quiz


import quiz from quizzes from puzzles


import quizzes from quiz from puzzles


from puzzles import quizzes.quiz




Did you know that the PyPI repo is also referred to as the Cheese Shop? The analogy comes from a British entertainment show by Monty Python, a comedy group. In one of their sketches, we watch a failed visit to a cheese shop where there is no cheese in the stock. The Python language was named after Monty Python, since it was developed with the aim to be fun to work with, thus the official documentation’s tutorials often refer to spam and eggs (a reference to a Monty Python sketch) instead of the standard foo and bar.


Please keep in mind that while PyPI is a free place to fetch packages, you need to respect the licenses that come with the packages.


Imagine you have written some modules inside the directory /home/me/python-examples/my-module. You want to import some functions from ‘my-module’ to the python file my-function.py created in another directory, at /home/me/python-exercises/.


How can you make sure that you can import the module in my-function.py without errors?



By copying the 'my-module' inside the directory of the my-function.py and do 'import my-module'


By doing 'import home.me.python-examples.my-module' at the start of the 'my-function.py'


By doing 'import sys', 'sys.path.append("/home/me/python-examples/") and 'import my-module'


By copying the file my-function.py under the my-module directory


So far, we have seen how slicing can reverse a string. Another built-in function for doing so is the reversed(d). However, it works slightly differently. For example:


>>> reversed('shop')
>>> <reversed object at 0x7f41a310def0>
>>> for i in reversed('shop'):
...  print(i)
...
p
o
h
s


What is the output of the following code?


Note: try to solve it without using the terminal.


chars = "1234"
char = ""
for char in reversed(chars):
    char += char

print(char)


cc


4321


10


11


movie = "My    beautiful\n laundrette!"

# Create a list of the above string
# without extra spaces nor new lines
movie = movie.split()


# Use slices, concatenation and list index all in one line
# to join the elements of the list excluding the exclamation mark
movie = " ".join(movie[:-1]) + " " + movie[-1][:-1]

# Change the word laundrette to garden
movie = movie.replace('laundrette', 'garden')

# Capitalize only the first character of each word and print the new string
print(movie.title())

txt = ",$,,   chocolate   banana ice-cream..."

# Add more options in the strip()
txt = txt.strip(",$ .")

# Clear any space left and print the outcome
txt = " ".join(txt.split())
print(txt)

Which of the following code snippets return False?


A. 'Python' > 'python'


B. 'python2' < 'python'


C. 'python1' < 'python2'


D. 'pythOn' < 'python'



A, B


A, D


B, C


C, D

Which of the following code snippets return True?


A. 'cDe'.lower() < 'CD' -->

B. 'cdE' > 'cde'


C. 'cde'.upper() < 'cde'


D. 'Vanilla' == 'vanilla'.title()



D, A


B, C


C, D


A, B

Which of the following code snippets return True?


A. "in not" not in "is not there?"


B. "in" not in "many fruits in the basket"


C. "in not" in "not in time yet"


D. "not" in "… and whatnot"



D, A


C, D


B, C


A, B

Which of the following code snippets returns True?



'10' > '8'


'20' > '8'


'21' == '021'


'10' > '010'

What is the output of the following code snippet?


>>> '10' != 10
>>> '10' == 10
>>> '10' > 10


What is the output of the following code snippet?


>>> min('duck') > max('Duck')
>>> min('duck') > min('Duck')
>>> max('12 AB') == min('aBD')


What is the output of the following code snippet?


>>> val1 = '222'.count('2')
>>> val2 = list('mmm').count('m')
>>> val1 == val2

False


ValueError


TypeError


True

What is the output of the following code snippet?


Note: Try to guess without accessing the terminal.


>>> x = str(1 // 3)
>>> var = ""
>>> for i in x:
...    x = x + var
...
>>> print(x[-1])

0


None


' '


1


'0 '

What is the output of the following code snippet?


>>> l1 = 'manuals how-tos docs'.split()
>>> l2 = sorted(l1)
>>> print(l1 == l2)
>>> l3 = l1.sort()
>>> print(l1 == l2)
>>> print(l3 == l1)

True

True

False


True

False

True


False

True

False

What is the output of the following code snippet?


>>> l1 = 'manuals how-tos docs'.split()
>>> l2 = sorted(l1)
>>> print(l1 == l2)
>>> l3 = l1.sort()
>>> print(l1 == l2)
>>> print(l3 == l1)

True

True

False


True

False

True


False

True

False

how to convert string to integer in python ?
answer : int() function is used to convert string to integer in python

Which of the following methods and functions are for strings only?



append


sorted() --> sorted() function is used to sort the elements of a list in ascending order


extend()


sort()

Which of the following methods are for lists only?
answer: sort(), sum() and append() methods are for lists only


sorted()


count()


sum()


index()

Which of the following methods are for both strings and lists?



min()


find()


split()


sort()

Select the correct output of the following code:


>>> l1 = [1, 2, 3, 1, 2, 3, 2, 1]
>>> l1.index(3, 4)

1


5


2


TypeError

Did you know the list's sort() method has a reverse flag?


Can you guess the output of:


>>> l = [3.3, 2.225, 1, 9.30, 0.64, 5.5]
>>> l.sort(reverse=True)
>>> print(l)

9.3


0.64


[9.3, 5.5, 3.3, 2.225, 1, 0.64]


[0.64, 1, 2.225, 3.3, 5.5, 9.3]


Did you know the list's sort() method has a reverse flag?


Can you guess the output of:


>>> l = [3.3, 2.225, 1, 9.30, 0.64, 5.5]
>>> l.sort(reverse=True)
>>> print(l)

9.3


0.64


[9.3, 5.5, 3.3, 2.225, 1, 0.64]


[0.64, 1, 2.225, 3.3, 5.5, 9.3]

What is the expected output of the following code snippet?


>>> p_string = 'pumpkin soup'.count('p', 2)
>>> p_list = 'pumpkin soup'.split().count('p')
>>> str(p_string) > str(p_list)

True


False


TypeError


ValueError



Open the file cipher_encrypt.py, and complete the function that encrypts a string. The string comes from user input. Make use of a simple Caesar cipher algorithm, which shifts each letter of the alphabet to the next one.


For more info about Caesar's encryption, see here: https://en.wikipedia.org/wiki/Caesar_cipher

msg = input("Enter your message to encrypt: ")


def encrypt(msg):
    result = ""

    # iterate through the input msg
    for i in range(len(msg)):
        char = msg[i]
        # Check if character is alphanumeric

            # Check char is either Z or z and append A, a respectively




            # Else shift to the next letter


        # If char not alphanumeric just continue

        return result


print("Message to encrypt : ", msg)
print("Cipher: ", encrypt(msg))



Open the file cipher_decrypt.py, and complete the program which takes as input an encrypted text from the previous exercise and decrypts it.

cipher = input('Enter your encrypted message: ')


def decrypt(cipher):
    result = ""
    # Iterate through the cipher

        # Check whether character is alphanumeric

            # Check whether character is A or a, replace with Z or z




            # Else shift letter one below
            else:

        # Else append character as it is
        else:
            result += char

    return result


print("Cipher was :", cipher)
print("Decrypted message is :", decrypt(cipher))



"""
