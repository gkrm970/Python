# Strings and bytes are not directly interchangeable
# Strings contain unicode, bytes are raw 8-bit values

# Python 3 uses unicode for strings by default (Python 2 uses ASCII)
# Python 3 uses bytes for binary data (Python 2 uses str)

def main():
    # define some starting values
    # using the b prefix for bytes
    a = b"this is a bytes string"
    a = bytes([0x41, 0x42, 0x43, 0x44])  # bytes from a list of values
    print(type(a), a)  # <class 'bytes'> b'this is a byte string'
    # using the u prefix for unicode
    b = u"this is a unicode string"
    print(type(b), b)

    # try combining them (fails)
    # c = a + b # TypeError: can't concat bytes to str
    # print(c)

    # Bytes and strings need to be properly encoded and decoded
    # before you can work on them together
    # decode the bytes to an unicode string
    a2 = a.decode("utf-8")  # decode bytes to unicode
    print(type(a2), a2)  # <class 'str'> this is a bytes string

    # now concatenate
    c = a2 + b
    print(c)  # this is a byte string-this is an unicode string

    # encode the unicode string to bytes
    c2 = c.encode("utf-8")  # encode unicode to bytes
    print(type(c2), c2)  # <class 'bytes'> b'this is a bytes string-this is an unicode string'

    # now combine the two properly encoded values
    d = a + c2
    print(d)  # b'this is a bytes stringthis is a bytes string-this is an unicode string'utf-8

    # encode the string to UTF-32
    a3 = a.decode("utf-8").encode("utf-32")
    print(type(a3), a3)  # <class 'bytes'> b'\xff\xfe\x00\x00A\x00\x00\x00B\x00\x00\x00C\x00\x00\x00D\x00\x00\x00'

    # decode UTF-32 back to a string
    a4 = a3.decode("utf-32")
    print(type(a4), a4)  # <class 'str'> ABCD

    # encode the string to latin-1
    a5 = a.decode("utf-8").encode("latin-1")
    print(type(a5), a5, "a5")  # <class 'bytes'> b'ABCD' a5


if __name__ == "__main__":
    main()
