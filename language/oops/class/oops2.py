# EXAMPLE7: constructor example
# class MyClass:
#     """
#     Static method is a method which is bound to the class and not the object of the class.
#     but we can call static method by using object reference as well as class name
#     """
#     def __init__(self):
#         print("this is constructor.")
#
#     @staticmethod
#     def m1():
#         print("hello...m1 method ")
#
#     @staticmethod
#     def m2(x, y):
#         return x + y
#
#
# mc = MyClass()  # Here constructor will invoke  automatically
# MyClass.m1()  # hello...m1 method
# print(mc.m2(10, 20))
from typing import Tuple


# Example8
# class MyClass:
#     """
#     instance variable: A variable which is declared inside the constructor with self is called instance variable
#     Instance variables are overwrite on class variables.
#     """
#     name = "john"  # class variable
#
#     def __init__(self, name) -> None:  # constructor expecting one argument
#         self.name = name  # instance variable
#         print(name)
#         print(self.name)
#
#
# mc = MyClass("David")  # passing a parameter to the constructor

# Example9 scenario1:
# My is Requirements
# Req: Emp
# constructor : eid, e_name, sal
# display()  : print eid, e_name & sal

# class Emp:
#     def __init__(self, eid, e_name, sal) -> None:
#         self.eid = eid
#         self.e_name = e_name
#         self.sal = sal
#
#     def display(self) -> tuple[int, str, any]:
#         return self.eid, self.e_name, self.sal
#
#
# # Create an object
# e1 = Emp(101, "john", 500000)
# print(e1.display())  # 101 john 500000
# #
# e2 = Emp(102, "scott", 700000)
# print(e2.display())  # 102 scott 700000


# Example10 scenario2:
# Req: Emp
# constructor : eid, e_name, sal
# string constructor  : print eid, e_name & sal

# This class is not clear. Need to check again
# class Emp:
#     def __init__(self, eid: int, e_name: str, sal: int | float) -> None:
#         self.eid = eid
#         self.e_name = e_name
#         self.sal = sal
#
#     def __str__(self) -> str:  # This constructor will return string type data only......
#         return self.e_name  # --> this is only valid code
#         # return(self.e_name,self.sal) # invalid because __str__() returns only string data
#         # TypeError: __str__ returned non - string(type tuple)
#
#     def __repr__(self) -> tuple[int, str, int | float]:
#         return self.eid, self.e_name, self.sal
#
#
# # e1 = Emp("john")  # Even though print only string value but have to give other variable as well
# e1 = Emp(101, "john", 500000)
# print(e1.__repr__())
# print(e1.display())
