# Define the enumerations using the Enum base class

from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    """
    Enum class for fruits
    Okay to have the same value for different enum but not the same name
    If required when you use @unique decorator, even it will raise an error if you have the same value for different enum
    """
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


def main():
    # todo : enum have human readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # # todo : enum have name and value properties
    print("Name is", Fruit.APPLE.name, "and ", "value is", Fruit.APPLE.value)

    # # todo : print the auto-generated value
    print(Fruit.PEAR.value)  # 5 - auto generated value
    print(Fruit.PEAR.name)  # PEAR

    # todo : enums are hashable - can be used as keys
    my_fruits = {}
    my_fruits[Fruit.BANANA] = "Come mr. tolly man"
    print(my_fruits[Fruit.BANANA])


if __name__ == '__main__':
    main()
