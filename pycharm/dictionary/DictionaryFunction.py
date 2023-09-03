a = dict({1: 'Web', 2: 'Java', 3: 'Database', 4: 'Ruby'})
print(a, type(a))

# len()
print(len(a))

# get(key, default_value)
print(a.get(1))
print(a.get(1, 100))
print(a.get(111, 100))

# keys()
print(a.keys())
print(type(a.keys()))
print(list(a.keys()))

# values()
print(a.values())
print(type(a.values()))
print(list(a.values()))

# items()
print(a.items())
print(type(a.items()))
print(list(a.items()))
