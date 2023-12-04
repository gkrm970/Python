# List comprehensions.
# output_list = [output_exp for var in input_list if (var satisfies this condition)]
# Constructing output list WITHOUT
# Using List comprehensions
# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
#
# output_list = []
#
# # Using loop for constructing an output list
# for var in input_list:
#     if var % 2 == 0:
#         output_list.append(var * 2)
#
# print("Output List using for loop:", output_list)

# Using List comprehensions for constructing an output list
# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
#
# list_using_comp = [var * 2 for var in input_list if var % 2 == 0]
#
# print("Output List using list comprehensions:", list_using_comp)

# Dictionary comprehension
# input_list = [1, 2, 3, 4, 5, 6, 7]
#
# output_dict = {}
#
# # Using it for loop for constructing output dictionary.
# for var in input_list:
#     if var % 2 != 0:
#         output_dict[var] = var ** 3
#
# print ("Output Dictionary using for loop:", output_dict)

# Using Dictionary comprehensions for constructing output dictionary
# input_list = [1, 2, 3, 4, 5, 6, 7]
# dict_using_comp = {var: var ** 3 for var in input_list if var % 2 != 0}
#
# print("Output Dictionary using dictionary comprehensions:", dict_using_comp)

# state = ['Gujarat', 'Maharashtra', 'Rajasthan']
# capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
#
# output_dict = {}
# # # Using loop for constructing output dictionary
# for key, value in zip(state, capital):
# 	output_dict[key] = value
#
# print("Output Dictionary using for loop:", output_dict)
#
# # Using Dictionary comprehensions for constructing output dictionary
#
# state = ['Gujarat', 'Maharashtra', 'Rajasthan']
# capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
#
# dict_using_comp = {key: value for (key, value) in zip(state, capital)}
#
# print("Output Dictionary using dictionary comprehensions:",
#       dict_using_comp)
#
# # Set Comprehensions:
# # Using loop for constructing output set
# input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# output_set = set()
# for var in input_list:
# 	if var % 2 == 0:
# 		output_set.add(var)
#
# print("Output Set using for loop:", output_set)

# # Using Set comprehensions for constructing an output set
# input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# set_using_comp = {var for var in input_list if var % 2 == 0}
#
# print("Output Set using set comprehensions:",
#       set_using_comp)

# # Generator Comprehensions: syntax is similar to list comprehensions, but we use () instead of []
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = (var for var in input_list if var % 2 == 0)
for var in output_gen:
    print(var, end=' ')
