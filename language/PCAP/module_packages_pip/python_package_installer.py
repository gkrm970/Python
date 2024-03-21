"""
Which of the following statements is not true?

A package contains modules -


A package can be installed


A package contains python files -


A package is an __init__.py file with functions

Answer: All of the above
Packages:

Contain modules: Yes, a package is a directory that groups related Python modules together. These modules can contain functions, classes, and variables that provide reusable code for your project.
Can be installed: You can install pre-written packages using package managers like pip. These packages often contain a collection of modules that offer functionality for various purposes (like data analysis, web development, machine learning, etc.).
Contain Python files: Yes, packages typically consist of Python files (.py extension) that define the modules within the package. These files contain the code that implements the functionality offered by the package.
Not just an init.py file: While an __init__.py file is often present in a package directory, it's not the sole definition of a package. This file can be used for initialization purposes or to define package-level attributes, but the actual functionality resides in the other Python files within the directory.
Key Points:

Packages promote code organization, reusability, and modularity.
They help manage large projects by keeping related code together.
You can create your own custom packages to organize your code.
Well-designed packages make code easier to understand, maintain, and share.



When a module is imported.:

all its entities are imported
all its entities are executed implicitly
its entities are ignored until explicitly called in the code
all its entities are executed explicitly

Answer: all its entities are imported


The recommended method is to import just the module. Why?

Because when we import a module's entities, they get executed and mess with our code
Because when we import a module's entities, we risk having namespace conflicts
Because the module's functions are imported faster in this way

Answer: all af the above


How can we prevent a module from executing its functions when imported in our file?

With the __name__ == '__module__' check
With the __name__ == '__main__' check

answer :
By importing specific functions instead of the whole module,
We cannot prevent it


What is the Python variable to store the name of a module?

__pycache__
__main__
__module__
__name__

Answer: __name__
# my_module.py
print(__name__)  # Output: "__main__"


Why do you need to add an __init__.py file when creating a package with some modules?
answer: To distinguish a package from a directory with modules

A. It is needed for uploading to PyPi and emailing the Python community
B. To add inside it any necessary code that needs to run upon the package modules' imports
C. To distinguish a package from a directory with modules
D. To add the licenses and your authorship information

Answer: B, C

There are two primary reasons why you need to add an init.py file when creating a package with some modules in Python:

Marking a Directory as a Package:

Python treats directories with an __init__.py file as packages. Without this file, it would simply see the directory as a regular folder containing Python files.
The __init__.py file acts as a signal to Python, indicating that this directory contains related modules that can be imported and used together as a cohesive unit.
Optional Initialization and Configuration:

Although not strictly required, the __init__.py file can be used for initialization purposes when the package is imported. This could involve:
Setting up global variables or constants for the package.
Defining custom logic that runs during package import.
Specifying which modules should be accessible when using from package import * (not recommended in general).
In summary:

The __init__.py file is essential for creating a package in Python.
It allows you to group related modules under a single namespace.
It can optionally be used for initialization tasks when the package is imported.
Benefits of Using Packages:

Organization: Packages help you organize your code into logical units, making large projects easier to manage and maintain.
Reusability: You can reuse modules across different parts of your application or even share them with others as reusable packages.
Namespace Management: Packages help to avoid naming conflicts, which can occur when modules from different directories have the same names.


How can we create a private value in Python?
answer: By adding two underscores before, e.g __value

A. By adding an underscore before and after, e.g _value_
B. By adding an underscore before, e.g _value
C. By adding two underscores before, e.g __value
D. By adding two underscores before and after, e.g __value__

Answer: C

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
22

Answer: 22

What does 'pip' stand for:

python install packager
pip installer for python
python installer for packages

Answer: pip installs for packages

Where can we find third-party python packages?
A. at py-shop
B. at PyPI repo
C. from our local machine with pip search <name of package>
D. from our local machine with pip list

Answer: at PyPI and at local machine with pip list



When we run 'pip install' which of the following is true?

it prompts the user to select a version for the package


it installs a specific version of a package depending on our Python version


it installs all versions of a package


it installs the newest version of a package

Answer: it install the newest version of a package

What does the 'pip list' do?

it lists all local packages
it lists all packages available in PyPi
it lists all pip commands
it lists all available updates for the installed packagesWhat does the 'pip list' do?

Answer: it lists all local packages


What is true of the pip command?

with the --system option we can install packages system-wide
with the --user option we can install packages to the user’s home directory without root privileges
with the --uninstall option we can remove packages
with the -U option we can uninstall packages

Answer: with the --user option we can install packages to the user’s home directory without root privileges


Use of pycache folder is to store the compiled bytecode of our modules.

What is inside the pycache files?
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

Answer: from puzzles import quizzes.quiz
Did you know that the PyPI repo is also referred to as the Cheese Shop? The analogy comes from a British entertainment show by Monty Python, a comedy group. In one of their sketches, we watch a failed visit to a cheese shop where there is no cheese in the stock. The Python language was named after Monty Python, since it was developed with the aim to be fun to work with, thus the official documentation’s tutorials often refer to spam and eggs (a reference to a Monty Python sketch) instead of the standard foo and bar.
Please keep in mind that while PyPI is a free place to fetch packages, you need to respect the licenses that come with the packages.


Imagine you have written some modules inside the directory /home/me/python-examples/my-module. You want to import some functions from ‘my-module’ to the python file my-function.py created in another directory, at /home/me/python-exercises/.
How can you make sure that you can import the module in my-function.py without errors?

By copying the 'my-module' inside the directory of the my-function.py and do 'import my-module'

By doing 'import home.me.python-examples.my-module' at the start of the 'my-function.py'
By doing 'import sys', 'sys.path.append("/home/me/python-examples/") and 'import my-module'
By copying the file my-function.py under the my-module directory



"""