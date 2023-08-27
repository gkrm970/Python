# def common_latter():
#     str1 = input('Enter a string latter')
#     str2 = input('enter second string latter')
#     set1 = set(str1)
#     set2 = set(str2)
#     lst = set1 and set2
#     print(lst)


# common_latter()

"""def frequency():
    str1 = "hello Radhakrishna how are you"
    lst = str1.split()
    empty = {}
    for i in lst:
        if i not in empty.items():
            empty[i] = 0
            empty[i] = empty[i]+1

    print(empty)


# frequency()
"""
# import keyword

# def list_to_dict():
#     key = [1, 2, 3]
#     value = ["one", "two", "three"]
#     result = dict(zip(key, value))
#     print(result.items())
#
#
# list_to_dict()

# finding the missing number

# def get_missing_summation(a):
#     n = a[-1]
#     sum1 = 0
#     total = n * (n + 1) // 2
#     sum1 = sum(a)
#     print(total - sum1)
#
#
# a = [1, 2, 3, 5, 6, 7]
# get_missing_summation(a)
# *******************************************************************************************************
# Alies concept 1
# Q1 Difference between is and == operators in python
"""In general Is operator for reference comparison or address comparison.ie if two references are pointing to the same
# object, then only Is operator return true."""
"""== Operator means for content comparison. I.e., even though objects are different, if the content is then == operator
# return true."""

# l1 = [10, 20, 30, 40]
# l2 = [10, 20, 30, 40]
# l3 = l1
#
# print(l1 is l2)  # false
# print(id(l1))
# print(id(l2))
# print(l1 == l2)  # true
# print(l1 == l3)  # true


# Q2 Explain about ternary operator or conditional operator
# x = first value if condition else second value
# if condition is true then first value will be considered, otherwise the second value will be considered.

# Find max of two given numbers.
"""a = input('Enter first value')
b = input('Enter second value')

mx = a if a > b else b
print('maximum value is ', {mx})"""

"""
# find max of three given numbers.
a = input('enter first value')
b = input('enter second value')
c = input('enter third value')

mx = a if a > b and a > c else b if b > c else c
print('biggest value among three numbers is ', {mx})"""

# Q3 what are various data types in python.
"""
# Int, float, complex, str, bool --> fundamentals data types.
# list, tuple, set, dict, frozen, frozenset, bytes, bytearray and  range.
"""
# Q4 explain mutability and immutability with an example.
# Mutable mean changeable where immutable mean non-changeable
# once an object is created, we cannot change.

# li = [10, 20, 30]
# li[2] = 40
# print(li)
#
# li = (10, 20, 30)
# # li[2] = 40 #tuples don't support item assignment
# print(li)

# In python, which object is immutable,
# all fundamentals data types are immutable.
# Tuple, frozen, bytes,range are immutable then rest are mutable

# Q6 explain difference between a list and tuple.

# List
# # is a group of comma separated by values within square parenthesis.
# []
# list =[1,2,3,4]
# list[2] =5
# list objects consume more size -->sys.getsizeOf(object)
# list object won't be reusable
# performance of a list is low, i.e., operation on list object requires more time.
# The Comprehensive concept is applicable for a list
#  object are un-hashable type, and hence we cannot store in a set and dict
# If the content is not fixed and keep on changing, then it is recommended to go head with a list object.
# Packing is not possible in a list object but reverse is possible

# tuple
#  is a group of comma separated by values within round parenthesis and parenthesis are optional
# ()
# tuple = (1,2,3,4) or 1,2,3,4
# tuple[3] =5  # Builtin 'tuple' cannot be parameterized directly
# TUPLE object consume LESS size -->sys.getsizeOf(object)
# tuple object won't be reusable
# performance  of tuple is high, ie operation on tuple object require less time.
# Comprehensive concept is not applicable for a tuple
#  object are hashable type, and hence we can store in a set and in dict
# If the content is fixed and not changing, then it is recommended to go head with a tuple object.
# # Packing and Unpacking is possible in a tuple object.

