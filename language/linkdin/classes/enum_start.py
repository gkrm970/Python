# Define the enum class for the start page
from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # RED_DELICIOUS = 1
    PEAR = auto()


def main():
    # todo : enum have human readable values and types
    # print(Fruit.APPLE)
    # print(type(Fruit.APPLE))
    # print(repr(Fruit.APPLE))

    # todo : enum have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # todo : print the auto-generated value
    print(Fruit.PEAR.value)  # 5

    # todo : enums are hashable - can be used as keys
    myFruits = {}
    myfruits[Fruit.BANANA] = "Come mr. tolly man"
    print(myfruits[Fruit.BANANA])


if __name__ == '__main__':
    main()
