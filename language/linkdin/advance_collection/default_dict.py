# Demonstrate the usage of default objects

def main():
    # TODO : define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # TODO: use a dictionary to count each element
    # fruit_counter = {}
    # for fruit in fruits:
    #     if fruit in fruit_counter.keys():
    #         fruit_counter[fruit] += 1
    #     else:
    #         fruit_counter[fruit] = 1
    #
    # print(fruit_counter)

    # TODO : use the default-dict instead
    from collections import defaultdict
    fruit_counter = defaultdict(int)
    # fruit_counter = defaultdict(lambda: 100)  # the default value is 100 on each key on the top will add
    for fruit in fruits:
        fruit_counter[fruit] += 1

    print(fruit_counter)

    # TODO : Create a dictionary of names and scores
    my_dict = {'a': 10, 'b': 20, 'c': 30}
    print(my_dict.keys())
    # I want to print the value of key 'd' if it does not exist then print 100
    print(my_dict.get('d', 100))
    # I want to print the value of key 'a'
    print(my_dict.get('a'))
    # I want to print the key of value 10
    print(list(my_dict.keys())[list(my_dict.values()).index(10)])


if __name__ == "__main__":
    main()
