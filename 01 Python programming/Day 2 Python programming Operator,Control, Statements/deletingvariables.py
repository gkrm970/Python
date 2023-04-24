a=100
b=200

print(a)
print(b)

del a

print(a) # NameError: name 'a' is not defined bcz a variable is  already deleted
print(b)
