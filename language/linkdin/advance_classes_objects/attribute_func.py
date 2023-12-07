# class attribute function

# object.__getattribute__(self, attr) - this function is called whenever the attribute of an object is accessed
#                                                   called when object.attr

# object.__getattr__(self, attr) - this function is called whenever the attribute of an object is accessed
#                                                   called when object.attr
# object.__setattr__(self, attr, val) - this function is called whenever an attribute value is set
#                                                   called when object.attr = val
# object.__delattr__(self, attr) - this function is called whenever an attribute is deleted
#                                                   called when del object.attr
# object.__dir__(self) - this function is called when dir() is called on the object
#                                                   called when dir(object)

# customize string representation of objects

class MyColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: use getattr to dynamically return a value
    def __getattr__(self, attr):
        """
        Use this getattr function to override the default getattr function
        """
        if attr == "rgbcolor":
            return self.red, self.green, self.blue
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)
        else:
            raise AttributeError

    # TODO: use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        """
        Use this setattr function to override the default setattr function
        """
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)
            # self.__dict__[attr] = val

    # TODO: use dir to list the available properties
    def __dir__(self):
        """
        Use this dir function to override the default dir function
        """
        return "red", "green", "blue", "rgbcolor", "hexcolor"


def main():
    # create an instance of myColor
    cls1 = MyColor()
    # TODO: print the value of a computed attribute
    # print(cls1.rgbcolor)
    # print(cls1.hexcolor)

    # TODO: set the value of a computed attribute
    cls1.rgbcolor = (125, 200, 86)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    # TODO: access a regular attribute
    print(cls1.red)

    # TODO: list the available attributes
    print(dir(cls1))


if __name__ == "__main__":
    main()
