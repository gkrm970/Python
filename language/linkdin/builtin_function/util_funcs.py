# demonstrate the use of the built-in utility functions
# any(), all(), min(), max(), sum()
# Apllication of any(), all(), min(), max(), sum() functions in python 3 and above versions of python 3 are shown here
# any() and all() functions are used to check the boolean values of the sequence
# min() and max() functions are used to find the minimum and maximum values of the sequence
# sum() function is used to find the sum of all the values in the sequence


def main():
    # TODO: use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 0, 5, 6]
    # TODO: any will return true if any of the sequence values are true
    print(any(list1))
    # all will return true only if all values are true
    print(all(list1))
    # TODO: min and max will return minimum and maximum values in a sequence
    print("min: ", min(list1))
    print("max: ", max(list1))
    # TODO: use sum() to sum up all of the values in a sequence
    print("sum: ", sum(list1))


if __name__ == "__main__":
    main()
