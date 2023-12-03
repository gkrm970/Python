# Example1: writing data in to text file
# file=open("C:\Demofiles\myfile.txt",'w')
#
# file.write("This is my first statement...\n")
# file.write("This is my second statement...\n")
# file.write("This is my third statement...\n")
# file.write("This is my fourth statement...\n")
# file.write("This is my fith statement...")
# file.close()
# print("program completed....")

# Example2: reading data from text file

# file=open("C:\Demofiles\myfile.txt",'r')
# #print(file.read())
# print(file.readline())
# file.close()

# Example3: appending data into text file
# file=open("C:\Demofiles\myfile.txt",'a')
#
# file.write("\n this is my sixth line\n")
# file.write(" this is my seventh line\n")
# file.close()
# print("program is completed....")

# Example4: reading data from text file using with block
# with open("C:\Demofiles\myfile.txt",'r') as file:
#     print(file.read())
#     print(file.readline())
# print("program completed....")

# Example5: writing data into text file using with block

# with open("C:\Demofiles\myfile.txt", 'w') as file:
#     file.write("This is my first statement...\n")
#     file.write("This is my second statement...\n")
#     file.write("This is my third statement...\n")
#     file.write("This is my fourth statement...\n")
#     file.write("This is my fith statement...")
    # file.close() is not required when we use with block

print("program completed....")

# Example6: appending data into text file using with block
# with open("C:\Demofiles\myfile.txt",'a') as file:
#     file.write("\n this is my sixth line\n")
#     file.write(" this is my seventh line\n")
# print("program is completed....")

# Example7: reading data from text file using for loop
# with open("C:\Demofiles\myfile.txt",'r') as file:
#     for line in file:
#         print(line)
# print("program completed....")

# Example8: writing data into text file using for loop
# with open("C:\Demofiles\myfile.txt", 'w') as file:
#     for i in range(1, 10):
#         file.write("This is my first statement...\n")
# print("program completed....")

# Example9: appending data into text file using for loop
# with open("C:\Demofiles\myfile.txt",'a') as file:
#     for i in range(1, 10):
#         file.write(" \n This is my first statement...\n")
# print("program completed....")

# Example10: reading data from text file using readline()
# with open("C:\Demofiles\myfile.txt",'r') as file:
#     print(file.readline())
# print("program completed....")

# Example11: writing data into text file using readline()
# with open("C:\Demofiles\myfile.txt", 'w') as file:
#     file.write("This is my first statement...\n")
#     file.write("This is my second statement...\n")
#     file.write("This is my third statement...\n")
#     file.write("This is my fourth statement...\n")
#     file.write("This is my fith statement...")
# print("program completed....")


