# create string variable

# Example 1  :  ways of creating string variables
# s="welcome"
# s='welcome'
# s=str('welcome')
# s=str("welcome")

# creating empty string variables
# name=""
# name=''
# name=str()

# Example 2  :  ways of creating string variables
# mutable-cannot change the value of variable
# immutable - can change the value of the variable

# string is immutable
# if the value is changed after update then it is immutable

# str1="welcome"
# print(id(str1))  #1831225521840
# str1=str1+"to python"
# print(id(str1)) #1630475397872


# Example 3  :  + and * with string
# str="welcome"
# print(str+"programming")   # concatenation/joining
# print(str*3)  #welcomewelcomewelcome

# Example4 : slicing  []
# starting index 0
# 0 1 2 3 4 5 6
# w e l c o m e
#-7-6-5-4-3-2-1

# str="welcome"

# print(str[1:3])  #el
# print(str[:6])  #welcom here starting index is 0 by default
# print(str[2:])   #lcome
# #
# print(str[1:-1])  #elcom last 1 char removed
# print(str[1:-2])  #elco last 2 chars removed
#

# Example5 : ord() and chr()
# print(ord('A'))  #65 # returns the ASCII code of the character.
# print(ord('B'))  #65 # returns the ASCII code of the character.
# print(chr(65))  #A  #returns character represented by a ASCII number.
# print(chr(66))  #A  #returns character represented by a ASCII number.
# # Usually 65,66,67,68........till it goes when A,B,C....Z
#
# print(chr(64))  # @  returns character represented by a ASCII number 64 .
# print(chr(63))  # ? returns character represented by a ASCII number 63 .
# print(chr(62))  # >  returns character represented by a ASCII number 62 .
# print(chr(61))  # =  returns character represented by a ASCII number 61 .


# Example6:   max()  min() len()
# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z
# 1,2,3,4,5,6,7,8,9,11,12....

# print(max('abc'))   #c
# print(min("abc"))   #a
# print(len("welcome"))   #7

# Example 7: in , not in operators  - returns true/false
# variable="welcome"
# print("come" in variable)  #True
# print("lome" in variable)  #False
# # #
# print("come" not in variable)  #False
# print("lome" not in variable)  #True



# Example8: String comparison

# Example9 : Testing strings  True/False
# s = "welcome to python"
# print(s.isalnum()) #False
# print("Welcome".isalpha()) #True
# print("2012".isdigit()) #True
# print("first Number".isidentifier())#False
# print(s.islower()) #True
# print("WELCOME".isupper()) #True
# print(" ".isspace()) #True
#

# Example10 : Searching for Substrings
# var = "welcome to python"
# print(var.endswith("thon")) #True
# #
# print(var.startswith("good")) #False
# #
# print(var.find("come"))  # 3
# print(var.find("become")) #-1   not found
# print(var.count("t")) #2   #Returns number of occurrences of substring the string


# Example11: Converting String
# s = "String in PYTHON"
# s1 = s.capitalize()
# print(s1) # String in python
# #
# s2 = s.title()
# print(s2)#String In Python
# #
# s3 = s.lower()
# print(s3) #string in python
# #
# s4 = s.upper()
# print(s4) #STRING IN PYTHON
# #
# s5 = s.swapcase()
# print(s5) #sTRING IN python
# #
# s6 = s.replace("in", "on")
# print(s6) # String on PYTHON

# Example12: Reverse a string
# Method1
# s="welcome"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str  # emoclew
# print("reversed string is:",rev_str) #emoclew

# Method2 --slicing method .
# s = "welcome"
# rev_str = s[::-1]  # s[0:7:-1]
# print(rev_str)  # emoclew
