# expressions
# ----------------
# 1. \b    The backslash-b (\b) metacharacter represents a word boundary.
#     For instance, the regular expression [a-zA-Z]+\b matches any sequence of one or more
#     alphabetic characters followed by a word boundary.

# \bcat\b matches "cat" but not "catnap"
# \bcat\b also matches "cat" but not "concatenate"

# \bthe\b matches "the" but not "them" or "there"
# \bthe\b also matches "the" but not "other" or "another"

# \bend\b matches "end" but not "ending"
# \bend\b also matches "end" but not "send" or "endless"

# \b...\b matches any three-letter word

# Example: # I want to fetch the repeated "cat" words from the sentence

# import re
# text = "cat bat cat cattie cat"
# r"\bcat\b" = r"\bcat\b"

# matches = re.findall(regex_expre, text)
# print(matches)

# Example: # I want to fetch the following statement from the sentence "the quick brown fox jumped over the lazy dog",
# the\bquick\bbrown\bfox\bjumped\bover\bthe\blazy\bdog matches the whole sentence
# "the quick brown fox jumped over the lazy dog" but not "the quick brown foxes jumped over the lazy dogs"

# import re
# text = "the quick brown fox jumped over the lazy dog"
# regex_expre = r"\bthe\bquick\bbrown\bfox\bjumped\bover\bthe\blazy\bdog"
# matches = re.findall(regex_expre, text)
# print(matches)

# Example: I want to fetch onle email address from the sentence
# import re
# text = "my email address is: abc@gmail.com"
# regex_expre = r"\b[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9.]+"
# matches = re.findall(regex_expre, text)
# print(matches)

# Example2:


# 2. \d
#
# The backslash-d (\d) metacharacter represents a digit. It matches any single digit character from 0 to 9.
#     For instance, the regular expression \d{3} matches any three-digit number, such as "123" or "456".
# \d{3} matches "123" but not "1234"
# \d{3} also matches "456" but not "4567"
# \d{3}-\d{3}-\d{4} matches "123-456-7890" but not "123-4567-890"
# \d{3}\s\d{3}\s\d{4} matches "123 456 7890" but not "123 4567 890"
# \d{3}[-\s]\d{3}[-\s]\d{4} matches "123-456-7890" but not "123-4567-890"

# Example: I want fetch my mobile number from the sentence
# import re
# text = "my mobile number is: +91-123-456-7890 and my office number is: is +918123453849"
# regex_expre = r"\+\d{2}-\d{3}-\d{3}-\d{4}" or r"\+\d{2}\d{10}"
# matches = re.findall(regex_expre, text)
# print(matches)
# for match in matches:
#     print(match)


# 1. Data Validation:
#
# Example: Validating email addresses


import re

# email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{1,64}@[a-zA-Z0-9-]{1,255}\.[a-zA-Z-]{2,}$"
#
#
# def is_valid_email(email):
#     if re.match(email_regex, email):
#         return True
#     else:
#         return False
#
#
# user_email = input("Enter your email address: ")
# if is_valid_email(user_email):
#     print("Valid email address")
# else:
#     print("Invalid email address")

# Explanation:
# This code defines a regular expression pattern for valid email addresses and uses the re.match() function to check
# whether a given email address matches the pattern.

# The pattern is as follows:
# 1. The local part of the email address may consist of alphanumeric characters, plus the following special characters:
# !#$%&'*+/=?^_`{|}~
# 2. The local part may be from 1 to 64 characters long.
# 3. The domain part of the email address may consist of alphanumeric characters, dashes (-) and dots (.).
# 4. The domain part may have a maximum of 255 characters.
# 5. The domain part must be at least 2 characters long.
# 6. The email address must be between 3 and 254 characters long.

# The re.match() function returns a match object on success, None on failure. Since None evaluates to False,
# the above code works fine.
# The re.match() function matches the pattern against the entire string, whereas re.search() matches the pattern
# against the string, but this match may be located anywhere in the string.

# 2. Data Extraction:
# Example: Extracting phone numbers
# Suppose you have a text file containing phone numbers, written in various formats. You want to extract all the phone
# numbers.
# The following code extracts all the phone numbers from the file.
# The regular expression pattern for a phone number is r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b".
# Let's break it down:
# 1. \b matches a word boundary (the start or end of a word).
# 2. \d{3} matches 3 digits.
# 3. [-.]? matches an optional - or . character.
# 4. \d{3} matches 3 digits.
# 5. [-.]? matches an optional - or . character.
# 6. \d{4} matches 4 digits.

# Example1: Extracting phone numbers
# import re
#
# phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
#
# with open("data.txt", "r") as file:
#     data = file.read()
#     matches = re.findall(phone_regex, data)
#     print(matches)

# Explanation:

# The re.findall() function returns a list of all matches. If no match is found, an empty list is returned.
# The \b in the pattern indicates a word boundary, so only the distinct phone numbers are matched.
# The r prefix before the pattern string indicates that it is a raw string. It changes how the string literal is
# interpreted. Such strings are useful when we use regular expressions in various ways, as we will see shortly.
# The \d represents any digit, and {3} repeats this rule three times.
# The question mark makes the preceding group optional. The pattern matches zero or one hyphen.
# The period matches any character, except newline characters. The question mark again makes the period optional.

# Example2: Extracting URLs

# import re
#
# text = "This website is very useful: https://www.example.com. Check out their blog: https://blog.example.com."
#
# url_regex = r"https?://\S+"
#
# matches = re.findall(url_regex, text)
# print(matches)
# for match in matches:
#     print(match)

# Explanation:

# https?: This part matches either "http" or "https" because the 's' is made optional by the ? quantifier.
# ://: Matches the "://" part of the URL.
# \S+: Matches one or more non-whitespace characters, representing the rest of the URL.

