# This is my_string module where I have defined some string functions.


# my_text = "This is my_string module where I have defined some string functions."
# print(my_text.index("my_string"))
# print(my_text.index("my_string", 10))
# print(my_text.index("my_string", 10, 20))
# print(my_text.find("my_string"))
# print(my_text.find("my_string"))
# print(my_text.find("my_string", 10))
# print(my_text.find("my_string", 10, 20))
# print(my_text.count("my_string"))
# print(my_text.count("my_string", 10))
# print(my_text.rfind("my_string"))
# print(my_text.rfind("my_string", 10))
# print(my_text.rfind("my_string", 10, 20))


# print(my_text.isalnum())
# print(my_text.isalpha())

print('John'.isalnum())   # False because it contains only alphabets
print('John1990'.isalnum())
print('John 1990'.isalnum())
print('John_1990'.isalnum())
print('John-1990'.isalnum())

#
# print(my_text.isascii())
# isdigit = my_text.isdigit()
# print(isdigit)
# isdecimal = my_text.isdecimal()
# print(isdecimal)
# isnumeric = my_text.isnumeric()
# print(isnumeric)
# print(my_text.islower())
# print(my_text.isupper())
# print(my_text.isspace())
# print(my_text.istitle())
# print(my_text.isprintable())
# print(my_text.isidentifier())


# Join built-in function
# my_list = "This", "is", "my_string", "module", "where", "I", "have", "defined", "some", "string", "functions."
# print("  ".join(my_list))
# print(" # ".join(my_text))
# print(" ".join(my_text.split()))
# print(" ".join(my_text.split(" ", 3)))
# print(" ".join(my_text.split()))
# print(my_text.split())

# sorted() built-in function
# srt = sorted(my_text.split())
# print(srt)
# print(sorted(my_text.split(), reverse=True))
# # reverse false
# print(sorted(my_text.split(), reverse=False))
# # sort by length

sample_story = '''Once upon a time, there was a beginner programmer named Alice who was eager to learn Python. She tried to learn from books, but found it difficult to grasp the concepts. One day, she stumbled upon an online course.

Alice was thrilled. The course was taught by a well-known programmer who made the lessons interesting and easy to understand. The course covered everything a beginner programmer needed, and Alice was finally able to understand how to code in Python.'''

# pick the largest word from the story
# def get_largest_word(story):
#     story = story.replace(",", "").replace(".", "")
#     largest_word = ""
#     for word in story.split():
#         if len(word) > len(largest_word):
#             largest_word = word
#     return largest_word
