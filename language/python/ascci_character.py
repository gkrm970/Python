# Write the ASCII character and ord  of alphabet
# ascii character of A
# print(ord('a'))  # 97
# print(ord('A'))  # 65
# print(ord('z'))  # 122
# print(ord('Z'))  # 90
# print(ord('1'))  # 49
# print(ord('0'))  # 48
# print(ord('9'))  # 57
# print(ord(' '))  # 32
# print(ord('\n'))  # 10
# print(ord('\t'))  # 9
# print(ord('\r'))  # 13
# print(ord('\f'))  # 12
# print(ord('\v'))  # 11
# print(ord('\b'))  # 8
# print(ord('\a'))  # 7
# print(ord('\0'))  # 0
# print(ord('\1'))  # 1
# print(ord('\2'))  # 2
# print(ord('\3'))  # 3
# print(ord('\4'))  # 4
from builtins import min

# print(len('\' \\') - len('\n'))
# print(len('\' \\') - len('\t'))
# print(len('\' \\') - len('\r'))
# print(len('\' \\') - len('\f'))
#
# print(float('1.0'))


print(min('abcdedfghijklmnopqrstuvwxyz'))
print(max('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
print(min('0123456789'))
print(max('0123456789'))

# difference between find() and index() find() returns -1 if the substring is not found, whereas index() throws an
# exception. find() is faster than index() because it returns -1 if the substring is not found, whereas index()
# throws an exception.
# print('python'.find('th')) # 2
# print('python'.find('th', 3)) # -1
# print('python'.find('th', 2)) # 2
print('python'.find('th', 0, 2))  # -1
print('python'.find('th', 0, 3))  # 2
print('python'.find('th', 0, 4))  # 2
print('python'.find('th', 0, 5))  # 2
print('python'.find('th', 0, 6))  # 2

# rfind() returns the highest index of the substring if found in the string, otherwise returns -1.
print('python'.rfind('th'))  # 2
print('python'.rfind('th', 3))  # -1
print('python'.rfind('th', 2))  # 2
print('python'.rfind('th', 0, 2))  # -1
print('python'.rfind('th', 0, 3))  # 2
print('python'.rfind('th', 0, 4))  # 2

