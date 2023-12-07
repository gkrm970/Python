# customize string representation of objects

# String functions
# repr() - returns a printable representation of the object
# str() - returns a nicely formatted string representation of the object
# format() - returns a string formatted by the passed in arguments
# bytes() - returns a bytes representation of the object


class Person:
    def __init__(self):
        self.f_name = 'Joe'
        self.l_name = 'Marini'
        self.age = 25

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        """
        Use this repr function to override the default repr function
        """
        return '<Person Class - f_name:{0}, l_name:{1}, age:{2}>'.format(self.f_name, self.l_name, self.age)

    # use __str__ to create a string useful for the user more readable
    def __str__(self):
        """
        Use this str function to override the default str function
        """
        return 'Person ({0} {1} is {2})'.format(self.f_name, self.l_name, self.age)

    # use __bytes__ to create a bytes representation of the object
    def __bytes__(self):
        val = 'Person:{0}:{1}:{2}'.format(self.f_name, self.l_name, self.age)
        return bytes(val.encode('utf-8'))


def main():
    # create a new person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print('Formatted: {0}'.format(cls1))
    print(bytes(cls1))


if __name__ == "__main__":
    main()

# Application 1: Create a class that returns the current date and time

# Application 2: Create a class that returns the current date and time in the timezone passed in as an argument
