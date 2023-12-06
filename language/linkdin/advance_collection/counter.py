# Demonstrate the usage of counter-objects


def main():
    # TODO : list of student in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah",
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # TODO : list of student in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # TODO : Create a Counter for class1 and class2
    from collections import Counter
    c1 = Counter(class1)
    c2 = Counter(class2)
    print(c1)
    print(c2)
    #
    # # TODO : How many students in class 1 named James?
    # print(c1["James"])
    #
    # # TODO : How many students are in class 1?
    # print(sum(c1.values()), "students in class 1")
    #
    # # TODO : Combine the two classes
    # # c1.update(class2)
    # # c3 = c1.__add__(c2)
    # c1.update(c2)
    # print(sum(c1.values()), "students in class 1 and 2")
    #
    # # TODO : What's the most common name in the two classes?
    # print(c1.most_common(3)) # the most common 3 names
    #
    # # TODO : Separate the classes again
    # c1.subtract(c2)
    # print(c1.most_common(2))
    # print(c2.most_common(2))

    # TODO : What's common between the two classes?
    print(c1 & c2)  # intersection: in both c1 and c2


if __name__ == "__main__":
    main()

# Application of Counter.
# 1. It is used to count hashable objects.
# 2. It is used to count objects in an iterable.
# 3. It is used to count objects in a dictionary.
# 4. It is used to count characters in a string.
# 5. It is used to count words in a sentence or a file.
# 6. It is used to count the frequency of each character in a string.
# 7. It is used to count the frequency of each word in a sentence or a file.
# 8. It is used to count the frequency of each line in a file.
# 9. It is used to count the frequency of each element in a list.
# 10. It is used to count the frequency of each element in a tuple.
# 11. It is used to count the frequency of each element in a dictionary.
# 12. It is used to count the frequency of each element in a set.
# 13. It is used to count the frequency of each element in a frozen set.
# 14. It is used to count the frequency of each element in a range.
# 15. It is used to count the frequency of each element in a bytes object.
# 16. It is used to count the frequency of each element in a bytearray object.
# 17. It is used to count the frequency of each element in a memoryview object.
# 18. It is used to count the frequency of each element in an array object.
# 19. It is used to count the frequency of each element in a deque object.
# 20. It is used to count the frequency of each element in a chainmap object.
# 21. It is used to count the frequency of each element in a userdict object.
# 22. It is used to count the frequency of each element in a userlist object.
# 23. It is used to count the frequency of each element in a userstring object.
# 24. It is used to count the frequency of each element in a defaultdict object.
# 25. It is used to count the frequency of each element in an ordereddict object.
# 26. It is used to count the frequency of each element in a namedtuple object.
# 27. It is used to count the frequency of each element in a counter object.
# 28. It is used to count the frequency of each element in a deque object.
