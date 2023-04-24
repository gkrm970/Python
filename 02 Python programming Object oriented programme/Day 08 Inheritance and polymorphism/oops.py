# EXAMPLE7: constructor example
# class MyClass:
#     def __init__(self):
#         print("this is constructor..")
#     def m1(self):
#         print("hello...")
#     def m2(self,x,y):
#             return(x+y)
#
# mc=MyClass()    # Here will invoke constructor automatically
# mc.m1()  # method we have to call explicitly by using object
# print(mc.m2(10,20))  # 20 method we have to call explicitly by using object

# Example8
# class MyClass:
#     name="john"
#     def __init__(self,name):     # constructor expecting one argument
#         print(name)
#         print(self.name)
#
# mc=MyClass("David")  # passing parameter to the constructor
# Requirements
# Example9
# Req: Emp
# constructor : eid, ename, sal
# display()  : print eid, ename & sal

# class Emp:
#     def __init__(self, eid, ename, sal):
#             self.eid=eid
#             self.ename=ename
#             self.sal=sal
#     def display(self):
#         print(self.eid,self.ename,self.sal)
#
# e1=Emp(101,"john",500000)
# e1.display()  #101 john 500000
#
# e2=Emp(102,"scott",700000)
# e2.display()  #102 scott 700000

# Example10
# Req: Emp
# constructor : eid, ename, sal
# constructor  : print eid, ename & sal

# class Emp:
#     def __init__(self, eid, ename, sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#
#     def __str__(self):  # This constructor will return string type data......
#         return (self.ename)  # --> this is only valid code
#         # return(self.ename,self.sal) # invalid becoz __str__() returns only string data
#         # TypeError: __str__ returned non - string(type tuple)
#
#
# # e1 = Emp("john")  # Even though print only string value but have to give other variable as well
# e1 = Emp(101, "john", 500000)
# print(e1)
