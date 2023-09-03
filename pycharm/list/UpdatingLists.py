a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# add new elements
# Using index to change the value
a[1] = 100
print(a)

# Using slicing operator to change value
a[1:4] = [33, 34, 35, 36, 37]
print(a)

# Using append() function
a.append(200)
a.append(300)
print(a)

# Using extend() function
a.extend([2, 4, 10])
print(a)

b = [99, 999, 9999]
c = [1, 2]
c.extend(b)
print(c)

# Using insert() function
a.insert(2, 1)
print(a)

# delete elements
# Using del function
del a[1]
print(a)

del a[1:3]
print(a)

# Using remove()
a.remove(5)
# a.remove(1:4)
print(a)

# Using pop()
a.pop(1)
print(a)

a.pop()
print(a)

# Using clear()
a.clear()
print(a)
