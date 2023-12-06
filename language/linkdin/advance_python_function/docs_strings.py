# Doc strings are used to document the purpose of a function, class, or module.
# Doc strings are surrounded by triple quotes.
# Doc strings are accessible through the __doc__ attribute on the object.
# Doc strings are used by the help() function.
# Doc strings are used by the pydoc module.
# Doc strings are used by the doctest module.
# Doc strings are used by the unittest module.
# Doc strings are used by the inspect module.


def add(a, b):
    """This function adds two numbers together"""
    return a + b


print(add(1, 2))
print(add.__doc__)


