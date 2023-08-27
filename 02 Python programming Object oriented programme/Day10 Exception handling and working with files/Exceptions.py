# Example1
# print("this is starting point of program...")
# print("this is starting point of program...")
# print("this is starting point of program...")

# try:
#     print("xyz")
# except:
#     print("Exception occurred")

# print("this is end of the program..")
# print("this is end of the program..")
# print("this is end of the program..")

# Example2
print("This is starting point of program.....")
print("Program in progress")
try:
    print(5/0)   #2.0
except:
    print("Exception occurred and handled..")

# print("Program completed...")

# Example3 : Multiple except blocks  - try, except else, finally
# try:
#     num1,num2=10,2
#     result=num1/num2
#     print("result is:",result)
# except ZeroDivisionError:
#     print("Thrown ZeroDivisionError exception....")
# except SyntaxError:
#     print("Thrown Syntax error exception...")
# except:
#     print("Exception handled...")
# else:
#     print("No exceptions occurred...")
# finally:
#     print("always execute...")

# Example4 : raising our own exceptions
# def enterage(num):
#     if num<0:
#         raise ValueError("Only Integers are allowed")
#     if num%2==0:
#         print("even")
#     else:
#         print("odd")
# # enterage(-1)
#
# print("checking number is even or odd by calling function..")
# num=0
# try:
#     enterage(num)
# except ValueError:
#     print("value error exception occurred and handled..")
# print("program completed....")
#
