"""
countries = [['Egypt', 'USA', 'India'],
       ['Dubai', 'America', 'Spain'],
       ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in
                       sublist if len(country) < 6]
print(countries2)

['Egypt', 'USA', 'India', 'Dubai', 'Spain'] ---> List Comprehension should to get in single line code

What will be the output of the following Python code?

countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
print(countries2)

['USA']

What will be the output of the following Python code?

matrix = [[j for j in range(3)] for i in range(3)]
print(matrix[1][2])

2

matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[0])
0

Choose the correct answer to define a list “Num” which contains numbers from 1-9 with 3 elements only in the row.

Num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


What will be the output of the following Python code?

matrix = [[j for j in range(4)] for i in range(4)]
print(matrix[3][1])

1

What will be the output of the following Python code?

a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a[3][3])

3

matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2])

2

a = []
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(j)

print(a[2][3])

which of the following answer will give for bellow code.
a = []
for i in range(2):
    a.append([])

print(a)




"""

# countries = [['Egypt', 'USA', 'India'],
#              ['Dubai', 'America', 'Spain'],
#              ['London', 'England', 'France']]
# countries2  = [country for sublist in countries for country in
#                        sublist if len(country) < 6]
# print(countries2)

# for sublist in countries:
#     for country in sublist:
#         if len(country) < 6:
#             print(country)

# matrix = [[j for j in range(3)] for i in range(3)]
# print(matrix)

# matrix = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
#
# matrix2 = []
#
# for submatrix in matrix:
#     for val in submatrix:
#         matrix2.append(val)
#
# print(matrix2)
# # print(matrix2[0])
#
# matrix = [j for j in range(4) for i in range(4)]
# print(matrix)

# a = []
# for i in range(5):
#     a.append([])
#     for j in range(5):
#         a[i].append(j)
#
# # print(a[3][3])
# print(a)


# a = []
# for i in range(5):
#     a.append([])
#     for j in range(5):
#         a[i].append(j)
#
# print(a[2])

# a = []
# for i in range(2):
#     a.append([])
#     for j in range(2):
#         a[i].append(j)

# a = []
# for i in range(2):
#     a.append([])
#
# print(a)