# s = {10, 20, 30, [40, 50]}   #---> Type error : un-hashable type list ---> this is not possible for set
# s = {10, 20, 30, (40, 50)}   #---> this is  possible for set
# s = {[10,20]: 'gk'}   #---> Type error : un-hashable type list ---> this is not possible for dict
# s = {(10,20): 'gk'}   # ---> this is possible for dict

# ls = 1, 2, 3, 4 # this is possible
# 1,2,3,4 = ls this is not possible

# ls = [1, 2, 3, 4]
# a, b, c, d = ls
# print(ls)

# ls = (1, 2, 3, 4)
# a, b, c, d = ls
# print(ls)

# a = 1
# b = 2
# c = 3
# ls = [a, b, c]
# print(ls)
#
# a = 1
# b = 2
# c = 3
# ls = (a, b, c)
# print(ls)

# Q7 what is the difference between set and frozen set.
# All properties of the set and frozenset are the same except the following difference.
# Set is mutable but frozenset is immutable.

# s = {10, 20, 30, 40}
# s.add(50)
# print(s)
# we can add new elements to the set as it is mutable.

# s = {10, 20, 30, 40}
# fs = frozenset(s)  # attribute error frozenset object has no attribute "add"
# s.add(50)
# print(s)
# As frozenset is immutable, add, remove, such type of terminology is not applicable.

# Q8 what is the difference between list and dict

# List
#  is a group of comma-separated individual objects withing square bracket.
# Ls = [1, 2, 3, 4, 5]
# In list insertion ordered is preserved.
# In the list, duplicated objects are allowed.
# In the list, we can access an object by using index, which is zero bases. I.e., the index of a first object is zero.
# In the list objects need to be hashable


# Dict is a group of comma-separated key-value pairs withing curly braces. D = {'key1': 'value1', 'key2': 'value2'}
# In dict all key-value pairs will be stored based on hashcode of keys, and hence insertion ordered is not
# preserved, But from 3.7 version onwards the dict functionality is internally replaced with orderedDict functionality.
# Hence, from 3.7 version onwards, in the case of normal dict also insertion can be guaranteed.
# d = {}
# d[10] = 'a'
# d[20] = 'b'
# d[30] = 'c'
# print(d)
# In dict, duplicates keys are not allowed but values can be duplicated. If we are trying to add an entry with
# duplicate key, then old value will be replaced with new value.

# d = {10: 'z', 20: 'b', 30: 'c'}
# print(d)

# In dict, we can access values by using keys.
# In the dict keys must be hashable

# Q9 what is the difference between list and set.
# List is a group of comma-separated individual objects withing square braces.
ls = [1, 2, 3, 4]
# set is a group of separated by individuals object within curly braces.
st = {1, 2, 3, 4}

# In the list, duplicates are allowed.
# In set duplicates are not allowed

# In the list insertion order is preserved
# In set objects will be inserted based on hashcode, and hence insertion order is not preserved.

# In list object need not hashable
# In a set object should be hashable

# In list indexing and slicing concept are applicable for a list.
# In a set indexing and slicing concept they are not applicable for a set

# Q10. Explain slice operator. If we want to access part (piece or slice) of a given sequence, then we should go for
# slice operator. The sequence can be string or list or tuple, etc.
# syntax:
# s[begin:end:step] step value can be either +ve or -ve but not zero.
# If step value is +ve, then we have to consider from beginning index to end-1 index in forward direction.
# If step value is -ve, then we have to consider from begin index to end+1 index in the backward direction.

# Note
# In forward direction, if enf value is zero, then a result is always empty.
# In the backward direction, if the end value is -1, then the result is always empty.

# Q12. How to reverse string by using slice operator.
# s[::-1]
# s = 'abcdefg'
# print('original string', s)
# print('reversed string',s[::-1])

