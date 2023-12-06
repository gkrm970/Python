# advanced iteration functions in the itertools package

import itertools


def test_function(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    # seq1 = ["Joe", "John", "Mike"]
    # cycle1 = itertools.cycle(seq1)  # cycle1 is an iterator
    # print(next(cycle1))  # Joe
    # print(next(cycle1))  # John
    # print(next(cycle1))  # Mike
    # print(next(cycle1))  # Joe

    # TODO: use count to create a simple counter
    # count1 = itertools.count(100, 10)  # start at 100, increment by 10
    # print(next(count1))  # 100
    # print(next(count1))  # 110
    # print(next(count1))  # 120

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    # acc = itertools.accumulate(vals)  # acc is an iterator
    # acc = itertools.accumulate(vals, max)  # acc is an iterator
    # print(list(acc))  # [10, 20, 30, 40, 50, 50, 50]

    # TODO: use chain to connect sequences together
    # x = itertools.chain("ABCD", "1234")
    # print(list(x))  # ['A', 'B', 'C', 'D', '1', '2', '3', '4']

    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    # print(list(itertools.dropwhile(test_function, vals)))  # [40, 50, 40, 30]
    # print(list(itertools.takewhile(test_function, vals)))  # [10, 20, 30]


if __name__ == "__main__":
    main()

