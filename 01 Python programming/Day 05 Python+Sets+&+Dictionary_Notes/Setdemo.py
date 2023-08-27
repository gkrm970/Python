# Example1 : creating set
# myset={"apple","banana","cherry"}
# print(myset) #{'banana', 'cherry', 'apple'}

# Example 2 duplicate are not allowed.
# myset={"apple","banana","cherry","banana","cherry"}
# print(myset) #{'banana', 'cherry', 'apple'}
#  Inlist duplicates are allowed.
# myset=["apple","banana","cherry","banana","cherry"]
# print(myset) #{'banana', 'cherry', 'apple'}


# Example2: Accessing items from set
# myset = {"apple", "banana", "cherry"}
# for i in myset:
#     print(i)

# print(myset[0])  # TypeError: 'set' object is not subscriptable

# Example3: value exists in set or not
# myset={"apple","banana","cherry"}
# print("banana" in myset)  # true
# print("banana2" in myset)  # false

# Example4: adding items to set
# add()-add single item    update()-add multiple items
# myset = {"apple", "banana", "cherry"}
# myset.add("orange")
# print(myset)  # {'orange', 'banana', 'apple', 'cherry'}  it is a unordered .
# #
# myset.update(["mango", "grapes"])  # some where will be updated in the set
# print(myset)  # {'banana', 'orange', 'apple', 'cherry', 'grapes', 'mango'}

# Example5: find number of items in a set - len()
# myset={"apple","banana","cherry"}
# print(len(myset)) #3


# Example6: remove item from set - remove(),discard()
# myset={"apple","banana","cherry"}
# myset.remove("banana")
# print(myset) # {'cherry', 'apple'}

# myset.remove("xyz")  # KeyError: 'xyz'

# myset.discard("banana")
# print(myset) #{'apple', 'cherry'}

# myset.discard("xyz")   # will not throw any error
# print(myset)

# Example7 : clear all items from set
# myset={"apple","banana","cherry"}
# myset.clear()
# print(myset)  #set()
# #
# del myset
# print(myset) #NameError: name 'myset' is not defined

# Example8: joining 2 sets  - union()
# set1={"a","b","c"}
# set2={"d","e","f"}
# set3=set1.union(set2)
# print(set3)  #{'b', 'c', 'f', 'e', 'd', 'a'}

# update()
# set1={"a","b","c"}
# set2={1,2,3}
# set1.update(set2)
# print(set1) # {'b', 1, 2, 3, 'c', 'a'}

# difference between union and update method in set collection.
# example
# Using union method
# new_set = set1.union(set2)
# print(new_set)  # Output: {1, 2, 3, 4, 5}
# print(set1)     # Output: {1, 2, 3} (original set1 remains unchanged)

# Using update method
# set1.update(set2)
# print(set1)     # Output: {1, 2, 3, 4, 5} (set1 is modified in place)
