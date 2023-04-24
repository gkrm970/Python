# lambda expression
# Example 01
# str2 = 'GeeksforGeeks'
#
# # lambda returns a function object
# rev_upper = lambda x: x.upper()
# # rev_upper = lambda x: x.upper()[::-1]
# print(rev_upper(str2))
#
# # Example 02
# format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
#
# print("Int formatting:", format_numeric(1000000))
# print("float formatting:", format_numeric(999999.789541235))
#
# # Example 03
# def cube(y,z):
# 	return y*y*z
#
#
# lambda_cube = lambda y,z: y*y*z
#
# # using function defined
# # using def keyword
# print("Using function defined with `def` keyword, cube:", cube(5,7))
#
# # using the lambda function
# print("Using lambda function, cube:", lambda_cube(5,6))
#

# Example 1: Python Lambda Function with List Comprehension

# is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
#
# # iterate on each lambda function
# # and invoke the function to get the calculated value
# for item in is_even_list:
# 	print(item())
# # print(list(is_even_list))    # this will not work

# Example 2: Python Lambda Function with if-else
# Max = lambda a, b : a if(a > b) else b
#
# print(Max(1, 2))

# Example 3: Python Lambda with Multiple statements

List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)


# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)

print(res)













# ml = lambda x, y: x + y
# print(ml(2, 3))
#
# # for above example will get same solution using for loop
# x = 3
# y = 2
#
#
# def multiplication(x, y):
#     return x + y
#
#
# print(multiplication(2, 3))
#
# # Using Lambda with Python Built-ins---------
# # Lambda Function with Filter()
#
# # Exm 01 all odd numbers are filtered out using the filter() function and lambda function.
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# final_list = list(filter(lambda x: (x % 2 != 0), li))
#
# print(final_list)
# # for above example will get same solution using for loop
# final_list = []
# for i in li:
#     if i % 2 != 0:
#         final_list.append(i)
# print(final_list)
#
# # Lambda Function with Map()
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(map(lambda x: x % 2, li))
#
# print(final_list)

# Lambda Function with Reduce()
# from functools import reduce
# exam 1 the sum of all elements of the list is calculated using reduce() function and lambda function.

# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)

