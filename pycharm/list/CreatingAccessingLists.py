# Creating lists
# Declaring list object
a = []
print(a)

a = [1, 2, 3, 4, 5, 6]
print(a)

# Using split() function
s = "I love python programming"
a = s.split()
print(a)
print(type(a))

# Using list() function
a = list(range(10, 20, 2))
print(a)

# list of numbers
a = [1, 2, 3]
print(a)

# list of strings
a = ["python", "programming"]
print(a)

# list of mixed datatype
a = [1, "a", 2, "b"]
print(a)

# Nested lists
a = [1, 2, ["a", "b"]]
print(a)
print(a[0])
print(a[2][1])

# Accessing elements of the list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(a[1])
print(a[-1])

# Slice operator to access elements of the given list
# list-name[start :  stop : step]
print(a[1: 10: 1])
print(a[1:10])
print(a[1::2])
print(a[1:500:2])
print(a[10:1:-2])
