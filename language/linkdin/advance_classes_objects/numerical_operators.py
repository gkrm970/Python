# Numerical functions
# object.__add__(self, other) - addition (+) operator        call when self + other
# object.__sub__(self, other) - subtraction (-) operator     call when self - other
# object.__mul__(self, other) - multiplication (*) operator  call when self * other
# object.__floordiv__(self, other) - floor division (//) operator call when self // other
# object.__truediv__(self, other) - division (/) operator    call when self / other
# object.__mod__(self, other) - modulo (%) operator          call when self % other
# object.__pow__(self, other) - exponent (**) operator       call when self ** other
# object.__lshift__(self, other) - left bitwise shift (<<) operator call when self << other
# object.__rshift__(self, other) - right bitwise shift (>>) operator call when self >> other
# object.__and__(self, other) - bitwise AND (&) operator     call when self & other
# object.__xor__(self, other) - bitwise XOR (^) operator     call when self ^ other
# object.__or__(self, other) - bitwise OR (|) operator       call when self | other

# object.__iadd__(self, other) - inplace addition (+=) operator call when self += other
# object.__isub__(self, other) - inplace subtraction (-=) operator call when self -= other
# object.__imul__(self, other) - inplace multiplication (*=) operator call when self *= other
# object.__ifloordiv__(self, other) - inplace floor division (//=) operator call when self //= other
# object.__itruediv__(self, other) - inplace division (/=) operator call when self /= other
# object.__imod__(self, other) - inplace modulo (%=) operator call when self %= other
# object.__ipow__(self, other) - inplace exponent (**=) operator call when self **= other
# object.__ilshift__(self, other) - inplace left bitwise shift (<<=) operator call when self <<= other
# object.__irshift__(self, other) - inplace right bitwise shift (>>=) operator call when self >>= other
# object.__iand__(self, other) - inplace bitwise AND (&=) operator call when self &= other
# object.__ixor__(self, other) - inplace bitwise XOR (^=) operator call when self ^= other
# object.__ior__(self, other) - inplace bitwise OR (|=) operator call when self |= other


# give object numeric-like behavior

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Use this repr function to override the default repr function
        """
        return '<Point Class - x:{0}, y:{1}>'.format(self.x, self.y)

    # TODO: implement addition
    def __add__(self, other):
        """
        Use this add function to override the default add function
        """
        return Point(self.x + other.x, self.y + other.y)

    # TODO: implement subtraction
    def __sub__(self, other):
        """
        Use this sub function to override the default sub function
        """
        return Point(self.x - other.x, self.y - other.y)

    # TODO: implement in-place addition
    def __iadd__(self, other):
        """
        Use this iadd function to override the default iadd function
        """
        self.x += other.x
        self.y += other.y
        return self

    # TODO: implement in-place subtraction

    # TODO: implement multiplication

    # TODO: implement in-place multiplication


def main():
    # declare some points
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(p1, p2)

    # TODO: add two points
    p3 = p1 + p2
    print(p3)

    # TODO: subtract two points
    p4 = p2 - p1
    print(p4)

    # TODO: perform inplace addition
    p1 += p2
    print(p1)


if __name__ == "__main__":
    main()
