"""
What may happen if our Python program does not handle errors?

The console returns errors
Our program stops running and errors appear in the console
Both of the above
None of the above

Answer: Both of the above

What mechanisms does Python provide to deal with errors?


A. Built-in error functions
B. Built-in error methods
C. Exception raising
D. The special keywords 'try', 'exception'
E. The special variables try, 'exception'

Answer: C

What is the order of the try/except code blocks?

try/except codeblocks are executed one after the other
the except codeblock only gets executed if the try codeblock fails
the try codeblock only gets executed if the except codeblock runs without errors

Answer: the except codeblock only gets executed if the try codeblock fails

We can build specific exceptions for certain errors.

False
True

Answer: True

When does Python throw a ValueError?

for wrong values passed in operations and functions
for wrong data types passed in operations and functions
for errors related to variables in our code
for wrong string and numeric data types
for errors related to the extension of our python files

Answer: for wrong data types passed in operations and functions

How many exceptions branches can we have in a try/except block?

Up to three
More than one as long as each branch has a unique name
No limit

answer is more than one as long as each branch has a unique name.

How many exceptions branches may get executed during errors?

As many as our exception branches

At most one

Depends on how many different types of errors we have

Answer: At most one

What is the error thrown by the following code snippet?


>>> 3 // 0 == 3 % 3

ValueError
TypeError
ZeroDivisionError
IndexError

Answer: ZeroDivisionError

What is the error thrown by the following code snippet?


>>> list1 = [1, 2, 3, 4]
>>> list1[4]

No error
TypeError
ValueError
IndexError

Answer: IndexError

What is the output of the following code block?

try:
      print("my_string"[1/0])
except IndexError:
      print("index error")
except ZeroDivisionError:
      print("zero error")
except:
      print("other error")


zero error
other error
other error
index error


Answer: zero error

Which of the following code snippets would raise an unhandled exception?


A.

try:
      x = y + 1
except NameError:
      print("y is not defined")

B.

try:
      x = 'seasalt'[7]
except IndexError:
      print("No character found in that index")

C.

try:
      x = 'y' + 1
except ValueError:
      print("y is not a number value")


C  - answer is C.

When does the unnamed exception run?


A. When there is no dedicated named exception


B. After all other named exceptions


C. When it is the only exception branch



A, C - answer is this.

What happens when an exception branch is executed?

None of the above
No other branch after or before that is executed
Next exception branches shall run if they are related to the error
Previous branches shall run if they are related to the error

Answer: No other branch after or before that is executed

A recap of the exception branches order:
try:
      #
      # Some code
      #
except ExceptName1:
      # Error handling related to Name1
except ExceptName2:
      # Error handling related to Name2
except:
      # Any other issues fall here

# Some more code

Which of the following code lines is the correct one if we want to break out of the while loop?

flowers = ['roses', 'daisies', 'dahlias', 'camellias']
i = 0
while True:
    try:
        print(flowers[i])
        i += 1
    ... :
        break

else


if i == 4
except ValueError
except IndexError -

Answer : IndexError because its keep on running No break has been defined.


Open the file handle_error.py, and rewrite the code so that all if/elif/else statements are replaced by a try/except code block. Use two named exceptions and one unnamed.


CheckCompleteIncomplete

def division():
    global number1, number2
    try:
        number1 = input("Enter a number: ")
        number2 = input("Enter another number: ")
        if not (number1.isnumeric() and number2.isnumeric()):
            raise ValueError("Please enter valid numbers.")
        if float(number2) == 0:
            raise ZeroDivisionError("Zero division error, please try again.")
        else:
            print(float(number1) / float(number2))
    except ValueError as ve:
        print(ve)

    except ZeroDivisionError as zde:
        print(zde)
    except:
        print("Hmm, something went wrong, try again.")


division()


What are the abstract exceptions?

General exceptions that they include other exceptions
Exceptions that we call without a specific name
Exception functions that take no arguments
ZeroDivisionError is a special case of:

answer is 1 General exceptions that they include other exceptions.


Why shouldn't we put more general exceptions before specific exceptions?

Because the tree of exceptions dictate us to do so
Because we risk having both general and specific exceptions raised
Because the specific exceptions would never execute and become useless

Answer: Because we risk having both general and specific exceptions raised

In the following snippet, which exception could replace the existing one?

try:
    y = 5 / 0
except ZeroDivisionError:
    print("Can't divide with zero.")

BaseException --> answer is this.
ValueError
RuntimeError

When can we use the raise keyword?

A. Inside the try block together with a named exception
B. Inside any try/except block
C. Inside the except block, but unnamed
D. Inside the try or except block with a named exception

Answer: Inside the try block together with a named exception

What is common between AssertionError and ArithmeticError?

They both have more specific error cases

Both options
None of the options
They both stem from Exception --> answer is this.


What are the specific exceptions included in the LookupError?


A. TypeError
B. KeyError
C. ValueError
D. IndexError

Answer: keyError and IndexError

What is the output of the following code snippet?

try:
    z = 3 // 0
except ZeroDivisionError:
    print("Zero won't work!")
except ArithmeticError:
    print("We have a problem!")

Zero won't work!
We have a problem!
Zero won't work!
We have a problem!

Answer: zero won't work!

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

Answer: C

Open the file function_error.py and include the error handling inside the function rather than invoking it from outside.


def err_fun():

    num = input('enter a number')
    try:
         return 3 / num

    except ZeroDivisionError:
        print("Cannot divide with zero!")

Open the file captcha.py and rework the code to use the assert keyword and the AssertionError instead of the if/else statements.


Keep the unnamed exception as it is.

def captcha():
    try:
        inp = int(input("3 + 16? "))
        if inp == 19:
            print("Correct!")
        else:
            print("Wrong input, please try again.")
    except Exception:
        print("Hmm, something went wrong, please try again.")

captcha()

"""