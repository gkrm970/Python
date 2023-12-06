# Demonstrate the use of only keyword arguments
# **kwargs is used to pass a keyworded, variable-length argument list
# kwargs is a dictionary, so it must be accessed like one
def my_function(arg1, arg2, *, suppress_exceptions=False):
    """* is used to separate positional arguments from keyword arguments"""
    pass


def main():
    # TODO : try to call function without keyword arguments
    my_function(1, 2, suppress_exceptions=True)


if __name__ == "__main__":
    main()
