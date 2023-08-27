# for loop

# print 1...10 numbers using for loop
# l1 = [1,2,3,4,5,6,7,8,9,10]
# for i in l1:
#     print(i)
# #
# print(list(range(1,11)))

# for i in range(10):
#     print(i)  # 0....9

# for i in range(1,11):   # 1,2,3,4,....10
#     print(i)   #1....10

# print only even numbers between 1....20
# for i in range(2,21,2):
#     print(i)

# print only add numbers between 1....21
# for i in range(1, 22, 2):
#     print(i)

# print 1...10 numbers in descending order ( 10,9,8.....1)
# for i in range(10,0,-1):
#     print(i)

# Requirement print 5,10,15,20.....100
# for i in range(5,101,5):
#     print(i)

# Nested loops  #############################
# exam 01
# x = [1, 2]
# y = [4, 5]
#
# for i in y:
#     for j in x:
#         print(i, j)

# exam =2
# Running outer loop from 2 to 3

# for i in range(2, 4):  # 2,3
#     # Printing inside the outer loop
#     # Running inner loop from 1 to 10
#     for j in range(1, 11):
#         # Printing inside the inner loop
#         print(i, "*", j, "=", i * j)
#     # Printing inside the outer loop
#     print()

# exam =3
# Initialize list1 and list2

# list1 = ['I am ', 'You are']
# list2 = ['healthy', 'fine', 'geek']
# print(len(list1))
# print(len(list2))
#
# # Store length of list2 in list2_size
# list2_size = len(list2)

# Running outer for loop to
# iterate through a list1.
# for item in list1:
#     # Printing outside inner loop
#     print("start outer for loop ")
#     # Initialize counter i with 0
#     i = 0
#     # Running inner While loop to
#     # iterate through a list2.
#     while i < list2_size:
#         # Printing inside inner loop
#         print(item, list2[i])
#         # Incrementing the value of i
#         i = i + 1
#     # Printing outside inner loop
#     print("end for loop ")

# Jumping statement
# exam 03
# Running outer loop from 2 to 3
# for i in range(2, 4):
#     # Printing inside the outer loop
#     # Running inner loop from 1 to 10
#     for j in range(1, 11):
#         if i == j:
#             break
#         # Printing inside the inner loop
#         print(i, "*", j, "=", i * j)
#     # Printing inside the outer loop
#     print()

# exam 04
# Running outer loop from 2 to 3
# for i in range(2, 4):
#     # Printing inside the outer loop
#     # Running inner loop from 1 to 10
#     for j in range(1, 11):
#         if i == j:
#             continue
#         # Printing inside the inner loop
#         print(i, "*", j, "=", i * j)
#     # Printing inside the outer loop
#     print()

# exam 05
# Using list comprehension to make nested loop statement in single line.
# list1 = [[j for j in range(3)] for i in range(5)]
# # Printing list1
# print(list1)
