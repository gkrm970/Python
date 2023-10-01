import random


# print(random.random())
# print(random.random())
# print(random.random())

# The random.seed() function is used to initialize the pseudorandom number generator in Python. The random.seed()
# function accepts only one parameter, which is an integer number. The random.seed() function is often used together
# seed() function is often used for debugging purposes, as it allows you to get the same random numbers whenever you
# run your program. This is especially useful when you're trying to debug a program that uses random numbers.
# print(random.seed(10))
# print(random.random())
# print(random.random())
# print(random.random())

# numbers = [1, 2, 3, 4, 5, 6]  # A list of numbers
# names = ["John", "Eric", "Jessica"]  # A list of names
# print(random.choice(numbers))
# print(random.choice(names))
#
# for i in range(10):
#     print(random.choice(names), sep="#")
#
# names = ["John", "Eric", "Jessica", "Jason", "Adam", "Bart", "Lisa"]
#
# print(random.sample(names, 3))
# print(random.sample(names, 5))
# print(random.sample(names, 7))
# print(random.sample(names, 2))
#

# Example 2:

def generate_tickets(ticket_count, max_number):
    # Generate a list of random unique integers
    numbers = random.sample(range(max_number), ticket_count)

    # Choose one random element as the winning number
    winning_number = random.choice(numbers)

    return numbers, winning_number


# Example usage:
result = generate_tickets(5, 10)
print(result)


# Example 1:


def generate_tickets(ticket_count, max_number):
    list_to_return = random.sample(range(0, max_number), ticket_count)
    return list_to_return, random.sample(list_to_return, 1)[0]
