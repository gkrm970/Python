# Demonstrate how to use set comprehension

def main():
    # define two sets of numbers
    evens = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    odds = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
    c_temps = [0, 12, 34, 100, 100]

    f_temps1 = [((t * 9 / 5) + 32) for t in c_temps]  # list comprehension
    f_temps2 = {(t * 9 / 5) + 32 for t in c_temps}  # set comprehension
    print(f_temps1)
    print(f_temps2)

    # TODO: build a set of unique Fahrenheit temperatures

    # TODO: build a set from an input source
    s_temp = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in s_temp if not c.isspace()}
    print(chars)

    # Perform a mapping and filter function on a list
    even_squared = list(map(lambda e: e ** 2, filter(lambda e: 4 < e < 16, evens)))
    print(even_squared)

    # Derive a new set of numbers from a given set using set comprehension
    even_squared = {e ** 2 for e in evens}
    print(even_squared)

    # Limit the items operated on with a predicate condition
    odd_squared = {e ** 2 for e in odds if 3 < e < 17}
    print(odd_squared)


if __name__ == "__main__":
    main()
