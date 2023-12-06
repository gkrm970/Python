# Demonstrate the use of variable argument lists
# *args is used to send a non-keyworded variable length argument list to the function

# TODO : Define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def addition2(base, *args):
    result = base
    for arg in args:
        result += arg
    return result


# Define a function that takes another function as a parameter
# this is called a higher order function
def apply_function(func, arg):
    # Call the function with the given argument
    return func(arg)


# Define a regular function
def square(x):
    return x ** 2


# Pass the regular function as a parameter to apply_function
result = apply_function(square, 5)

# Print the result
print(result)


def main():
    # TODO : pass different arguments
    # print(addition(5, 10, 15, 20))
    # print(addition2(1, 2, 3))

    # TODO : pass an existing list
    # my_nums = [5, 10, 15, 20]
    # print(addition(*my_nums))
    pass


if __name__ == "__main__":
    main()
