"""
matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2][2])

2

What will be the output of the following Python code?

matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[0][0][1])

1

What will be the output of the following Python code?

matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2])

[0, 1, 2]

What will be the output of the following Python code?

matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[2][1])

[0,1,2]

Choose the correct code to get the third element in the second row, Regarding the following list :

Colors = [ ['Red', 'Green', 'White', 'Black'], ['Green', 'Blue', 'White', 'Yellow'] ,['White', 'Blue', 'Green', 'Red'] ]

print(Colors[1][2])

What will be the output of the following Python code?

matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
print(matrix[0][0][0])

0

What will be the output of the following Python code?

matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix[1][1][1])

1

What will be the output of the following Python code?

matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]

matrix2 = []

for submatrix in matrix:
  for val in submatrix:
    matrix2.append(val)

print(matrix2[2][0])

0












"""
# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
#
# matrix2 = []
#
# for submatrix in matrix:
#     for val in submatrix:
#         matrix2.append(val)
#
# print(matrix2)

# matrix = [[[k for k in range(3)] for j in range(3)] for i in range(3)]
# print(matrix[0][0][1])
#
# matrix = [[[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 2], [0, 1, 2]]]
#
# matrix2 = []
#
# for submatrix in matrix:
#   for val in submatrix:
#     matrix2.append(val)
#
# print(matrix2)


Colors = [[['Blue', 'Green', 'White', 'Black']], [['Green', 'Blue', 'White', 'Yellow']],
          [['White', 'Blue', 'Red', 'Green']]]

print(Colors[2][0][2])
