# Example1: creating dictionary
# mydic={101:"x",102:"y",103:"z"}
# print(mydic) #{101: 'x', 102: 'y', 103: 'z'}

# Example2: access items from dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2021
# }
# print(mydic["brand"])  # Hyudai
# print(mydic["model"]) #i10
# # using get()
# print(mydic.get("brand")) #Hyudai

# Example3: change values in dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
# }
# print(mydic) # {'brand': 'Hyudai', 'model': 'i10', 'year': 2020}
# mydic["year"]=2021    # new value
# print(mydic) #{'brand': 'Hyudai', 'model': 'i10', 'year': 2021}

# Example4: reading items from dictionary using loop
# mydic={
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2020
# }
#
# for i in mydic:
#     print(i)   # prints only keys from dictionary
#
# for i in mydic:
#     print(mydic[i])    # prints only values from dictionary

# for i in mydic.values():
#     print(i)  # prints only values from dictionary

# for x,y in mydic.items():
#     print(x,y)    # print keys along with the value

# Example5: check key is exist in dictionary or not
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
#  }
#
# if "model1" in mydic:
#     print("exist")
# else:
#     print("not exist")

# print("model" in mydic)  # True

# Example6: find number of items in dictionary
# mydic={
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2020
#  }
# print(len(mydic))  #3

# Example7: Adding items to dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
#  }
# mydic["color"]="red"
# print(mydic) #{'brand': 'Hyudai', 'model': 'i10', 'year': 2020, 'color': 'red'}

# Example8: Remove item from dictionary
# mydic={
#     "brand": "Hyudai",
#     "model": "i10",
#     "year": 2020
#  }
# mydic.pop("year")
# print(mydic) # {'brand': 'Hyudai', 'model': 'i10'}

# del mydic["year"]
# print(mydic) #{'brand': 'Hyudai', 'model': 'i10'}

# del mydic
# print(mydic) #NameError: name 'mydic' is not defined

# mydic.clear()
# print(mydic)   # {}

# Example9: copying dictionary
# mydic1 = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year": 2020
# }

# using copy()
# mydic2 = mydic1.copy()
# print(mydic2)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2020}

# without using copy()
# mydic2=mydic1
# print(mydic2) #{'brand': 'Hyundai', 'model': 'i10', 'year': 2020}


# Nested loops

# exam o1
# create a nested dictionary with 3
# fields of 3 students
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }

# iterate all the nested dictionaries with
# both keys and values

# for i in data:
#     # display
#     print(data[i])

# exam 02
# create a nested dictionary with 3 fields of 3 students
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
#
# # iterate all the nested dictionaries with keys
# for i in data:
#     # display
#     print(data[i].keys())

# exam 03
# create a nested dictionary with 3 fields of 3 students
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
#
# # iterate all the nested dictionaries with values
# for i in data:
#     # display
#     print(data[i].values())
#
# while loops in dictionaries
# exam 01
# coffee_list = {"Peter": 0,
#                "Eva": 0,
#                "Franka": 0}
#
# while True:
#     name = input("Name: ")
#     if name == "":
#         break
#     coffee_list[name] += 1
#     print(coffee_list[name])
#
# print("coffee list: ", coffee_list)

# exam 02
# coffee_list = {"Peter": 0,
#                "Eva": 0,
#                "Franka": 0}
# tea_list = {"Peter": 0,
#             "Eva": 0,
#             "Franka": 0}

# while True:
#     name = input("Name: ")
#     if name == "":
#         break
#     getrank = input("Beverage (coffee/tea): ")
#     if getrank.lower() == "coffee":
#         coffee_list[name] += 1
#         print(coffee_list[name])
#     elif getrank.lower() == "tea":
#         tea_list[name] += 1
#         print(tea_list[name])
#
# print("coffee list: ", coffee_list)
# print("tea list: ", tea_list)

# exam 03
# list_of_beverages = {"Peter": {"tea": 0,
#                            "coffee": 0},
#                  "Eva": {"tea": 0,
#                          "coffee": 0},
#                  "Franka": {"tea": 0,
#                             "coffee": 0}}
#
# while True:
#     name = input("Name: ").capitalize()
#     if name == "":
#         break
#     if name not in list_of_beverages:
#         antwort = input("Shall we include " + name + " in the list? (y/n)")
#         if antwort.lower() in ["y", "yes"]:
#             list_of_beverages[name] = {"tea": 0, "coffee": 0}
#         else:
#             print(name + " cannot have a drink!")
#             continue
#     drink = input("Beverage (coffee/tea): ")
#     list_of_beverages[name][drink] += 1
# print(list_of_beverages)

# exam 04
# supermarket = {"milk": {"quantity": 20, "price": 1.19},
#                "biscuits":  {"quantity": 32, "price": 1.45},
#                "butter":  {"quantity": 20, "price": 2.29},
#                "cheese":  {"quantity": 15, "price": 1.90},
#                "bread":  {"quantity": 15, "price": 2.59},
#                "cookies":  {"quantity": 20, "price": 4.99},
#                "yogurt": {"quantity": 18, "price": 3.65},
#                "apples":  {"quantity": 35, "price": 3.15},
#                "oranges":  {"quantity": 40, "price": 0.99},
#                "bananas": {"quantity": 23, "price": 1.29}}
# total_value = 0
# for article, numbers in supermarket.items():
#     quantity = numbers["quantity"]
#     price = numbers["price"]
#     product_price = quantity * price
#     article = article + ':'
#     print(f"{article:15s} {product_price:08.2f}")
#     total_value += product_price
# print("="*24)
# print(f"Total sum:      {total_value:08.2f}")