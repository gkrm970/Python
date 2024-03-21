"""
Which of the following statements is correct when bellow code is executed?
>>> import platform
>>> print(len(dir(platform)))

the length of a list
all entities of platform
the length of a dictionary
KeyError

Answer: the length of a list


Which of the following statements are true?

dir(os) is list
dir(math) == list(dir(math))
dir(sys) == dir(os)
len(dir(platform)) is a numbers

Answer: all of the above

In the following code snippet, which outcome is expected to be True?


>>> number = [1, 2, 3]
>>> l = dir(number)
>>> d = dir()


A. 'append' in l
B. 'number' in l
C. 'number' in d

What does the module platform provide?

Information about the versions of Python available on our computer
Information on where the python files are stored
Information about our hardware, operating system and python interpreter

Answer: All of the above

The platform module in Python provides access to information about the computer's operating system, such as the operating system name, the system version, and the machine architecture. It can also be used to retrieve information about the Python interpreter, such as the version and the architecture.


If you would like to know, which OS (Operating System) you are on:

use platform.machine()
use platform.version()
use platform.system()

Answer: platform.system()


What is the difference between the platform's version and python_version functions?
answer :

A. version() returns the system's OS release version as a string
B. version() returns the system's OS release version as a tuple
C. python_version() returns the current interpreter's version as a string
D. python_version() returns all the python versions available in the system in a list

Answer: A, C

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

d.
>>> import platform
>>> print(platform.architecture())

Answer: d

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

Answer: B


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

Answer: D


What is the output of the following code?

from platform import python_version_tuple

for ver in python_version_tuple():
    print(ver, end=" ")

Answer: 3 11 4


Open the file platform_info.py, and complete the code so that the function returns first the
Operating System (OS), -->
then the architecture, and third the
Python version currently running on the system.


from platform import machine, system, python_version


def platform_info():
    user_os = platform.system()
    user_arch = platform.machine()
    user_arch1 = platform.architecture()
    user_python = platform.python_version()
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

Answer:
def platform_info(spec):
    if spec == "OS":
        return platform.system()
    elif spec == "architecture":
        return
    elif spec == "python_version":
        return platform.python_version()
    else:
        print("Sorry we couldn't answer your query")


inp = input("Enter one word in [OS, architecture, python]:  ")
print(platform_info(inp))

"""