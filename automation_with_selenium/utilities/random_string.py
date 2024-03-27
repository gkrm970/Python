import random
import string


def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    _str = random.choice(chars)
    return "".join(_str for x in range(size))


print(random_string_generator(size=5, chars=string.ascii_lowercase + string.digits))
