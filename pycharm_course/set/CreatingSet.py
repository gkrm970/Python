s = {1, 2, 3, 4, 5}
print(s)

# No duplicates
s = {1, 2, 2, 3, 4, 5}
print(s)

# set of mixed data types
a = {1, 2, "Python", 3}
print(a)
print(type(a))

# converting list to set
l = [1, 2, 3]
s = set(l)
print(s)
print(type(s))

# set cannot have mutable objects like list, set
# a = {1, 2, {11, 22, 44}}
# print(a)

# a = {1, 2, [11, 22, 44]}
# print(a)

# empty set
a = {}
print(a)
