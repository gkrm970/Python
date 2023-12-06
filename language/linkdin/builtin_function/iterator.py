# demonstrate the use of iterator objects using the built-in function iter(), next(), zip(), enumerate(),iteritems(),
# iter(), iterkeys(), itervalues() An iterator is an object that represents a stream of data. This object returns the
# data one element at a time. It can be a list, tuple, dictionary, set, or string. An iterator object can be iterated
# upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which
# implements the iterator protocol, which consist of the methods __iter__() and __next__(). Lists, tuples,
# dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:


def main():
    # TODO: define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    days_fr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # TODO: use iter to create an iterator over a collection
    # i = iter(days)
    # print(next(i))  # Sun
    # print(next(i))  # Mon
    # print(next(i))  # Tue

    # TODO: iterate using a function and a sentinel
    # with open("text_file.txt", "r") as fp:
    #     for line in iter(fp.readline, ''):
    #         print(line)

    # TODO: use regular interation over the days
    # for m in range(len(days)):
    #     # print(m, days[m]) # 0 Sun, 1 Mon, 2 Tue, 3 Wed, 4 Thu, 5 Fri, 6 Sat
    #     print(m + 1, days[m])  # 1 Sun, 2 Mon, 3 Tue, 4 Wed, 5 Thu, 6 Fri, 7 Sat

    # TODO: using enumerate reduces code and provides a counter
    # for i, m in enumerate(days, start=1):
    #     print(i, m)  # 1 Sun, 2 Mon, 3 Tue, 4 Wed, 5 Thu, 6 Fri, 7 Sat

    # TODO: use zip to combine sequences
    # for i, m in enumerate(zip(days, days_fr), start=1):
    #     print(i, m[0], "=", m[1], "in french") # 1 Sun = Dim in french, 2 Mon = Lun in french, 3 Tue = Mar in french,
    #     # 4 Wed = Mer in french, 5 Thu = Jeu in french, 6 Fri = Ven in french, 7 Sat = Sam in french

    # TODO: use zip and enumerate to combine sequences
    # for i, m in enumerate(zip(days, days_fr), start=1):
    #     print(i, m[0], "=", m[1], "in french")

    # TODO: use a dictionary to convert to more friendly names
    # days_dict = dict(zip(days, days_fr))
    # print(days_dict)  # {'Sun': 'Dim', 'Mon': 'Lun', 'Tue': 'Mar', 'Wed': 'Mer', 'Thu': 'Jeu', 'Fri': 'Ven',
    # # 'Sat': 'Sam'}
    # days_tuple = tuple(zip(days_fr, days))  # (('Dim', 'Sun'), ('Lun', 'Mon'), ('Mar', 'Tue'), ('Mer', 'Wed'),
    # days_list = list(zip(days_fr, days))  # [('Dim', 'Sun'), ('Lun', 'Mon'), ('Mar', 'Tue'), ('Mer', 'Wed'),
    # days_set = set(zip(days_fr, days))  # {('Dim', 'Sun'), ('Lun', 'Mon'), ('Mar', 'Tue'), ('Mer', 'Wed'),

    # TODO: use iter on a string
    # i = iter("abcdefg")
    # print(next(i))  # a
    # print(next(i))  # b
    # iterator = iter("abcdefg")
    # for i in iterator:
    #     print(i)

    # TODO: use iter on a tuple
    # i = iter(("one", "two", "three", "four", "five"))
    # print(next(i))  # one
    # print(next(i))  # two

    # TODO: use iter on a set (unordered collection)
    # i = iter({"one", "two", "three", "four", "five"})
    # print(next(i))  # four
    # print(next(i))  # two

    # TODO: use iter on a dictionary (ordered collection)
    # i = iter({"one": 1, "two": 2, "three": 3, "four": 4, "five": 5})
    # print(next(i))  # one
    # print(next(i))  # two
    # print(next(i))  # three

    # TODO: use iter on a dictionary
    # d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    # for k in d:
    #     print(k, d[k])  # one 1, two 2, three 3, four 4, five 5

    # TODO: use iterkeys() to iterate over keys

    # TODO: use iter function instead of for loop and while loop
    # i = iter(days)
    # while True:
    #     try:
    #         print(next(i))
    #     except StopIteration:
    #         break

    # TODO: use itervalues() to iterate over values
    # d = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    # for k in d.values():
    #     print(k)

    # TODO: use iteritems() to iterate over key, value pairs
    # for k, v in d.items():
    #     print(k, v)  # one 1, two 2, three 3, four 4, five 5


if __name__ == "__main__":
    main()