# 3. Data Cleaning:
# Example: Removing HTML tags
# Suppose you have a text file containing HTML tags. You want to remove all the tags.
# The following code removes all the HTML tags from the file.
# The regular expression pattern for an HTML tag is r"<.*?>"
# Let's break it down:
# 1. < matches the < character.
# 2. .* matches all characters except newline characters.
# 3. > matches the > character.

# Example: Removing HTML tags
# import re
#
# html_regex = r"<.*?>"
#
# with open("data.txt", "r") as file:
#     data = file.read()
#     data = re.sub(html_regex, "", data)
#     print(data)

# Explanation:
# The re.sub() function replaces all matches of the pattern in a string with a replacement string.
# The replacement string can be empty, to delete matches.
# The re.sub() function returns the modified string as output.
# The r prefix before the pattern string indicates that it is a raw string. It changes how the string literal is
# interpreted. Such strings are useful when we use regular expressions in various ways, as we will see shortly.
# The .* matches all characters except newline characters.
# The ? makes the .* lazy, i.e., it matches as few characters as possible.
# The ? after the > character makes it match the first occurrence of >.

# 3. Pattern Matching:
# Example: Extracting all words
# Suppose you have a text file containing words. You want to extract all the words.
# The following code extracts all the words from the file.
# The regular expression pattern for a word is r"\w+".
# Let's break it down:
# 1. \w matches any alphanumeric character.
# 2. + matches one or more of the preceding character.

# Example: Extracting all words
# import re
#
# word_regex = r"\w+"
#
# with open("data.txt", "r") as file:
#     data = file.read()
#     matches = re.findall(word_regex, data)
#     print(matches)

# Example
import re

# text = "This document contains the keywords 'machine learning' and 'artificial intelligence'."
#
# keyword_regex = r'\b(machine learning|artificial intelligence)\b'
#
# matches = re.findall(keyword_regex, text)
# for match in matches:
#     print(match)

# Explanation: This code defines a regular expression pattern for the keywords "machine learning" and "artificial
# intelligence" and uses the re.findall() function to identify all occurrences of these keywords in the given text.

# The pattern is as follows:
# 1. The \b matches a word boundary (the start or end of a word).
# 2. The | character matches either the pattern to the left or the pattern to the right.
# 3. The () groups patterns together.
# 4. The machine learning and artificial intelligence are the two keywords we want to match.

# 4. Search and Replace:
# Example: Replacing words
# Suppose you have a text file containing words. You want to replace all occurrences of a word with another word.
# The following code replaces all occurrences of the word "dog" with "cat".
# The regular expression pattern for the word "dog" is r"\bdog\b".
# Let's break it down:
# 1. \b matches a word boundary (the start or end of a word).
# 2. dog matches the word "dog".

# Example: Replacing words
# import re
#
# word_regex = r"\bdog\b"
#
# with open("data.txt", "r") as file:
#     data = file.read()
#     data = re.sub(word_regex, "cat", data)
#     print(data)

# Explanation:
# The re.sub() function replaces all matches of the pattern in a string with a replacement string.
# The replacement string can be empty, to delete matches.
# The re.sub() function returns the modified string as output.
# The r prefix before the pattern string indicates that it is a raw string. It changes how the string literal is
# interpreted. Such strings are useful when we use regular expressions in various ways, as we will see shortly.
# The \b matches a word boundary (the start or end of a word).
# The dog matches the word "dog".

# 5. Splitting a String:
# Example: Splitting a string

# import re
#
# text = "This is a sentence. This is another sentence. This is the last sentence."
#
# sentences = re.split(r"\. ", text)
# print(sentences)

# Explanation:
# The re.split() function splits a string into substrings using a regular expression.
# The re.split() function returns a list of substrings.
# The r prefix before the pattern string indicates that it is a raw string. It changes how the string literal is
# interpreted. Such strings are useful when we use regular expressions in various ways, as we will see shortly.
# The \. matches the . character.

# 4. Search and Replace:
# Example: Replacing all occurrences of 'a' with 'A' in a text file
#
# import re
#
# with open('myfile.txt', 'r') as file:
#     text = file.read()
#
# new_text = re.sub('a', 'A', text)
#
# with open('myfile.txt', 'w') as file:
#     file.write(new_text)

# Explanation:
# This code reads the contents of a text file, replaces all occurrences of 'a' with 'A' using the re.sub()
# function, and then writes the modified text back to the file.

# Text Processing:
#
# Example: Removing HTML tags from text

# import re
#
# text = ("<p>This paragraph contains HTML tags: <b>bold</b>, <i>italic</i>, and <a "
#         "href='https://www.example.com'>link</a>.</p>")
#
# html_tag_regex = r'<[^>]*>'
#
# clean_text = re.sub(html_tag_regex, '', text)
# print(clean_text)

# Explanation:
#
# This code defines a regular expression pattern for HTML tags and uses the re.sub() function to remove all HTML tags
# from the given text, resulting in plain text.

# The pattern is as follows:
# 1. The < matches the < character.
# 2. The [^>]* matches zero or more characters that are not >.
# 3. The > matches the > character.


# Advanced Regular Expressions:

# 1. Quantifiers:
# Quantifiers are used to specify the number of occurrences of a character or a group of characters.
# Example: Matching a phone number
# Suppose you have a text file containing phone numbers, written in various formats. You want to extract all the phone
# numbers.
# The following code extracts all the phone numbers from the file.


# import re
#
# phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
#
# with open("data.txt", "r") as file:
#     data = file.read()
#     matches = re.findall(phone_regex, data)
#     print(matches)

# Explanation:
