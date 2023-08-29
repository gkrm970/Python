a = {1, 2, 3}
# add()
print(a)
a.add(10)
print(a)

# update()
# a.add(10,20)
a.update([11, 22, 33])
print(a)

# update() with range()
a.update(a, range(10))
print(a)

# copy()
b = a.copy()
print(b)
