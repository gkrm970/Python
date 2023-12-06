# demonstrate the use of templete string
import string


def main():
    # Usual string formatting with format()
    a = "This is a string"
    print(type(a), a)  # <class 'str'> This is a string

    # create a template with placeholders
    t = string.Template("This is a $thing ${name} ${name} ${name}")
    print(type(t), t)

    # use the substitute method with keyword arguments
    s = t.substitute(thing="gk", name="Python")
    print(type(s), s)  # <class 'str'> This is a gk Python Python Python

    # use the substitute method with a dictionary
    d = {"thing": "gk", "name": "Python"}
    s = t.substitute(d)
    print(type(s), s)  # <class 'str'> This is a gk Python Python Python




if __name__ == "__main__":
    main()
