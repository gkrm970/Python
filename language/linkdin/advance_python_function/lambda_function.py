# Demonstrate the use lambda functions in place of simple functions

def fahrenheit_celsius(t):
    return (t - 32) * 5 / 9


def celsius_fahrenheit(t):
    return (t * 9 / 5) + 32


def main():
    c_temps = [0, 12, 34, 100]
    f_temps = [32, 65, 100, 212]

    # TODO : Use regular functions to convert temps
    print(list(map(fahrenheit_celsius, c_temps)))
    print(list(map(celsius_fahrenheit, f_temps)))

    # TODO : Use lambda functions to accomplish the same thing
    print(list(map(lambda t: (t - 32) * 5 / 9, f_temps)))
    print(list(map(lambda t: (t * 9 / 5) + 32, c_temps)))


if __name__ == "__main__":
    main()
