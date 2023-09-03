# Example1:

# class MyClass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# mc1=MyClass()
# mc1.myfun()
# mc1.display("scott") #john

# Example2
# class MyClass:
#     def m1(self):
#         print("this is instance method...")
#
#     @staticmethod
#     def m2(self, num):
#         print(
#             self + num)  # when we declare and call the static method inside the class ,# we have to give value for self parameter


# mc = MyClass()
# mc.m1()
# mc.m2(100, 200)  # 100 200
# MyClass.m2(10, 20)  # 10, 20 # here calling static method directly using class not through object.

# Example3:

# class MyClass():
#     a,b=10,20  # this the class variables
#     def add(self,d):
#         print(self.a+self.b +d)  # a, b are class variable.when we use class variable inside the method , should use -->self.variableName
#
#     def mul(self,c):
#       print(self.a*self.b*c)
# #
# mc=MyClass()
# mc.add(30) #60
# mc.mul(40) # 8000


# Example4
# i, j = 15, 25  # global variables
#
#
# class MyClass:
#     a, b = 10, 20  # class variables
#
#     def add(self, x, y):
#         print(x + y)  # x, y are the local variables.
#         print(self.a + self.b)  # a, b are class variables
#         print(i + j)  # i, j are global variables
#
# mc = MyClass()
# mc.add(100,200)

# Example5:

# a,b=15,25   # global variables
# class MyClass:
#     a,b=10,20   # class variables
#     def add(self,a,b):
#         print(a+b)  # local variables
#         print(self.a+self.b)  # class variables
#         print(globals()['a']+globals()['b'])  # global variables
#
# mc=MyClass()
# # mc.add(1,2)
# mc.add(100,200)

# Example6: one class can have multiple objects
# class MyClass:
#     def display(self,name):
#         print("this is display method....")
#         print(name)
# #
# obj1=MyClass()
# obj1.display("john")
# #
# obj2=MyClass()
# obj2.display("scott")

# EXAMPLE7: constructor example
# class MyClass:
#     def __init__(self):
#         print("this is constructor..")
#
#     def m1(self):
#         print("hello...")
#
#     def m2(self, x, y):
#         return (x + y)
#

#
# mc = MyClass()  # invoke constructor automatically. we need not use the object.
# mc.m1()  # method ---we have to call the method explicitly by using object.
# print(mc.m2(10,20))  # 20
