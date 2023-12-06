# use transform functions like sorted, filter, map

def filter_func(x):
    if x % 2 == 0:
        return False
    return True


def filter_func2(x):
    if x.isupper():
        return False
    return True


def square_func(x):
    return x ** 2


def grade_func(x):
    if x < 60:
        return "F"
    elif x < 70:
        return "D"
    elif x < 80:
        return "C"
    elif x < 90:
        return "B"
    else:
        return "A"


def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: use filter to remove items from a list
    # odds = list(filter(lambda x: x % 2 == 1, nums))
    # odds = list(filter(filter_func, nums))
    # print(odds)

    # TODO: use filter on non-numeric sequence
    # lowers = list(filter(lambda x: x < "a", chars))
    # lowers = list(filter(filter_func2, chars))
    # print(lowers)

    # TODO: use map to create a new sequence of values
    # squares = list(map(lambda x: x**2, nums))
    # squares = list(map(square_func, nums))
    # print(squares)

    # TODO: use sorted and map to change numbers to grades
    # grades = sorted(grades)
    # letters = list(
    #     map(lambda x: "F" if x < 60 else "D" if x < 70 else "C" if x < 80 else "B" if x < 90 else "A", grades))
    # letters = list(map(grade_func, grades))
    # print(letters)


if __name__ == "__main__":
    main()