# Q13. What is the difference between *args and **kwargs? *Args --> variable length arguments f(*args) --> If a
# function with *args arguments, then we can call that function by passing any number of values including zero. With
# all these values tuple will be created.
# def f1(*args):
#     print(args)
#
#
# f1()
# f1(1, 2, 3)
# f1(1, 2, 3, 4, 5)

# def sum1(*args):
#     total = 0
#     for x in args:
#         total = total + x
#     print('the sum', total)
#
#
# sum1()
# sum1(1, 2, 3)
# sum1(1, 2, 3, 4, 5)

# **kwargs -->variable length keyword arguments.

# f1(**kwargs): we call this function by passing aby number of keyword arguments including zero numbers, and with all
# these keyword arguments, a dictionary will be created.
# def f1(**kwargs):
#     print(kwargs)
#
#
# f1(name='gk', roll=1, marks=90)

# Q14 what is the difference between dir() and help() function.
# dir() function just list out all members of given
# module. But help() function provides documentation related to what module.
# Exm import math
# print(dir(math))
# help(math)

# x = 10
# y = 20
#
#
# def f1():
#     pass
#
#
# print(dir())

# note
# dir()-->without argument, it will list out all the members of the current module.
# dir(modulename) --> with argument, it will list out all members of specified module.
# help(keyword.kwlist)

# Q15 what is lambda function or anonymous function? sometimes we can declare a function without any name such type
# of nameless function is called anonymous function or lambda function.
# the main objective of anonymous function is just for instant use.
# Using lambda functions, we can write very concise code, so that the readability of the code will be improved.

# Normal function
# we can define normal function by using def keyword.
# def square(n):
#     return n * n
#

# lambda function
# we can define anonymous function by using lambda keyword
# syntax lambda argument_list: expression
# n_n = lambda n: n * n

# exm create a lambda function to find square of given number.
# sqr = lambda n: n * n
# print('the square of', sqr(2))
#

# Q16 what are the differences between normal function and lambda function?

# 1. It is a named function, and we can define by using def keyword.
# It's a nameless(anonymous) function, and we can define by using lambda keyword

# 2. In normal function, we have written a return statement explicitly to return some value.
"""In lambda function,In we are not required to write a return statement explicitly to return some value because lambda
 function internally has a return statement."""

# 3. If we want to use a function multiple times, then we should go for a normal function.
# If we want to a function just for instant use(ie one time usage), then we should go for lambda function.

# 4. In normal function, the length of the code is more and hence readability will be reduced.
# In lambda function, the length of the code is very less (concise code), and hence readability will be improved.

# 5. for normal function, we can handle complex logic which consists more lines of code.
# for lambda function, we cannot handle complete logic which consists of more lines of code.

# Q17 Explain about filter() function?.
# We can use filter() to filter values from the given sequence based on some condition.
"""Filter(function,sequence) Where argument function is responsible to perform conditional check, 
and it should be a boolean-valued function."""

"""for every element in given sequence this function will be applied and if it return true then only the value will be
considered in the results"""

# with/without lambda function
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# l1 = [0, 5, 10, 15, 20, 25, 30]
#
# # is_even = [i % 2 == 0 for i in l1]
is_even = lambda x: x % 2 == 0
#
#
# l2 = list(filter(is_even, l1))
# print(l2)
# # exm02
ll = ['apple', 'banana', 'pineapple']
#
# fltr = list(filter(lambda x: len(x) > 5, ll))
# print(fltr)

# Q17 Explain about map() function
# Q18 Explain about reduce() function
# Q19 Explain about decorator function
# Q20 Explain about generator function


# x = ['a', 'b', 'c', 'd']
#
# # for x1 in x:
# #     print(x1)
# #
# for x[-1] in x:
#     print(x[-1], end='')
# # abcc

"""
Dictionary Comprehension is a syntax construction to ease the creation of a dictionary based on the existing iterable.
"""
# my_dict = {i: i+1 for i in range(1, 10)}
# print(my_dict)

for i in range(5):
    print(i, end=" ")
print()

