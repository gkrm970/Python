# Example1
# print("this is a starting point of program...")
# print("this is a starting point of program...")
# print("this is a starting point of program...")

# try:
#     print("xyz")
# except:
#     print("Exception occurred")

# print("this is end of the program.")
# print("this is end of the program..")
# print("this is end of the program..")

# Example2
# print("This is starting point of program.....")
# print("Program in progress")

# try:
#     print(5 / 0)
# except:
#     print("Exception occurred and handled.")

# print("Program completed...")

# Example3 : Multiple except blocks  - try, except else, finally
# try:
#     num1, num2 = 10, 2
#     result = num1 / num2
#     print("result is:", result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception....")
# except SyntaxError:
#     print("Thrown Syntax error exception...")
# except Exception as e:
#     print("Exception handled... ", e)
# else:
#     print("No exceptions occurred...")
# finally:
#     print("always execute...")

# Example4: raising our own exceptions
def enter_age(number):
    if number < 0:
        raise ValueError("Only Integers are allowed")
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


enter_age(-1)
#
print("checking number is even or odd by calling function.")
number = 0
try:
    enter_age(number)
except ValueError:
    print("value error exception occurred and handled..")

except TypeError:
    print("Type error exception occurred and handled..")

except ZeroDivisionError:
    print("ZeroDivisionError exception occurred and handled..")

except SyntaxError:
    print("SyntaxError exception occurred and handled..")

except NameError:
    print("NameError exception occurred and handled..")

except AttributeError:
    print("AttributeError exception occurred and handled..")

except Exception as e:
    print("Exception occurred and handled..", e)
finally:
    print("program completed....")

