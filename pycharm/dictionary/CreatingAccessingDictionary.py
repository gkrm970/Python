a = {}
print(a, type(a))

a = {1: "Python", 2: "Java"}
print(a, type(a))

# using dict()
a = dict()
print(a, type(a))

a = dict({1: "Python", 2: "Java", 200: "C++"})
print(a, type(a))

# accessing elements using []
print(a[1])
print(a[2])
print(a[200])

# accessing elements using get()
print(a.get(1))
print(a.get(100))
