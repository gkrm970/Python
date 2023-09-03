# Example1  : how to create list

# mylist1 = [10, 20, 30, 40, 50]
# mylist2 = ["apple", "banana", "cherry"]
# mylist3 = ["apple", 10, "banana", 20.5]
# mylist = list()  # empty list
# #
# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

# Example2 : Accessing items from the list
# mylist=["apple","banana","cherry"]     # index starts from 0(zero)
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])

# Example3: Range of indexes , whenever the range statement the end number will never count.
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist[2:5])  #['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])  # ['orange', 'kiwi', 'melon']

# Example4: change item value
# mylist = ["apple", "banana", "cherry"]
# print(mylist)  # ['apple', 'banana', 'cherry']
# mylist[0] = "orange"  # this will change the values based on index
# print(mylist)    #['orange', 'banana', 'cherry']

# Example5: read the list items using loop
# mylist = ["apple", "banana", "cherry"]
# for i in mylist:
#     print(i)

# Example6: check if the item is existed in the list or not
# mylist=["apple", "banana", "cherry"]

# if "orange" in mylist:
#     print("No. orange is not present")
# else:
#     print(" orange is not in the mylist")


# Example7:List Length (counting number of items in a list)
# mylist = ["apple", "banana", "cherry"]
# print(len(mylist))  # 3

# Example8: Add items to the list--->using append()  insert() methods
# mylist=["apple", "banana", "cherry"]
# mylist.append("orange") # adding new item always at the end of the list in append operation.
# print(mylist)
# mylist.insert(2,"orange")  # add item somewhere in the middle of the list based on the index
# print(mylist)

# Example9: remove item from the list. --> using # pop() and remove() method

# mylist=["apple", "cherry", "banana"]
# mylist.pop(1) # here we should specify index not the value
# print(mylist) #['banana', 'cherry']
# mylist.sort() #['apple', 'banana', 'cherry']
# print(mylist)
# mylist.remove("banana")
# print(mylist)


# del method.
# mylist = ["apple", "banana", "cherry"]
# del mylist[2]  # here del command removes single item based on the index
# print(mylist) #['apple', 'banana']

# clear() method.
# mylist = ["apple", "banana", "cherry"]
# mylist.clear()
# print(mylist)  # [] empty list

# Example10 : copy()  method.
# list()
# one way of copy.
# mylist1=["apple", "banana", "cherry"]
# mylist2=list(mylist1)  # this code  is trying to copy from mylist1 to mylist2
# print(mylist1)  #['apple', 'banana', 'cherry']
# print(mylist2)  #['apple', 'banana', 'cherry']

# copy() method
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = mylist1.copy()  # this code  is trying to copy from mylist1 to mylist2 variable
# print(mylist1)  #['apple', 'banana', 'cherry']
# print(mylist2)  #['apple', 'banana', 'cherry']

# Example11: combine/join lists
# using +(plus) operator
# list1=["a","b","c"]
# list2=[1,2,3]
# list3=list1+list2
# print(list3) #['a', 'b', 'c', 1, 2, 3]

# using loop statement and append method, how to add the two list.
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# for i in list2:
#     list1.append(i)
#     # print(list1)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# using extend() method how top add the two list
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)  # ['a', 'b', 'c', 1, 2, 3]

# lists comparison
# mylist1=[10,20,30]
# mylist2=[10,40,30]
#
# if mylist1==mylist2:
#     print("lists are equal")
# else:
#     print("lists are not equal")
