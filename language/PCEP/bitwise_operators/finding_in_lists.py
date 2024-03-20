"""
What will be the output of the following Python code?

list1=[3,4,6,1,2]
list2=list1
list1[0]=9
print(list2)

[9,4,6,1,2]

What will be the output of the following Python code?

list1 = [0, 3, 4, 1, 2]
list1[1]=[8,9]
print(list1)

[0, [8, 9], 4, 1, 2]

What will be the output of below Python code?

my_list = [0, 1, 2, 3, 4]
print(my_list.index(2))

2

What will be the output of below Python code?

countries = ["USA", "Canada", "India"]
countries[0], countries[1] = countries[1], countries[0]
print(countries)

['canada', 'usa', 'india']

What will be the output of the following Python code?

list1 = [0, 3, 4, 1, 2]
list1[2:5]=[8,9]
print(list1)

[0, 3, 8, 9]

What will be the output of below Python code?

my_list = [0, 3, 4, 1, 2]
print(my_list.index(1))

3

What is the output of the following code:

(4, 6) not in [(4, 7), (5, 6), "hello"]

True
But python syntax error

Choose the correct answer if the following list contains the element 'A'. Check if you get "True" in the output.

Li = ['A','C','b', 1, 3, 4]

"A" in Li,correct
A in Li is wrong

What will be the output of the following Python code?

list1=[3,4,6,1,2]
list2=list1
list1[1]=9
print(list2)


list1 = [0, 3, 4, 1, 2]
list1[2:4]=[1,2]
print(list1)

[0, 3, 1, 2, 2]







"""
#
# my_list = [0, 1, 2, 3, 4]
# print(my_list.index(2))

# countries = ["USA", "Canada", "India"]
# countries[0], countries[1] = countries[1], countries[0]
# print(countries)
#

# (4, 6) not in [(4, 7), (5, 6), "hello"]

list1 = [0, 3, 4, 1, 2]
list1[2:4] = (1, 2)
print(list1)
