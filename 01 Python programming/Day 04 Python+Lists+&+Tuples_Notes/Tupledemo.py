# Example1: creating tuple
# mytuple=("apple","banana","cherry")
# print(mytuple)
# mytuple1=()
# print(mytuple1) # empty tuple

# Example2: access specific tuple items
# mytuple = ("apple", "banana", "cherry")
# print(mytuple[1])  # banana   here index starts from 0
# print(mytuple[-1])  # cherry

# Example3: range of indexes
# mytuple=("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(mytuple[2:5]) #('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1]) # ('orange', 'kiwi', 'melon')

# Example 4: Changing tuple items
# by default tuple does not allow you to change values bcoz it is immutable, but there is work around it
# tuple--> list(modify)--> tuple
#
# #mytuple=("apple", "banana", "cherry")
# mytuple=("apple", 100, 200)
# mylist=list(mytuple) # convert tuple into list
# mylist[0]="orange"
# mytuple=tuple(mylist)
# print(mytuple) #('orange', 'banana', 'cherry')

# Example5: reading tuple items using loop
# mytuple=("apple", "banana", "cherry")
# for i in mytuple:
#     print(i)

# Example6: Check if Item Exists( searching of item in tuple)
# mytuple=("apple", "banana", "cherry")
# if "banana" in mytuple:
#     print("yes, banana is present")
# else:
#     print("no, banana is not present")

# Example7: Tuple Length - counting items in a tuple
# mytuple=("apple", "banana", "cherry")
# print(len(mytuple)) #3

# Example8: Add items to tuple - Not possible bcoz tuple is immutable - cannot change/insert values/items
# mytuple=("apple", "banana", "cherry")
# mytuple[0]="orange" #TypeError: 'tuple' object does not support item assignment
# print(mytuple)

# Example9:  copy tuple
# mytuple1 = ("apple", "banana", "cherry")
# mytuple2=mytuple1
# print(mytuple2) #('apple', 'banana', 'cherry')

# Example10 : removing items from tuple - not possible bcoz tuple is immutable
# mytuple=("apple", "banana", "cherry")
# mytuple.remove("apple")  # invalid  / it is not possible

# del mytuple
# print(mytuple) #NameError: name 'mytuple' is not defined because its already deleted.

# Example11: Join/combine tuple
# tuple1 = (10, 20, 30)
# tuple2 = ('a', 'b', 'c')
#
# tuple3 = tuple1 + tuple2  # concatenation possible
# print(tuple3)  # (10, 20, 30, 'a', 'b', 'c')
# tuple3 = tuple1.copy('tuple2')  # AttributeError: 'tuple' object has no attribute 'copy'

# Example12:  tuples comparison
# tuple1 = (10, 20, 30)
# tuple2=('a','b','c')
# tuple2 = (10, 20, 30)

# if tuple1 == tuple2:
#     print("tuples are equal")
# else:
#     print("tuples are not equal")
