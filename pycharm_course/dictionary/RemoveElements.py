a = dict({1: 'Web', 2: 'Java', 3: 'Database', 4: 'Ruby'})
print(a, type(a))

# pop(<key>)
a.pop(1)
print(a)
# a.pop(1)

# popItem()
a.popitem()
print(a)

# del
del a[2]
print(a)

# del a
# print(a)

# clear()
a.clear()
print(a)
