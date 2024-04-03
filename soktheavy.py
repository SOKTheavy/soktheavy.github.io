# def add_xy(x, y):
#     return x+y;
#
#
# def minus_xy(x, y):
#     return x-y;
#
#
# def multiply_xy(x, y):
#     return x*y;
#
#
# def divide_xy(x, y):
#     return x/y;
#
#
# x = int(input("Enter X: "))
# y = int(input("Enter Y: "))
# opt = str(input("Enter Operation + - * /"))
#
# if opt == "+":
#     res = add_xy(x,y)
#     print("The Result", res)
# elif opt == "-":
#     res = minus_xy(x,y)
#     print("The Result", res)
# elif opt == "*":
#     res = multiply_xy(x,y)
#     print("The Result", res)
# elif opt == "/":
#     res = divide_xy(x,y)
#     print("The Result", res)
# else:
#     print(" Worng Operation")

# f declearation for variable for open file name
# f = open("test.txt", "r")
#
# print(f.read())
# end for open file
# for open file and then add new data to the file
# f = open("test.txt", "a")
# f.write("\nThis is my new line update from Python file.\n")
# f.close()
# f = open("test.txt", "r")
# print(f.read())
# f.close()
# end for append new data
# update new data in to file in the folder
# f = open("test.txt", "w")
# f.write("Welcome for the new paragraph in this file has update.\nBy the new paragraph from python file.\nIt not Easy for me.\n Hello KOUN PAPA.")
# f = open("test.txt", "r")
# print(f.read())
# f.close()
#end for write data into file
# Create new File by use python syntax
# f = open("myfile.txt", "x")
# End Create new File by use python syntax
# DElect new File by use python syntax
import os
os.remove("myfile.txt")
# End Delect new File by use python syntax
