a = {1, 2, 3}
b = {3, 4, 5, 6}

# union()
print(a.union(b))
print(a | b)

# intersection()
print(a.intersection(b))
print(a & b)

# difference()
print(a.difference(b))
print(b.difference(a))
print(b - a)
print(a - b)

# symmetric_difference()
print(a.symmetric_difference(b))
print(a ^ b)
