# Example1 : Single inheritance  To check the inheritance concept inherit method from parent class to child
# class class A:
#   @staticmethod
#   def m1():
#   print("this is m1 method from class A")
#
#
# #
# class B(A):
#     @staticmethod
#     def m2():
#         print("this is m2 method from class B")
#
#
# bobj = B()
# bobj.m1()  # this is m1 method from class A
# bobj.m2()  # this is m2 method from class B

# # Example2: single inheritance accessing parent class variables and methods in child class
# # parent class variables and methods overriding on child class variables and methods.
# class A:
#     x, y = 10, 20
#
#     def m1(self) -> int:
#         return self.x + self.y
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self) -> int:
#         return self.a * self.b
#
#
# bobj = B()
# print(bobj.m1())  # 30
# print(bobj.m2())  # 100
# print(bobj.x)  # 10
# print(bobj.y)  # 20
# print(bobj.a)  # 200
# print(bobj.b)  # 100

# Example2: single inheritance accessing parent class variables and methods in child class
#  variables and methods overriding on parent class variables and methods.
# class A:
#     a, b = 10, 20
#
#     def m1(self) -> int:
#         return self.a + self.b
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self) -> int:
#         return self.a * self.b
#
#
# bobj = B()
# print(bobj.m1())  # 30
# print(bobj.m2())  # 100

# Example 3: Multilevel inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# #
# class C(B):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)
#
#
# cobj = C()
# cobj.m1()  # 30
# cobj.m2()  # 100
# cobj.m3()  # 10
# print(cobj.x)  # 10
# print(cobj.y)  # 20
#
# print(cobj.a)  # 200
# print(cobj.b)  # 100
#
# print(cobj.i)  # 5
# print(cobj.j)  # 2

# #Example4: Hierarchy inheritance
# class A:
#     x, y = 10, 20
#
#     def m1(self):
#         print(self.x + self.y)
#
#
# class B(A):
#     a, b = 200, 100
#
#     def m2(self):
#         print(self.a - self.b)
#
#
# #
# class C(A):
#     i, j = 5, 2
#
#     def m3(self):
#         print(self.i * self.j)


#
# bobj=B()
# bobj.m1()  # 30
# bobj.m2() # 100
#
# cobj = C()
# cobj.m1()  # 30
# cobj.m3()  # 10

# Example5 : Multiple inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# #
# class B:
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
# #
# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)
#
# cobj=C()
# cobj.m1() # 30
# cobj.m2() #100
# cobj.m3() # 10

# **** Example6: calling parent class method using child class(super())
# using super() method we can call parent class instance method and static method,
# using super() method we can call parent class instance variables and class variables
# *** but if method declares as static method, from it can't be calling either instance or static method
# using super() method even for variables also.

# q = 10 # global variables
# w = 20 # global variables
#
#
# class A:
#     x = 1
#     y = 2
#     abc = None
#
#     def __init__(self):
#         print("This is constructor from class A")
#         self.a, self.b = 10, 20
#         self.xyz = None
#
#     @staticmethod
#     def m1(a):  # static method can't be accessed either of class and instance variables.
#         print("This is m1 method from class A", {a})
#
#     def m2(self):  # instance method
#         print("This is m2 method from class A", self.a + self.b)
#         self.abc = [1, 2, 3, 4, 5]
#         self.xyz = [6, 7, 8, 9, 10]
#
#
# class B(A):
#     # @staticmethod # static method can't be called using super() method
#     def m3(self):
#         print("This is m3 method from class B")
#         super().m1(self.x)  # calling static method from parent class and accessing class variable from parent class
#
#         super().m2()
#         #  **** I want to access a variables abc and xyz from method m1 from class A to method m2 from class B
#         print(self.abc)
#         print(self.xyz)
#
#         super().m1(self.a)  # This is not possible
#         super().__init__()  # calling constructor from parent class
#         print(self.a + self.b)  # instance variables from parent class
#         print(self.x + self.y)  # class variables from parent class
#         print(q + w)  # global variables
#         print(self.a)


#
# bobj = B()

# bobj.m1()

# bobj.m2()
# bobj.m3()  # This is m3 method from class B
#             #This is m1 method from class A
#             #This is m2 method from class A

# Example7
# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=100,200
#     def m(self,x,y):
#         print(x+y)  # local variables  3000
#         print(self.i+self.j) # class variables 300
#         print(self.a+self.b) # printing class variables from parent class  ---30
# #
# bobj=B()
# bobj.m(1000,2000)

# Example8: overriding variables
# class Parent:
#     name = "Scott"
#
#
# class Child(Parent):
#     name = "John"  # overriding the variable value
#
#     def test(self):
#         print(self.name)
#         print(super().name)
#
#
# #
# cobj = Child()
# cobj.test()  # john  Scott
# print(cobj.name)  # "John" # overriding the variable value

# Example 9: Overriding methods
# class Bank:
#     def rate_of_interest(self):
#         return 0
#
#
# #
# class XBank(Bank):
#     def rate_of_interest(self):
#         return 10
#
#
# #
# class YBank(Bank):
#     def rate_of_interest(self):
#         return 12
#
#
# objx = XBank()
# print(objx.rate_of_interest())  # 10 method name is remained same here

# objy = YBank()
# print(objy.rate_of_interest())  # 12 method name is remained same here

# Example10: overloading 1(polymorphism)
# class Human:
#     @staticmethod
#     def sayhello(name=None):
#         if name is not None:
#             print("Hello " + name)
#         else:
#             print("Hello no name")
#
#
# #
# h = Human()
# h.sayhello("scott")
#
# h.sayhello()

# Example11: overloading 2

# class Calculation:
#     @staticmethod
#     def add(a=0, b=0, c=5):
#         print(a + b + c)
#
#
# #
# calobj = Calculation()
# calobj.add()  # 0
# calobj.add(10, 20)  # 30
# calobj.add(100, 200, 300)  # 600
