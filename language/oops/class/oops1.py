# Example1:


# def display1(name):
#     print(name)
#
#
# class MyClass:
#     def myfun(self):
#         pass
#
#     def display(self, name):
#         """
#         this is an Instance method because it has self-parameter.
#         """
#         print(name)
#
#
# mc1 = MyClass()  # object creation
# mc1.myfun()  # calling the method
# mc1.display("scott")  # john
# print(mc1.display("john"))
#

# Example2
# class MyClass:
#     def __init__(self, name):
#         self.name = name
#
#     def m1(self):
#         print("this is instance method...")
#         print(self.name)
#
#     @staticmethod
#     def m2(self, num2):  # static method we can give any name for self as parameter.
#         Print("this is static method...")
#         # Note: print(self.name) # we can't access instance variable inside the static method.
#         print(self + num2)  # when we declare and call the static method inside the class,
#         # we have to give value for self-parameter because it is not a class method.
#         Return self + num2
#
#
# mc = MyClass("gk")
# mc.m1()
# # Since instance method calling instance method using an object.
# mc.m2(100, 200)  # 100 200
# # Since static method calling static method directly using class not through an object.
# MyClass.m2(10, 20)  # 10, 20

# Example3:

# Class MyClass:
#     a, b = 10, 50 # this the class variables which are declared inside the class but outside the method.
#
#     Def __init__(self, book, pen="Blue pen"):
#         """
#         This is the constructor.
#         Constructor is used to declare the instance variables.
#         Instance variables are declared inside the constructor.
#         For instance variables, we have to use self.variableName.
#         Create instance variables and assign values to instance variables
#         and access instance variables anywhere in the class.
#         Create instance variables using the arguments which passed in the constructor.
#         And assign values as instance variables while creating an object, If not given the default values.
#         """
#         Self.book = book # This is the instance variable declared inside the constructor.
#         self.gk = "gk"
#         age = 30  # this is the local variable declared inside the constructor.
#         self.pen = pen
#
#     def add(self, d):
#         # a, b are class variable.when we use class variable inside the method, should use -->self.variableName
#         print(self.a + self.b + d)
#         print(self.book)  # instance variable
#         print(self.gk + " " + self.book)  # instance variable
#         print(self.pen)  # instance variable
#
#     def __add__(self, other):
#         print(self.a + self.b + other.a + other.b)
#
#     def __mul__(self, other):
#         print(self.a * self.b * other.a * other.b)
#
#
# mc = MyClass("thermodynamics")
# mc.add(30)  # 60
# mc.__add__(MyClass)  # 60
# # Below two method are not clear.
# mc.__add__(mc)  # 120
# mc.__mul__(mc)  # 250000

# Example4
# i, j = 15, 25 # global variables # we can access global variables inside the class and method.
#
#
# Class MyClass:
#     a, b = 10, 20 # class variables
#
#     def add(self, x, y): # x, y are the local variables.
#         """
#         Global variables can be accessed inside the class and method.
#         Class variables can be accessed inside the class and method.
#         Local variables can be accessed only inside the method.
#         """
#         print(x + y)  # x, y are the local variables.
#         print(self.a + self.b)  # a, b are class variables
#         print(i + j)  # i, j are global variables
#
#
# mc = MyClass()
# mc.add(100, 200)

# Example5:

# a, b = 15, 25 # global variables
#
#
# class MyClass:
#     a, b = 10, 20 # class variables
#
#     def add(self, a, b):
#         """
#         local variables can be accessed only inside the method.
#         class variables can be accessed inside the class and method.
#         global variables can be accessed inside the class and method.
#         local variables have higher priority than class variables or
#         local variables overwrite on class variables and global variables.
#         class variables have higher priority than global variables.
#         or class variables overwrite on global variables only.
#
#         """
#         print(a + b)  # local variables
#         print(self.a + self.b)  # class variables
#         print(globals()['a'] + globals()['b'])  # global variables
#
#
# mc = MyClass()
# # mc.add(1,2)
# mc.add(100, 200)

# Example6: one class can have multiple objects
# class MyClass:
#
#     @staticmethod
#     def display(name):
#         print("this is display method....")
#         print(name)
#
#
# #
# obj1 = MyClass()
# obj1.display("john")
# #
# obj2 = MyClass()
# obj2.display("scott")

# EXAMPLE7: constructor example
# class MyClass:
#     def __init__(self):
#         print("this is constructor..")
#
#     @staticmethod
#     def m1():
#         print("hello...")
#
#     @staticmethod
#     def m2(x, y):
#         return x + y
#
#
# mc = MyClass()  # Invoke constructor automatically as soon as create an object. We need not use the object.
# mc.m1()  # we can call the method using an object or class name.
# print(mc.m2(10, 20))  # 20
