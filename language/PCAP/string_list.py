"""
What does ASCII stand for?



Asynchronous Standard Computer Information Intelligence


American Standard Computer for Information Intelligence


American Standard Code for Information Interchange


American Studies and Code for Information Interchanged


How many Latin characters are stored in ASCII?



164


128


248


256


What is a code point?


A. A special variable in Python for the Latin characters


B. A number that is mapped to a character


C. A name for the upper 128 numbers


D. A part of a code page, which assigns numbers to different characters based on the language of the code page



A, D


B, C


D, B


C, A


How was internationalization implemented in computers?



ASCII got extended


Code pages for different languages were implemented


A new standard called UTF was designed


A new standard called Unicode was designed

why python3 is Internationalization-ready?
answer : Unicode is the default encoding for Python 3 and utf-8 is the default encoding for Python 2

Which of the following statements are true about strings in python?


A. Strings can be indicated with quotes, apostrophes, or triple quotes


B. Strings can be only one line


C. Strings can vary from one to multiple lines


D. Strings can be indicated with quotes or apostrophes



B, D


A, C


A, B

For the code snippet below, which of the following functions would work?


Note: try to guess without using the help of the terminal, because during the PCAP exams there is no terminal access support.


>>> fruit = 'orange'


A. del ord(fruit[1])


B. del fruit[1]


C. chr(ord(fruit[:1]))


D. fruit.index('o')


E. len(fruit[:1])



C, D, E


A, B, C


B, E, C


What is the output of print('orange'[::2])


Note: try to guess without using the help of the terminal



naro


or


gao


oag

What is the correct use of the escape character \, single and double quotes if we want the final output of the print statement to be The coffee house's name is "Plaza Cafe"


Note: try to guess without using the help of the terminal.


A. print('The coffee house's name is "Plaza Cafe"')


B. print('The coffee house\'s name is "Plaza Cafe"')


C. print("The coffee house's name is \"Plaza Cafe\"")


Open the file strings.py, and complete the code so that each letter of the variable my_string is duplicated and has two asterisks between the letters.

my_string = 'Blue skies'

# Iterate through the string here
for letter in my_string:
    print(letter*2, end='**')


Which method returns a string in all capital letters?



upper()


caps()


uppercase()


capitalize()

Which method returns a string with the first letter capitalized and the rest in lower case?



capitals()


title()


capitalize()

What does the center() method accomplish?



It centers on a word within a sentence


It returns the central letter of a string


It adds left and right padding between a string ---> its meaning is to add padding to the left and right of a string :


It returns the centered element from a list

Which of the following code snippets returns False?



"bicycle".endswith("cle")


"Black glasses".index("h")


"Black glasses".find("h")


"Cloudy weather".startswith("clo")

Let's do a recap of some of the methods we learned in the lecture.


isalnum() : Returns True if all the characters are alphanumeric, namely alphabet letter (a-z) and numbers (0-9).


What are non-alphanumeric characters?


These are symbols such as !#%&?, including <space>.


isalpha() : Check if all characters are alphabetic.


isascii() : Check if all the characters in the text are ASCII characters, which contains the numbers from 0-9, English letters from A to Z (upper and lower case), and some special characters. Total 128.


isdigit() : returns True if all the characters are digits, exponents, like ², are also considered to be a digit.


isnumeric() : Returns True if all the characters are numeric (0-9). Exponents, like ² and ¾ are also considered to be numeric values.


isdecimal() : Returns True if all the characters are decimals (0-9).


This method is used on Unicode objects.


islower() and isupper() return True or False based on the letter case of the string. And isspace() returns True if the string only includes one or more whitespaces.

What is the outcome of the following code?


>>> txt = "Company123!ψ"
>>> x = txt.isascii()
>>> print(x)

ValueError


False


True

What is the outcome of the following code?


>>> a = "\u0030" #unicode for 0
>>> b = "\u0047" #unicode for G
>>> print(a.isdecimal())
>>> print(b.isdecimal())

False

False


True

False


True

True

meaning of unicode

What is the outcome of the following code?


>>> txt = "50800"
>>> x = txt.isdigit()
>>> print(x)

True


False


ValueError

What is the outcome of the following code?


>>> a = "\u0030" #unicode for 0
>>> b = "\u00B2" #unicode for ²
>>> c = "-5"
>>> d = "5.5"
>>> print(a.isnumeric())
>>> print(b.isnumeric())
>>> print(c.isnumeric())
>>> print(d.isnumeric())


The index() method is almost the same as the find() and rfind() method,

the only difference is that the latter methods return -1

if the value is not found, while index() raises an exception.


They both take one required argument, and two optional:


string.find(value, start, end)

string.index(value, start, end)


Example:

# >>> txt = "Hello, welcome to python world."
# >>> x = txt.index("e", 5, 10)
# >>> y = txt.index("e")
# >>> print("index with all arguments: ", x, "\nindex with only the required argument: ", y)
index with all arguments:  8
index with only the required argument:  1


Try the above examples with the find() and rfind() methods and see if there are any differences.


Select the option which would return True:



'python'.index(' ')


'python'.sort()


'python'.rfind('o')


' \n '.isspace()





"""

print('The coffee house\'s name is "Plaza Cafe"')