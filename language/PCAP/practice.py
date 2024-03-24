def division():
    global number1, number2
    try:
        number1 = input("Enter a number: ")
        number2 = input("Enter another number: ")
        if not (number1.isnumeric() and number2.isnumeric()):
            raise ValueError("Please enter valid numbers.")
        if float(number2) == 0:
            raise ZeroDivisionError("Zero division error, please try again.")
        else:
            print(float(number1) / float(number2))
    except ValueError as ve:
        print(ve)

    except ZeroDivisionError as zde:
        print(zde)
    except:
        print("Hmm, something went wrong, try again.")


division()
