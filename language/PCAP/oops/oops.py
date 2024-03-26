"""
**********************************************************************************************************************
What is polymorphism in Python OOP?

The ability to invoke superclass methods from the subclass


The ability of the subclass to override superclass methods


None of the above


The ability to define methods in a class

Answer: The ability of the subclass to override superclass methods
Polymorphism is the ability of the subclass to override superclass methods.
Polymorphism is the ability of the subclass to override superclass methods with the same name.
Polymorphism is the ability of the subclass to override superclass methods with the same name and different parameters.
Polymorphism is the ability of the subclass to override superclass methods with the same name and different parameters and different return values.

What happens when we override a method in a subclass?

We break out of the inheritance
An error is raised
The overridden and the new method co-exist
We alter the behavior of the superclass

Answer: We alter the behavior of the superclass
When we override a method in a subclass, we alter the behavior of the superclass.
When we override a method in a subclass, we alter the behavior of the superclass with the same name.
When we override a method in a subclass, we alter the behavior of the superclass with the same name and different parameters.
When we override a method in a subclass, we alter the behavior of the superclass with the same name and different parameters and different return values.

What is the difference between inheritance and composition?

Both of the above are correct ,
None of the above are correct
Composition can use other objects (derived from other classes or not) and implement the desired parts of the other objects' properties
Inheritance extends a class's capabilities by adding new components and modifying existing ones

Answer: Both of the above are correct,
Both of the above are correct.
Inheritance extends a class's capabilities by adding new components and modifying existing ones.
Composition can use other objects (derived from other classes or not) and implement the desired parts of the other objects' properties.

what is the composition?
Composition is a way to combine simple objects or data types into more complex ones.
Composition is a way to combine simple objects or data types into more complex ones by using the properties of the simple objects or data types.
Composition is a way to combine simple objects or data types into more complex ones by using the properties of the simple objects or data types and by adding new properties.
Composition is a way to combine simple objects or data types into more complex ones by using the properties of the simple objects or data types and by adding new properties and modifying existing ones.

How does Python solve the diamond problem?

Python doesn't handle this, we need to be careful with multiple subclassing and composition

Python throws a Class Exception
Python uses the MRO check and throws a TypeError
Python throws a TypeError

Answer: Python uses the MRO check and throws a TypeError
Python uses the MRO check and throws a TypeError.
Python uses the MRO check and throws a TypeError when it detects the diamond problem.
Python uses the MRO check and throws a TypeError when it detects the diamond problem in multiple inheritance.
Python uses the MRO check and throws a TypeError when it detects the diamond problem in multiple inheritance and composition.

Assuming the code below has been executed, which of the following class declarations are correct?


class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D(C, B):
    pass


A. class Mixed (A, B): pass


B. class Mixed_2(C, A): pass


C. class Mixed_3(D, B): pass


D. class Mixed_4(B, C): pass


Answer: B, C # class Mixed_2(C, A): pass, class Mixed_3(D, B): pass
The Mixed_2 class inherited from the C class and from the A class.
The Mixed_2 class inherits from the C class and from the A class which inherits from the B class.
The Mixed_3 class inherits from the D class and from the B class.
The Mixed_3 class inherits from the D class and from the B class which inherits from the C class.

What is the output of the code below?


class A:
    def make(self):
        pass
    def add(self):
        return self.make()

class B(A):
    def add(self):
        return 1

class C(B):
    pass

a = A()
b = B()
c = C()
print(c.add() + a.add())

Answer: TypeError
The C class inherits from the B class which inherits from the A class.
The C class inherits from the B class which inherits from the A class which has the add() method.
The C class inherits from the B class which inherits from the A class which has the add() method that calls the make() method.
The C class inherits from the B class which inherits from the A class which has the add() method that calls the make() method which is not defined in the C class. # make() method which is not defined in the C class

why type error?
The C class inherits from the B class which inherits from the A class which has the add() method that calls the make() method which is not defined in the C class.

What is the output of the following code?
class Upper:
    def upper(self):
        print("upper")

class Left(Upper):
    def middle(self):
        print("left")

class Right(Upper):
    def middle(self):
        print("right")

class Down(Upper, Left, Right):
    def down(self):
        print("down")

object = Down()
object.down()
object.middle()
object.upper()

TypeError


down

right

upper


down

left

upper

Answer: TypeError # TypeError
TypeError: Cannot create a consistent method resolution
order (MRO) for bases Upper, Left, Right

Open the file layout.py, and complete the code so that the class Layout takes as arguments the class Position and calculates a textbox area.


Follow the instructions in the comments inside the file.

class Position:
    def __init__(self, x=0.0, y=0.0):
        #
        #

    def get_x(self):
        #

    def get_y(self):
        #


class Layout:
    def __init__(self, start, coord_x, coord_y):
        self.position1 = start
        self.position2 = coord_x
        self.position3 = coord_y

    def textbox(self):
        # Calculate length and breadth from the coordinates passed in the class
        #
        #
        area = length * breadth
        return area


layout = Layout(Position(0, 0), Position(3, 0), Position(0, 5))
print(layout.textbox())
class Position:
    def __init__(self, x=0.0, y=0.0):
        #
        #

    def get_x(self):
        #

    def get_y(self):
        #


class Layout:
    def __init__(self, start, coord_x, coord_y):
        self.position1 = start
        self.position2 = coord_x
        self.position3 = coord_y

    def textbox(self):
        # Calculate length and breadth from the coordinates passed in the class
        #
        #
        area = length * breadth
        return area


layout = Layout(Position(0, 0), Position(3, 0), Position(0, 5))
print(layout.textbox())


class Position:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Layout:
    def __init__(self, start, coord_x, coord_y):
        self.position1 = start
        self.position2 = coord_x
        self.position3 = coord_y

    def textbox(self):
        # Calculate length and breadth from the coordinates passed in the class
        length = abs(self.position2.get_x() - self.position1.get_x())
        breadth = abs(self.position3.get_y() - self.position1.get_y())
        area = length * breadth
        return area

layout = Layout(Position(0, 0), Position(3, 0), Position(0, 5))
print(layout.textbox())


Open the file composition.py, and complete the code, so that the Train and Bus classes can be passed as parameters of the class Transport.


Follow the instructions in the file's comments.

Expected output:

A train uses diesel

A bus uses electricity

A train covers 600Km in 3 hours.

A bus covers 240Km in 3 hours.


CheckCompleteIncomplete

class Train:
    def get_fuels(self):
        return 'diesel'

    def get_speed(self):
        return "200Km/hr"

    def get_type(self):
        return "A train"


class Bus:
    def get_fuels(self):
        return 'electricity'

    def get_speed(self):
        return "80Km/hr"

    def get_type(self):
        return "A bus"


class Transport:
    # Add the constructor with a transport argument

    def travel(self):
        # Get fuels from transport object
        fuels = # complete the code
        # complete code below so outcome is:
        # A bus uses diesel / or A train uses electricity
        return # complete code

    def distance_covered(self, hrs):
        # Get speed from the transport object
        # use a string method to delete 'Km/hr' part from speed
        # and return an integer
        km = # complete the code
        return (
            # complete code so outcome is:
            # A train covers <km> in <hrs> hours.
            # or A bus covers <km> in <hrs> hours.

        )


train = Transport (Train())
bus = Transport(Bus())

print(train.travel())
print(bus.travel())
print(train.distance_covered(3))
print(bus.distance_covered(3))


class Train:
    def get_fuels(self):
        return 'diesel'

    def get_speed(self):
        return "200Km/hr"

    def get_type(self):
        return "A train"


class Bus:
    def get_fuels(self):
        return 'electricity'

    def get_speed(self):
        return "80Km/hr"

    def get_type(self):
        return "A bus"


class Transport:
    def __init__(self, transport):
        self.transport = transport

    def travel(self):
        fuels = self.transport.get_fuels()
        return f"{self.transport.get_type()} uses {fuels}"

    def distance_covered(self, hrs):
        speed = self.transport.get_speed().replace("Km/hr", "")
        speed = int(speed)
        distance = speed * hrs
        return f"{self.transport.get_type()} covers {distance}Km in {hrs} hours."


train = Transport(Train())
bus = Transport(Bus())

print(train.travel())  # A train uses diesel
print(bus.travel())  # A bus uses electricity
print(train.distance_covered(3))  # A train covers 600Km in 3 hours.
print(bus.distance_covered(3))  # A bus covers 240Km in 3 hours.

**********************************************************************************************************************

Can a try/except block have an else statement too?

No, else statements need to be preceded with if/elif statements
Yes, after the try branch
Yes, after the first except branch
Yes, after the last except branch

Answer: Yes, after the last except branch
A try/except block can have an else statement too.
A try/except block can have an else statement too after the last except branch. # after the last except branch

In a try/except block, we can also have a ‘finally’ branch.


What is true of the following statements?

the finally branch must come after the try branch
the finally branch must be the last branch of our code with a try/except block
When we have a try/except block followed by else, we cannot have a finally branch
the finally branch doesn't get executed if there is an exception raised

Answer: the finally branch must be the last branch of our code with a try/except block
The finally branch must be the last branch of our code with a try/except block.


the finally branch doesn't get executed if there is an exception raised

What type of data are Exceptions?

Dictionaries
Variables
Classes
Strings

Answer: Classes # Classes
Exceptions are classes.
Exceptions are classes that inherit from the Exception class.
Exceptions are classes that inherit from the Exception class which inherits from the BaseException class.
Exceptions are classes that inherit from the Exception class which inherits from the BaseException class which inherits from the object class.

What is the as keyword used for in Python?

an alias for Exceptions
a metaphor for the exception branch
an alias for various data types such as modules, classes, exceptions
an alias for importing modules only

Answer: an alias for various data types such as modules, classes, exceptions
The as keyword is used for an alias for various data types such as modules, classes, exceptions.
The as keyword is used for an alias for various data types such as modules, classes, exceptions, and variables.
The as keyword is used for an alias for various data types such as modules, classes, exceptions, and variables in import statements.
The as keyword is used for an alias for various data types such as modules, classes, exceptions, and variables in import statements and in try/except blocks.   # in import statements and in try/except blocks

Which of the following exception classes can replace the RecursionError?

Note: for the hierarchy of exceptions visit:

https://docs.python.org/3/library/exceptions.html#exception-hierarchy

A.
LookupError
B.
_DeadlockError
C.
RuntimeError
D.
BaseException

Answer: C, D # RuntimeError, BaseException
The RuntimeError exception class can replace the RecursionError exception class.
The BaseException exception class can replace the RecursionError exception class.
The RuntimeError exception class can replace the RecursionError exception class which inherits from the BaseException exception class.

What is the output of the following code?

def division(number):
    try:
        number = 1 / number
    except ZeroDivisionError:
        print("Zero is not allowed")
        return None
    else:
        print("Yes! We have an outcome")
        return number

print(division(4))
print(division(0))

Answer: Yes! We have an outcome, 0.25; Zero Division is not allowed, None
The division() function returns the number if it is not zero.
The division() function returns the number if it is not zero and prints "Yes! We have an outcome".
The division() function returns the number if it is not zero and prints "Yes! We have an outcome" and prints "Zero Division is not allowed" if the number is zero.
The division() function returns the number if it is not zero and prints "Yes! We have an outcome" and prints "Zero Division is not allowed" if the number is zero and returns None.

What is the output of the following code?


try:
    i = int("apple")
except Exception as e:
    print(e)
    print(e.__str__())


Answer: invalid literal for int() with base 10: 'apple', invalid literal for int() with base 10: 'apple'
The exception object is printed.
The exception object is printed and its string representation is printed.
The exception object is printed and its string representation is printed with the __str__() method.
The exception object is printed and its string representation is printed with the __str__() method and with the print() function.

Which error is raised with the following code?

>>> var = 'A4'
>>> num = int(var)

ArithmeticError
ValueError
TypeError

Answer: ValueError
The ValueError is raised with the following code because the int() function cannot convert the string 'A4' to an integer.
The ValueError is raised with the following code because the int() function cannot convert the string 'A4' to an integer because it contains a letter. and not number

In which of the following code snippets would the e.args actually print something?


Note: The object's property named args (a tuple) stores all arguments passed to the object's constructor.

A.
try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ' ,end=' : ')
    print(e.args)

B.

try:
    raise Exception("error1, error2")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print(e.args)

C.

try:
    raise Exception("error1", "error2")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    print(e.args)

Answer: B, C
The e.args actually print something in the code snippets B and C.


Which of the following code snippets won't raise an unhandled exception?

A.
try:
    x = y + 1
except NameError, SystemError:
    x = y + 1
else:
    print(x)

B.

try:
    x = y + 1
except (NameError, SystemError):
    y = y + 1
else:
    print(x)


C.

try:
    x = y + 1
except (NameError, SystemError):
    y = 1
else:
    print(x)

Answer: C # C
The code snippet C won't raise an unhandled exception.
The code snippet C won't raise an unhandled exception because the y variable is defined in the except branch.
The code snippet C won't raise an unhandled exception because the y variable is defined in the except branch and the x variable is defined in the else branch.
The code snippet C won't raise an unhandled exception because the y variable is defined in the except branch and the x variable is defined in the else branch and the print() function is called in the else branch.

What would be printed in the following code snippet?

class E(Exception):
    def __init__(self, message):
        self. Message = message

    def __str__(self):
        return 'custom exception'

try:
    print('test')
    raise E('custom message')
except BaseException as e:
    print('error', e, e.message)
else:
    print('Done')

Answer: test, error custom exception custom message

Open the file emailerror.py, and build a custom exception based on the Exception class.

Follow the comments in the file for the exact instructions.

Note: Make use of the class method __str__ to return the new constructors’ arguments.

Expected output:
pending! wrong format!

class EmailError(ValueError):
    # complete the class by adding status
    # and message arguments for the constructor


email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError("pending!","wrong format!")
except EmailError as e:
    print(e)


class EmailError(Exception):
    def __init__(self, status, message):
        self.status = status
        self.message = message

    def __str__(self):
        return f"{self.status} {self.message}"

email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError("pending!", "wrong format!")
except EmailError as e:
    print(e)  # This will print "pending! wrong format!"


Open the file emailerror2.py, and build an exception class based on Exception. This time, complete the EmailError class so that we do not have to invoke it with any arguments. Make use of the class method __str__ to return the constructors’ arguments like in the previous exercise.

Expected output:

pending! wrong format!

class EmailError(ValueError):
    # Add your code here

email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError()
except EmailError as e:
    print(e)

class EmailError(Exception):
    def __str__(self):
        return "pending! wrong format"

email = "admin#libray.net"

Answer:
class EmailError(ValueError):
    def __str__(self):
        return "pending! wrong format!"

email = "admin#libray.net"
try:
    if "@" not in email:
        raise EmailError()
except EmailError as e:
    print(e)  # This will print "pending! wrong format!"


**********************************************************************************************************************


"""