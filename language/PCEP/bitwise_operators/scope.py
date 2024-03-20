"""
What is the output of the following snippet:

x = 20
def my_function():
  x = 30
  print(x, end=' ')

my_function()
print(x, end=' ')

30 20

What is the output of the following snippet:

def my_function():
  def my_inner_function():
    x = 20
    print(x)
  my_inner_function()

my_function()
20

What is the output of the following snippet:

def myfunc():
  a = 20

myfunc()
print(a)

error

What is the output of the following snippet:

def my_function():
  def my_inner_function():
    x = 20
  print(x)
  my_inner_function()

my_function()

error

What is the output of the following snippet:

x = 20
def my_function():
  print(x, end=' ')

my_function()
print(x, end=' ')

20 20

What is the output of the following snippet:

x = 20
def my_function():
  x = 30
  print(x, end=' ')

my_function()
print(x, end=' ')

30 20

What is the output of the following snippet:

def myfunc():
  a = 20
  print(a)

myfunc()

20

x = 30
def my_function():
  global x
  x = 20

my_function()
print(x)

20---> considered the latest value

What is the output of the following snippet:

def my_function():
  global x
  x = 30

my_function()
print(x)
30

What is the output of the following snippet:

def my_function():
  x = 20
  def my_inner_function():
    print(x)
  my_inner_function()
my_function()









"""


# x = 20
# def my_function():
#   x = 30
#   print(x, end=' ')
#
# my_function()
# print(x, end=' ')

# def my_function():
#     def my_inner_function():
#         x = 20
#         print(x)
#
#     my_inner_function()


# my_function()

# def myfunc():
#   a = 20
#
# myfunc()
# print(a)

# def my_function():
#   def my_inner_function():
#     x = 20
#   print(x)
#   my_inner_function()
#
# my_function()
# x = 30


# def my_function():
#     global x
#     x = 20
#
#
# my_function()
# print(x)

# def my_function():
#     global x
#     x = 30
#
#
# my_function()
# print(x)

def my_function():
    x = 20

    def my_inner_function():
        print(x)

    my_inner_function()


my_function()
