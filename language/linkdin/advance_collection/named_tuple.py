# Demonstrate the use of named tuples object
import collections


def main():
    # TODO : create a Point namedtuple
    pass
    Point = collections.namedtuple("Point", "x y")
    #
    # p1 = Point(10, 20)
    # p2 = Point(30, 40)
    #
    # print(p1, p2)
    # print(p1.x, p1.y)
    # print(p2.x, p2.y)
    #
    # # TODO : use _replace to create a new instance
    # p1 = p1._replace(x=100)
    # print(p1)

    # TODO : use _replace to create a new instance
    # p1 = p1._replace(x=100)
    # print(p1)

    # TODO : create a named tuple from a dictionary
    d = {"x": 10, "y": 20}
    p1 = Point(**d)
    print(p1)


if __name__ == "__main__":
    main()

# Application of Named Tuple.
# 1. It is used to create a lightweight object type.
# 2. It is used to create an immutable object type.
# 3. It is used to create a readable object type.
# 4. It is used to create a self-documenting object type.
# 5. It is used to create a dictionary-like object type.
# 6. It is used to create an object type that can be used without knowing the position of the elements it contains.
# 7. It is used to create an object type that can be used without knowing the number of elements it contains.
# 8. It is used to create an object type that can be used without knowing the names of the fields it contains.
# Named Tuple is a subclass of Tuple.

# example 1
# from collections import namedtuple
#
# # Declaring namedtuple()
# student = namedtuple('Student', ['name', 'age', 'DOB'])
# s1 = student('Nandini', '19', '2501997')
# print(s1)
