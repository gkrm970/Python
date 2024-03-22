"""

So far, we have seen how slicing can reverse a string. Another built-in function for doing so is the reversed(d). However, it works slightly differently. For example:


>>> reversed('shop')
>>> <reversed object at 0x7f41a310def0>
>>> for i in reversed('shop'):
...  print(i)
...
p
o
h
s


What is the output of the following code?


Note: try to solve it without using the terminal.


chars = "1234"
char = ""
for char in reversed(chars):
    char += char

print(char)

cc
4321
10
11

Answer is 11


movie = "My    beautiful\n laundrette!"

# Create a list of the above string
# without extra spaces nor new lines
movie = movie.split()
print(movie)

# Use slices, concatenation, and list index all in one line
# to join the elements of the list excluding the exclamation mark
movie = " ".join(movie[:-1]) + " " + movie[-1][:-1]

# Change the word laundrette to garden
movie = movie.replace('laundrette', 'garden')

# Capitalize only the first character of each word and print the new string
print(movie.title())

txt = ",$,,   chocolate   banana ice-cream..."

# Add more options in the strip()
txt = txt.strip(",$ .")

# Clear any space left and print the outcome
txt = " ".join(txt.split())
print(txt)

Which of the following code snippets return False?


A. 'Python' > 'python'


B. 'python2' < 'python'


C. 'python1' < 'python2'


D. 'python' < 'python'

Answer: D A


Which of the following code snippets return True?


A. 'cDe'.lower() < 'CD' -->

B. 'cdE' > 'cde'


C. 'cde'.upper() < 'cde'


D. 'Vanilla' == 'vanilla'.title()

Answer: C


Which of the following code snippets return True?


A. "in not" not in "is not there?"


B. "in" not in "many fruits in the basket"


C. "in not" in "not in time yet"


D. "not" in "… and whatnot"

Answer: A


Which of the following code snippets returns True?

'10' > '8'


'20' > '8'


'21' == '021'


'10' > '010'

Answer: '10' > '010'

#  ascci number for 8 is 56
#  ascci number for 0 is 48


What is the output of the following code snippet?


'10' != 10 --> true
'10' == 10 --> false
'10' > 10 -->error


What is the output of the following code snippet?


min('duck') > max('Duck')   ---> false
min('duck') > min('Duck') ---> false
max('12 AB') == min('aBD')  ---> true


What is the output of the following code snippet?


val1 = '22aaa2'.count('a')   ---> 3
val2 = list('mmm').count('m')
val1 == val2

Answer: True
False
ValueError
TypeError
True

What is the output of the following code snippet?


Note: Try to guess without accessing the terminal.

x = str(1 // 3)
var = ""
for i in x:
    x = x + var
print(x[-1])


Answer: 0

What is the output of the following code snippet?


l1 = 'manuals how-tos docs'.split()
l2 = sorted(l1)
print(l1 == l2)
l3 = l1.sort()
print(l1 == l2)
print(l3 == l1)

True

True

False


True

False

True


False

True

False

What is the output of the following code snippet?


>>> l1 = 'manuals how-tos docs'.split()
>>> l2 = sorted(l1)
>>> print(l1 == l2)
>>> l3 = l1.sort()
>>> print(l1 == l2)
>>> print(l3 == l1)

False
True
False

how to convert string to integer in python ?
answer : int() function is used to convert string to integer in python


Which of the following methods and functions are for strings only?

append
sorted() --> sorted() function is used to sort the elements of a list in ascending order
extend()
sort()

Out of the options you listed, only append is specifically designed for strings.

Here's a breakdown of why the others are not exclusive to strings:

sorted(): This function can be used to sort any iterable object, not just strings. It can sort lists, tuples, dictionaries (by key), and other data structures.
extend(): This function is typically used with lists. It adds all the elements from an iterable (like another list or string) to the end of the original list.
sort(): This method is used for sorting elements in-place within a list. Similar to sorted(), it can sort various data types within a list.


Which of the following methods are for lists only?
answer: sort(), sum() and append() methods are for lists only


sorted()
count()
sum()
index()

Which of the following methods are for both strings and lists?

min()
find()
split()
sort()

Select the correct output of the following code:


>>> l1 = [1, 2, 3, 1, 2, 3, 2, 1]
>>> l1.index(3, 4)

Answer:5


Did you know the list's sort() method has a reverse flag?

yes


Can you guess the output of:


>>> l = [3.3, 2.225, 1, 9.30, 0.64, 5.5]
>>> l.sort(reverse=True)
>>> print(l)


[9.3, 5.5, 3.3, 2.225, 1, 0.64]

What is the expected output of the following code snippet?


>>> p_string = 'pumpkin soup'.count('p', 2)
>>> p_list = 'pumpkin soup'.split().count('p')
>>> str(p_string) > str(p_list)

True


False


TypeError


ValueError



Open the file cipher_encrypt.py, and complete the function that encrypts a string. The string comes from user input. Make use of a simple Caesar cipher algorithm, which shifts each letter of the alphabet to the next one.


For more info about Caesar's encryption, see here: https://en.wikipedia.org/wiki/Caesar_cipher

msg = input("Enter your message to encrypt: ")


def encrypt(msg):
    result = ""

    # iterate through the input msg
    for i in range(len(msg)):
        char = msg[i]
        # Check if character is alphanumeric

            # Check char is either Z or z and append A, a respectively




            # Else shift to the next letter


        # If char not alphanumeric just continue

        return result


print("Message to encrypt : ", msg)
print("Cipher: ", encrypt(msg))



Open the file cipher_decrypt.py, and complete the program which takes as input an encrypted text from the previous exercise and decrypts it.

cipher = input('Enter your encrypted message: ')


def decrypt(cipher):
    result = ""
    # Iterate through the cipher

        # Check whether character is alphanumeric

            # Check whether character is A or a, replace with Z or z




            # Else shift letter one below
            else:

        # Else append character as it is
        else:
            result += char

    return result


print("Cipher was :", cipher)
print("Decrypted message is :", decrypt(cipher))



"""
