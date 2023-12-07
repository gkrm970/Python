"""
What is the difference between procedural and Object-Oriented Programming (OOP)?


A. In procedural programming, the program is divided into data types and functions


B. In object programming, the data cannot use the methods


C. In object-oriented programming, the program is divided into objects, which include data and methods


D. In procedural programming, data are integrated with code



A, C


A, B


B, D


C, D

# Answer: AC
In object programming,
    the data can use the methods
    the program is divided into objects, which include data and methods
    the program is organized around objects that represent real-world entities.
    Objects are instances of classes, which define the properties (attributes) and behaviors (methods) of the objects.
    In OOP, the emphasis is on data encapsulation, inheritance, and polymorphism.
    Data encapsulation ensures that the data is hidden and can only be accessed through the methods of the object.
    Inheritance allows the creation of new classes based on existing classes, inheriting their attributes and behaviors.
    Polymorphism allows objects of different classes to be treated as objects of a common superclass,
     enabling code reuse and flexibility.

In procedural programming,
    data are not integrated with code but are kept separately in data structures
    the program is divided into data types and functions.
    Data and functions are kept separately, and
    data is not integrated with code but is kept separately in data structures.
    Procedural programming focuses on the step-by-step execution of procedures or functions to solve a problem.
    It does not involve the concept of objects or classes.


What keyword do we use in Python to define an object?



class


variable


init


method

# Answer: class
In Python, we use the class keyword to define a class.
The class is a blueprint for creating objects (instances of the class).
The class defines the attributes and methods of the objects.
The attributes are the data that the object holds.
The methods are the functions that the object can perform.

What is a class constructor?

A default variable for each object that is created on each instance of a class


A default method, which is called every time a new instance of a class is created


A default property that is set in the class

Answer: A default method, which is called every time a new instance of a class is created
constructor is a special method that is called every time a new instance of a class is created.
The constructor is used to initialize the object's attributes.
The constructor method is named __init__ (two underscores before and after init).
The constructor method can have parameters that are used to initialize the object's attributes.
The constructor method is optional.
If the class does not have a constructor, the object is created with the default values of the attributes.


What is a superclass in Python?



an abstract class from which other more specific objects can derive


the first class we create in our program


the first class we import in our program


specialized class, which derives from a more general class

Answer: an abstract class from which other more specific objects can derive

In Python, a superclass is an abstract class from which other more specific objects can derive.
The superclass is also called a base class.
The class that derives from a superclass is called a subclass. The subclass is also called a derived class.
The subclass inherits the attributes and methods of the superclass.
The subclass can override the superclass methods and add new methods.
The subclass can also add new attributes.
The subclass can be derived from another subclass, which is called a parent class.
The subclass can be derived from multiple parent classes, which is called multiple inheritance.

Which of the following statements are correct?


A. An object has a name, properties, and methods


B. An object is a class


C. An object is an instance of its class



A, B


A, C


B, C


All of the options

Answer: A, C

An object is an instance of its class.
An object has a name, properties, and methods.
The name of the object is the name of the variable that holds the object.
The properties of the object are the attributes of the class.
The methods of the object are the methods of the class.

How can we make a new object from an existing class 'Wagon'?



wagon = Wagon


wagon = class Wagon


wagon = __Wagon__


wagon = Wagon()

Answer: wagon = Wagon()
To create a new object from an existing class, we use the class name followed by parentheses.
The parentheses are used to call the constructor method of the class.
The constructor method is used to initialize the object's attributes.  # __init__

Which of the following class definitions is correct?


A.

class Text:
    def __paragraph__(self):
        self.paragraph = []


B.

class Text:
    def __init__(self):
        self.paragraph = []


C.

class Text:
    def __init__():
        self.paragraph = []


D.

class Text:
    def init(self):
        self.paragraph = []


B


A


D


C

Answer: B # __init__
The constructor method is named __init__ (two underscores before and after init).
The constructor method can have parameters that are used to initialize the object's attributes.
The constructor method is optional.
If the class does not have a constructor, the object is created with the default values of the attributes.

Which of the following class definitions would return a string when a new object is created?


A.

class Letter:
    def __init__():
        print("Do you like writing letters?")


B.

class Letter:
    def __init__(self):
        self.string = "Do you like writing letters?"
        return self.string


C.

class Letter:
    def __init__(self):
        self.string = "Do you like writing letters?"
        print(self.string)


B


A


C

Answer: C # __init__
The constructor method is named __init__ (two underscores before and after init).
The constructor method can have parameters that are used to initialize the object's attributes.
The constructor method is optional.
If the class does not have a constructor, the object is created with the default values of the attributes.

Choose the correct code option for making a private property for the following class:


A.

class Message:
    def __init__(self):
        self._plaintext = "My secret message"


B.

class Message:
    def __init__(self):
        self.__plaintext__ = "My secret message"


C.

class Message:
    def __init__(self):
        self.__plaintext = "My secret message"


A


C


B

Answer: C
To make a private property, we use two underscores before the property name. # __plaintext
what is double underscore property name called? # dunder
The private property can be accessed only from within the class.

what is the difference between a private and a public property?
A private property can be accessed only from within the class,
while a public property can be accessed from outside the class.

what is the difference between a private and a public method?
A private method can be accessed only from within the class,
while a public method can be accessed from outside the class.
how to make a private method?
To make a private method, we use two underscores before the method name. # __method_name
The private method can be accessed only from within the class.

what is mangling?
Mangling is a process of adding the class name to the private property or method name.
The private property or method name is prefixed with the class name and two underscores.
The private property or method name is also suffixed with two underscores.
Mangling is used to avoid name clashes between properties and methods of different classes.

Which of the following code snippets creates a class without any data or methods?



class My_class:

print()


class My_class:

return


class My_class:

pass


class My_class:

break

Answer: class My_class: pass
To create a class without any data or methods, we use the pass keyword.
The pass keyword is used as a placeholder for future code.
The pass keyword is used when a statement is required syntactically but no code needs to be executed.


Open the file bookshop.py, and complete the code so that the Book class has two new methods add_author and add_chapter. Also, add a new subclass BookMeta, which has a price property and a rating method. The price is related to the rating.


Follow the comments in the code for the exact actions these methods should perform.


Expected output:


Book info: Two Scoops of Django, 5 stars, 12.0

Book properties: {'title': 'Two Scoops of Django', 'author': 'Greenfeld', 'chapter_number': '3',
                'chapter_title': 'Async Views'}

BookInfo properties: {'title': 'Two Scoops of Django', 'author': None, 'info': True, 'price': 12.0, 'stars': 5}


class Book:
    def __init__(self, title):
        self.title = title
        self.author = None

    def add_author(self, name):
        author += name # add name to author


    def add_chapter(self, number, title):
        # add properties chapter_number and chapter_title
        cha



class BookInfo(Book):
    def __init__(self, title, price, info=False):
        Book.__init__(self, title)
        # add properties price and info
        ...
        ...
        self.stars = 0

    def rating(self, stars):
        try:
            # check if existing stars are less than new stars
            # and if new stars are greater than 4
            # adjust new price by a 20% increase
            ...
                ...
            # update the stars property
            ...
        except Exception as e:
            print(e, "Please try again")


# Create a book object titled 'Two Scoops of Django'
...
# Add the author 'Greenfeld'
...
# Add a chapter 3, with title 'Async Views'
...

# Create a book_info object titled 'Two Scoops of Django'
# with a price of 10, and info set to True
...
# Give the book_info a rating of 5 stars
...

print("Book info: ", end=" ")
# Print book_info's title, stars and price
print(
    ..., str(book_info.stars) + " stars",
    ..., sep=", "
)
# Print all properties of book and book_info objects
print("Book properties: ", ...)
print("BookInfo properties: ", ...)

**********************************************************************************************************************

An object's properties can be added or removed at any time.



False


True

Answer: True
An object's properties can be added or removed at any time.
The properties can be added or removed by assigning or deleting them.
The properties can be added or removed from within the class or from outside the class.

Instances of the same Class can have different properties because:



Each object is always invoked with different methods


Each object is always invoked with different values


None of the options are True


Some properties are added with class methods if those are invoked

Answer: Some properties are added with class methods if those are invoked
Instances of the same Class can have different properties because some properties are added with class methods if those are invoked.

One of the default attributes of a class, which comes along whenever we create a class, is the __dict__.


As we saw in the video, we can call it from the object:


my_obj.__dict__


but we can also call it from the class:


MyClass.__dict__


Another way besides __dict__ to check if an object or a class has a specific attribute is:



the built-in function 'hasattr()'


the private class attribute '_hasattr'


the built-in class attribute '__hasattr__'


the built-in class method 'hasattr()'

Answer: the built-in function 'hasattr()'
Another way besides __dict__ to check if an object or a class has a specific attribute is the built-in function hasattr().
The hasattr() function takes two arguments: the object and the attribute name.
The hasattr() function returns True if the object has the attribute, and False otherwise.


What is the expected output of the code snippet below?



class Flower:
    stem = 'green'
    def __init__(self, petals=True, thorns=False):
        self.petals = petals
        self.thorns = thorns

flower = Flower()
print(type(flower.__dict__))

<class 'str'>


<class 'tuple'>


<class 'list'>


<class 'dict'>

Answer: <class 'dict'>
The __dict__ attribute of an object is a dictionary that contains all the attributes of the object.

What is the expected output of the code snippet below?


class Flower:
    stem = 'green'
    def __init__(self, petals=True, thorns=False):
        self.__petals = petals
        self.__thorns = thorns

flower = Flower(False)
flower.__leaves = True
print(flower.__dict__)

{'_Flower__petals': False, '_Flower__thorns': False, '__leaves': True, stem: 'green'}


TypeError: __init__() missing 1 required positional argument: 'thorns'


{'_Flower__petals': False, '_Flower__thorns': False, '__leaves': True}


{'_Flower__petals': False, '_Flower__thorns': False, '_Flower__leaves': True}

Answer: {'_Flower__petals': False, '_Flower__thorns': False, '__leaves': True, stem: 'green'}

Which of the options would return a value and not an error after the following code snippet is executed:


class Flower:
    def __init__(self, petals=True, thorns=False):
        self.__petals = petals
        self.__thorns = thorns

flower = Flower()
flower.__leaves = True


A. flower.__thorns


B. flower._Flower__thorns


C. flower.Flower__thorns


D. flower.__dict__['__leaves']


E. flower.__class__.__leaves



B, D


C, E


A, C

Answer: B, D # flower._Flower__thorns, flower.__dict__['__leaves']


Assuming the following code is executed, which of the following options shall return True:


class A:
    Var = n = 1
    def __init__(self, val):
        self.val = value = 2

a = A(3)


A. 'n' in a.__dict__


B. 'val' in A.__dict__


C. 'Var' in A.__dict__


D. 'value' in a.__dict__


E. hasattr(a, 'n')



A, D


A, E


B, C


C, E

Answer: C, E # 'Var' in A.__dict__, hasattr(a, 'n')
The hasattr() function takes two arguments: the object and the attribute name.
The hasattr() function returns True if the object has the attribute, and False otherwise.

Choose the correct line of code from the options to complete the method update() of the class A.


The outcome of the final print statement in the below code should be [0,1,1]


class A:
    def __init__(self, list1):
        self.list1 = list1

    def get(self):
        return self.list1

    def put(self, x):
        self.list1.append(x)

    def update(self):
        ...

obj = A([0])
obj.put(1)
obj.update()
print(obj.get())

put(len(self.list1[]) -1)


self.put(self.list1)


self.put(self.get()[-1])

Answer: self.put(self.get()[-1])
The update() method should append the last element of the list to the list.
The last element of the list is the last element of the list returned by the get() method.
The last element of the list returned by the get() method is the last element of the list1 attribute.
The last element of the list1 attribute is the last element of the list1 attribute of the object.
The last element of the list1 attribute of the object is the last element of the list1 attribute of self.
The last element of the list1 attribute of self is the last element of the list1 attribute of self.

class A:
    var = 1

    def __init__(self, value=2):
        self.value = value


a = A()

# Use var or value inside the hasattr()
print(hasattr(a, ...) is True)
print(hasattr(A, ...) is True)
print(hasattr(A, ...) is False)
print(hasattr(a, ...) is True)

Answer: value, var, value, var # value, var, value, var
The hasattr() function takes two arguments: the object and the attribute name.
The hasattr() function returns True if the object has the attribute, and False otherwise.

Contrary to instance variables, class variables are stored outside any object, thus:


- they aren't shown in an object's __dict__


- they always return the same value in all class instances (objects), except if they are altered inside the class method. In the latter case, any new object that invokes that method, alters the class variable's value


- they can still be accessed with the hasattr() function and with object.<variable> notation


- they can be private like any other properties and accessed with '_ClassName__PrivatePropertyName' notation


Keeping in mind the above information, open the file obj_counter.py and complete the code so that a class variable counter works as a counter of new objects. Follow the comment for detailed instructions.


Expected output:


Object_2 first: 2

Object_3 first: 4

We have created 3 objects

Counter inside the ObjCounter is now 3

class ObjCounter:
    # set the private 'counter' here

    def __init__(self, val=1):
        # set a private property 'first' to val

        # add here the counter


object_1 = ObjCounter()
object_2 = ObjCounter(2)
object_3 = ObjCounter(4)

print("Object_2 first: ", ...)
print("Object_3 first: ", ...)

print("We have created", end=" ")
print(object_3..., "objects")

print("Counter inside the ObjCounter is now", end=" ")
print(ObjCounter.__dict__["..."])

*********************************************************************************************************************

What is a class method?



a function called before an object


another name for user-defined functions


Python's build-in methods


a function defined in the class

Answer: a function defined in the class
A class method is a function defined in the class.
The class method is defined with the @classmethod decorator.
example of class method:
    @classmethod
    def class_method(cls):
        pass

The class method takes the class as the first argument.
example of class method:
    @classmethod
    def class_method(cls):
        print(cls)

The class method is called with the class name followed by parentheses.
example of class method:
    @classmethod
    def class_method(cls):
        print(cls)
    class_method() # calling the class method

The parentheses are used to call the class method.
The class method is used to create factory methods.
example of class method:
    @classmethod
    def class_method(cls):
        return cls() # factory method to create objects of the class with different initial values
    obj = class_method() # calling the class method to create an object of the class with default initial values

The factory method is used to create objects of the class.
example of class method:
    @classmethod
    def class_method(cls):
        return cls() # factory method to create objects of the class with different initial values
    obj = class_method() # calling the class method to create an object of the class with default initial values

The factory method is used to create objects of the class with different initial values.

What are some of the differences between a function and a method?



All of the above options


methods are invoked from objects, functions are stand-alone


methods always take the parameter 'self' when is defined


methods are functions created inside a class

Answer: All of the above options
All of the above options are correct.
Methods are invoked from objects, functions are stand-alone.
Methods always take the parameter 'self' when is defined.
Methods are functions created inside a class.

What is true about the 'self' parameter?


A. It allows an object instance to access all its class properties and methods


B. We don't need to add it when we invoke the method, only on its class definition


C. We need to add it when we define and invoke the class methods


D. A keyword that refers to functions inside a class



A, B


D


C

Answer: A, B # It allows an object instance to access all its class properties and methods, We don't need to add it when we invoke the method, only on its class definition
The self parameter is a reference to the current instance of the class.
The self parameter is used to access the attributes and methods of the class.
The self parameter is used to invoke the methods of the class.
The self parameter is used to invoke the methods of the class from within the class.
The self parameter is used to invoke the methods of the class from outside the class.
The self parameter is used to invoke the methods of the class from within the class and from outside the class.

Which class method is always invoked when we create an object?



the constructor method of the class if it exists


the __dict__ attribute


None, we always need to call a class method explicitly


all the class methods are implicitly invoked

Answer: the constructor method of the class if it exists
The constructor method is always invoked when we create an object.
The constructor method is named __init__ (two underscores before and after init).
The constructor method can have parameters that are used to initialize the object's attributes.
The constructor method is optional.
If the class does not have a constructor, the object is created with the default values of the attributes.

Which of the following code snippets is correctly creating an object instance of the class Bean?


class Bean:
    def __init__(self, color)
        self.color = color


A.

greenbean = Bean.__init__("green")


B.

greenbean = Bean("green")


C.

greenbean = Bean()

greenbean.color = "green"


D.

greenbean = Bean(color="green")



B, D


A, C


All of the options


C, B, D

Answer: B, D # greenbean = Bean("green"), greenbean = Bean(color="green")
To create a new object from an existing class, we use the class name followed by parentheses.
The parentheses are used to call the constructor method of the class.
The constructor method is used to initialize the object's attributes.
The constructor method is named __init__ (two underscores before and after init).
The constructor method can have parameters that are used to initialize the object's attributes.
The constructor method is optional.

The class built-in __dict__ attribute shows all properties and methods of a class. We have seen previously that it may be invoked either with a class or with an object. The former reveals all class methods built-in and user-defined, and all class variables. In a class we can have private methods too, like we have private variables, see the example below:


class Space:
    def __init__(self, kind):
        self.kind = kind

    def public(self):
        print("public")

    def __private(self):
         print("private")

obj = Space()


Based on the Space class and the obj creation above, can you guess what the following code would return?


obj.public()

try:
    obj.__private()
except:
      print("inaccesible")

obj._Space__private()


public


inaccessible

private

public


inaccessible

error

public


private

private

Answer: public, inaccessible, private
The public() method is a public method.
The public() method can be accessed from outside the class.
The public() method can be accessed from outside the class with the object name followed by a dot and the method name.
The public() method can be accessed from outside the class with the object name followed by a dot and the method name and parentheses.

Which built-in method should we use in order to find the name of a superclass?



__name__


__module__


__dict__


__bases__

Answer: __bases__
The __bases__ attribute of a class is a tuple that contains the base classes of the class.
The __bases__ attribute of a class is a tuple that contains the superclasses of the class.
The __bases__ attribute of a class is a tuple that contains the parent classes of the class.
The __bases__ attribute of a class is a tuple that contains the derived classes of the class.
example of __bases__ attribute:
    class A:
        pass
    class B(A):
        pass
    print(B.__bases__) # prints (<class '__main__.A'>,) # tuple with the base class of B which is A class

Which of the following options would not return an error if the below code is executed:


class One:
    count = 1
    def __init__(self):
        self.first = True
    def add(self, num):
        self.count += num

one = One()


A. One.__bases__


B. one.__name__


C. one.__bases__


D. type(one).__name__



A, D


A, C


B, D

Answer: A, D # One.__bases__, type(one).__name__
The __bases__ attribute of a class is a tuple that contains the base classes of the class.
The __bases__ attribute of a class is a tuple that contains the superclasses of the class.
The __bases__ attribute of a class is a tuple that contains the parent classes of the class.
The __bases__ attribute of a class is a tuple that contains the derived classes of the class.
example of __bases__ attribute:
    class A:
        pass
    class B(A):
        pass
    print(B.__bases__) # prints (<class '__main__.A'>,) # tuple with the base class of B which is A class

The __name__ attribute of a class is a string that contains the name of the class.

Open the file modules.py, and complete the code so that the final print statements return the names of the functions' modules.

from os import wait, walk, write
from math import ceil, hypot
from random import randint

print(...)
print(...)
print(...)
print(...)
print(...)
print(randint.__module__)

# You should import modules and functions correctly.
import os
import math
import random

# Using the functions correctly.
print(os.wait)  # This will print the 'wait' function from the 'os' module.
print(os.walk)  # This will print the 'walk' function from the 'os' module.
print(os.write)  # This will print the 'write' function from the 'os' module.

# Using math functions.
print(math.ceil(3.5))  # This will print the ceiling value of 3.5.
print(math.hypot(3, 4))  # This will calculate the hypotenuse of a right triangle with sides 3 and 4.

# Using a random function.
print(random.randint.__module__)  # This will print the module of the 'randint' function.

Open the file flowers.py, and complete the code so the program creates a subclass Rose, a rose object and a default spring season. Print the rose's season and its class name.


Follow the instructions in the comments inside the file.

class Flower:
    def __init__(self, petals=False, thorns=False, color=False):
        self.petals = petals
        self.thorns = thorns
        self.color = color

    def has_color(self, color):
        if self.color:
            return "it has color " + color

    def has_thorns(self, thorns):
        if self.thorns:
            return "it has thorns"

    def season(self, blooming):
        return "it blooms in " + blooming


class Rose(Flower):
    def __init__(self, color):
        # Call the superclass init


    def season(self):
        # return the superclass season and pass as parameter 'spring'



rose = Rose("Red")

# print the rose season


# print the rose superclasses


class Flower:
    def __init__(self, petals=False, thorns=False, color=False):
        self.petals = petals
        self.thorns = thorns
        self.color = color

    def has_color(self, color):
        if self.color:
            return "it has color " + color

    def has_thorns(self):
        if self.thorns:
            return "it has thorns"

    def season(self, blooming):
        return "it blooms in " + blooming

class Rose(Flower):
    def __init__(self, color):
        # Call the superclass init
        super().__init(color=color)

    def season(self):
        # return the superclass season and pass 'spring' as a parameter
        return super().season("spring")

rose = Rose("Red")

# Print the rose season
print(rose.season())

# Print the rose superclass information
print(rose.has_color("Red"))
print(rose.has_thorns())

**********************************************************************************************************************

What is the default output when we call print(object)?



its class name


its properties


its module and its memory address location


its name

Answer: its module and its memory address location
The default output when we call print(object) is its module and its memory address location.
The default output when we call print(object) is its module and its memory address location in hexadecimal format.
The default output when we call print(object) is its module and its memory address location in hexadecimal format prefixed with 0x.

How can we give a unique identity to an object?



with the __module__() method


with the __name__() method


with the __str__() method


with the __init__() method

Answer: with the __str__() method   # __str__()
To give a unique identity to an object, we use the __str__() method.
The __str__() method is used to return a string representation of the object.
The __str__() method is used to return a string representation of the object that can be used to recreate the object.
The __str__() method is used to return a string representation of the object that can be used to recreate the object with the eval() function.

What is helpful with class inheritance?



We can build upon other classes for refined properties


Objects of the same class inherit the same properties


We can duplicate a class


We can invoke it as a method to pass attributes from one object to another

Answer: We can build upon other classes for refined properties
Inheritance is a mechanism that allows us to build upon other classes for refined properties.
Inheritance is a mechanism that allows us to build upon other classes for refined methods.
Inheritance is a mechanism that allows us to build upon other classes for refined attributes.
Inheritance is a mechanism that allows us to build upon other classes for refined properties, methods, and attributes.

How does the subclass inherit the constructor from the superclass?


Note: Consider the var below as a class parameter.



By adding the superclass name within parenthesis on its declaration


All of the above


By calling the superclass.__init__(self, var)


By calling super.__init__(var)

Answer: All of the above
The subclass inherits the constructor from the superclass by adding the superclass name within parenthesis on its declaration.

The subclass inherits the constructor from the superclass by calling the superclass.__init__(self, var).
The subclass inherits the constructor from the superclass by calling the superclass.__init__(self, var) from within the subclass.
The subclass inherits the constructor from the superclass by calling the superclass.__init__(self, var) from outside the subclass.  # outside the subclass
The subclass inherits the constructor from the superclass by calling the superclass.__init__(self, var) from within the subclass and from outside the subclass.


Which of the following code options return True if the following code snippet is executed?


class One:
    pass

class Two(One):
    pass

class Three(Two):
    pass

issubclass(Two, One)


All of the options


issubclass(One, One)


issubclass(Three, One)

Answer: All of the options # issubclass(Two, One), issubclass(One, One), issubclass(Three, One)
The issubclass() function takes two arguments: the subclass and the superclass.
The issubclass() function returns True if the subclass is a subclass of the superclass, and False otherwise.

Which of the following code options return False if the following code snippet is executed?


class One:
    pass

class Two(One):
    pass

one = One()
two = Two()

isinstance(one, One)


isinstance(two, One)


None of the options


isinstance(two, Two)

Answer: None of the options # isinstance(one, One), isinstance(two, One), isinstance(two, Two)
The isinstance() function takes two arguments: the object and the class.
The isinstance() function returns True if the object is an instance of the class, and False otherwise.

The is operator can check whether two objects refer to the same internal Python memory allocation.


Can you guess the output of the below code?


class ClassVal:
    def __init__(self, val):

        self.val = val


obj1 = ClassVal(1)
obj2 = ClassVal(2)
obj3 = obj1

print(obj1 is obj2)
print(obj2 is obj3)
print(obj3 is obj1)

False

False

True


False

False

False

Answer: False, False, True
The is operator can check whether two objects refer to the same internal Python memory allocation.

Open the file flavors.py, and replace the subclass constructor with the alternative super constructor invocation. Also, complete the code as per the instructions in the comments inside the file.


Expected output:


My favorite flavor is pistachio

class Desert:
    def __init__(self, flavor):
        self.flavor = flavor


class IceCream(Desert):
    def __init__(self, flavor):
        Desert.__init__(self, flavor)

    # Add a custom string representation


# Create an object IceCream with a pistachio flavor

print(obj)

class Desert:
    def __init__(self, flavor):
        self.flavor = flavor


class IceCream(Desert):
    def __init__(self, flavor):
        Desert.__init__(self, flavor)

    def __str__(self):
        return f"My favorite flavor is {self.flavor}"

# Create an object IceCream with a pistachio flavor
obj = IceCream("pistachio")

# Print the custom string representation
print(obj)

Open the file inheritance.py, and complete the code, so that the class variables are replaced with instance variables.


Keep their value the same so that the print statements still return 12 and 11.


Note: Use the super constructor in the subclass.

class Super:
    # Add your code here
    supVar = 11


class Sub(Super):
    # Add your code here
    subVar = 12


obj = Sub()

print(obj.subVar)
print(obj.supVar)

class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init()
        self.subVar = 12

obj = Sub()

print(obj.subVar)  # Should print 12
print(obj.supVar)  # Should print 11


**********************************************************************************************************************

Which of the following errors is thrown when Python cannot find a property in an object or in a class?



ValueError


ClassError


AttributeError


PropertyError

Answer: AttributeError # AttributeError
The AttributeError is thrown when Python cannot find a property in an object or in a class.

What is the difference between single and multiple inheritance?



The subclass inherits from more than one superclass at the same time

The subclass has a superclass which has also a superclass

In single inheritance we can opt not to include the parent's constructor while in multiple it is required

In multiple inheritance we need to call all previous superclasses in the subclass constructor

Answer: The subclass inherits from more than one superclass at the same time
In single inheritance, the subclass inherits from one superclass.
In multiple inheritance, the subclass inherits from more than one superclass at the same time.

How can the subclass override the superclass methods?



It cannot override it


By omitting the self parameter in the method definition


By invoking the method with different parameters from an object instance

By defining a method with the same name as in the superclass

Answer: By defining a method with the same name as in the superclass
The subclass can override the superclass methods by defining a method with the same name as in the superclass.
The subclass can override the superclass methods by defining a method with the same name as in the superclass and with different parameters.
The subclass can override the superclass methods by defining a method with the same name as in the superclass and with the same parameters.
The subclass can override the superclass methods by defining a method with the same name as in the superclass and with the same parameters and different return values.


We learned that in multiple inheritance Python scans from left to right. So in the following example, class B (called in the left) is scanned before class A (called in the right), and the B.fun takes precedence over A:


class A:
    def fun(self):
        return "left"

class B:
    def fun(self):
        return "right"

class AB(B, A):
    pass


Thus the following happens:


>>> ab = AB
>>> print(ab.fun())
>>> right


However, if the parents are subclasses themselves, then our code is prone to bugs. Take the case where one parent is a subclass of the other:


class A:
    def fun(self):
        return "left"

class B(A):
    def fun(self):
        return "right"

class AB(B, A):
    pass


Which AB.fun() would be called? Python offers the MRO algorithm, which creates a linear list of the inheritance hierarchy. Let’s create again the ab object with the above inheritance:


>>> AB.mro()
>>> [<class '__main__.AB'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
>>> ab = AB()
>>> print(ab.func())
>>> right


This order of inheritance works because there is no ambivalence in the hierarchy of the parents. All these may be hard to grasp when we just started learning Object Oriented Programming. But a rule of thumb to keep in mind is: we call the more specific first (in this case B), and the more general after (in this case A). Also keep in mind that when we subclassing from another class, we do so to create a more specific object from a parent object. While in our examples, this is not explicit, as we give the same methods in parent and child classes, in real life programming, inheritance only makes sense when we want to extend parent classes to more specific child classes.


Would you like to dig deeper about MRO? Here is the official docs:

https://www.python.org/download/releases/2.3/mro/

Based on the previous information, how does Python scan for object properties in the case of multiple inheritance?


A. The same as in the single inheritance, from bottom to top


B. In multiple inheritance, Python scans from left to right.


C. In multiple inheritance, if one of the superclasses is also a subclass, python also looks from bottom to top



C, B


A, B

Answer: C, B # In multiple inheritance, if one of the superclasses is also a subclass, python also looks from bottom to top, In multiple inheritance, Python scans from left to right.
In multiple inheritance, Python scans from left to right.
In multiple inheritance, Python scans from left to right and from bottom to top.

What is the output of the following code snippet?


class Class1:
    var = 1
    def fun(self):
        return 1

class Class2(Class1):
    var = 2
    def fun(self):
        return 2

class Class3(Class2):
    pass

obj = Class3()
print(obj.var, obj.fun())

1, 1


2, 2


1, 2


error

Answer: 2, 2
The Class3 class inherits from the Class2 class.
The Class3 class inherits from the Class2 class which inherits from the Class1 class.

What is the output of the following code snippet?


class A:
    var = 'A'
    var_left = "left"

    def fun(self):
        return self.var_left

class B:
    var = 'B'
    var_right = "right"

    def fun(self):
        return self.var_right

class AB(A, B):
    pass

obj = AB()
print(obj.var_left, obj.var_right, obj.var, obj.fun())

left right A left


left right B right

Answer: left right A left # left right A left
The AB class inherits from the A class and from the B class.

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



Both of the above are correct


None of the above are correct


Composition can use other objects (derived from other classes or not) and implement the desired parts of the other objects' properties


Inheritance extends a class's capabilities by adding new components and modifying existing ones

Answer: Both of the above are correct
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


A. class Mixed(A, B): pass


B. class Mixed_2(C, A): pass


C. class Mixed_3(D, B): pass


D. class Mixed_4(B, C): pass



C, D


A, B


B, C

Answer: B, C # class Mixed_2(C, A): pass, class Mixed_3(D, B): pass
The Mixed_2 class inherits from the C class and from the A class.
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

1


TypeError


ValueError

Answer: TypeError
The C class inherits from the B class which inherits from the A class.
The C class inherits from the B class which inherits from the A class which has the add() method.
The C class inherits from the B class which inherits from the A class which has the add() method that calls the make() method.
The C class inherits from the B class which inherits from the A class which has the add() method that calls the make() method which is not defined in the C class. # make() method which is not defined in the C class
why type error ?
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
or Answer: down, right, upper # down, right, upper

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


train = Transport(Train())
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

In a try/except block we can also have a ‘finally’ branch.


What is true of the following statements?



the finally branch must come after the try branch


the finally branch must be the last branch of our code with a try/except block


When we have a try/except block followed by else, we cannot have a finally branch


the finally branch doesn't get executed if there is an exception raised

Answer: the finally branch must be the last branch of our code with a try/except block
The finally branch must be the last branch of our code with a try/except block.

the finally branch doesn't get executed if there is an exception raised
The finally branch doesn't get executed if there is an exception raised.
The finally branch doesn't get executed if there is an exception raised in the try branch.
The finally branch doesn't get executed if there is an exception raised in the try branch or in the except branch.
The finally branch doesn't get executed if there is an exception raised in the try branch or in the except branch or in the else branch.

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



A, D


B, D


C, D


A, B


B, C

Answer: C, D # RuntimeError, BaseException
The RuntimeError exception class can replace the RecursionError exception class.
The BaseException exception class can replace the RecursionError exception class.
The RuntimeError exception class can replace the RecursionError exception class which inherits from the BaseException exception class.

What is the output of the following code?


def division(number):
    try:
        number = 1 / number
    except ZeroDivisionError:
        print("Zero Division is not allowed")
        return None
    else:
        print("Yes! We have an outcome")
        return number

print(division(4))
print(division(0))

Yes! We have an outcome


0.25

Zero Division is not allowed

0.25


Zero Division is not allowed

None

Yes! We have an outcome


0.25

Zero Division is not allowed

None

0.25


Zero Division is not allowed

Answer: Yes! We have an outcome, 0.25, Zero Division is not allowed, None
The division() function returns the number if it is not zero.
The division() function returns the number if it is not zero and prints "Yes! We have an outcome".
The division() function returns the number if it is not zero and prints "Yes! We have an outcome" and prints "Zero Division is not allowed" if the number is zero.
The division() function returns the number if it is not zero and prints "Yes! We have an outcome" and prints "Zero Division is not allowed" if the number is zero and returns None.

What is the output of the following code?


def division(number):
    try:
        number = 1 / number
    except ZeroDivisionError:
        print("Zero Division is not allowed")
        number = None
    else:
        print("Yes! We have an outcome")
    finally:
        print("Result is:", end=" ")
        return number

print(division(0))

Zero Division is not allowed


Result is: None

Zero Division is not allowed


Yes! we have an outcome

Result is: None

Zero Division is not allowed

Answer: Zero Division is not allowed, Result is: None
The division() function returns the number if it is not zero.
The division() function returns the number if it is not zero and prints "Yes! We have an outcome".
The division() function returns the number if it is not zero and prints "Yes! We have an outcome" and prints "Zero Division is not allowed" if the number is zero.
The division() function returns the number if it is not zero and prints "Yes! We have an outcome" and prints "Zero Division is not allowed" if the number is zero and returns None.
The division() function returns the number if it is not zero and prints "Yes! We have an outcome" and prints "Zero Division is not allowed" if the number is zero and returns None and prints "Result is:".

What is the output of the following code?


try:
    i = int("apple")
except Exception as e:
    print(e)
    print(e.__str__())

invalid literal for int() with base 10: 'apple'


invalid literal for int() with base 10: 'apple'

invalid literal for int()


invalid literal for int() with base 10: 'apple'

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
The ValueError is raised with the following code.
The ValueError is raised with the following code because the int() function cannot convert the string 'A4' to an integer.
The ValueError is raised with the following code because the int() function cannot convert the string 'A4' to an integer because it contains a letter.
The ValueError is raised with the following code because the int() function cannot convert the string 'A4' to an integer because it contains a letter and not a number.

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


B


A, B


B, C


C

Answer: B, C # B, C
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


C


A


B


None

Answer: C # C
The code snippet C won't raise an unhandled exception.
The code snippet C won't raise an unhandled exception because the y variable is defined in the except branch.
The code snippet C won't raise an unhandled exception because the y variable is defined in the except branch and the x variable is defined in the else branch.
The code snippet C won't raise an unhandled exception because the y variable is defined in the except branch and the x variable is defined in the else branch and the print() function is called in the else branch.

What would be printed in the following code snippet?


class E(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'custom exception'

try:
    print('test')
    raise E('custom message')
except BaseException as e:
    print('error', e, e.message)
else:
    print('Done')

custom message


Unhanddled exception

test


error custom exception custom message

Done

test


custom message

test


error custom exception custom message

Answer: test, error custom exception custom message
The code snippet prints test, error custom exception custom message.
The code snippet prints test, error custom exception custom message because the E class inherits from the Exception class.
The code snippet prints test, error custom exception custom message because the E class inherits from the Exception class and the __str__() method is overridden.
The code snippet prints test, error custom exception custom message because the E class inherits from the Exception class and the __str__() method is overridden and the message property is defined.


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
try:
    if "@" not in email:
        raise EmailError()
except EmailError as e:
    print(e)  # This will print "pending! wrong format"

**********************************************************************************************************************


"""