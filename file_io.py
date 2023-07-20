#!python
"""The intention of this file is to show some examples of how fileio works in python"""
print("Lets read from a test file")
with open("resources/read.txt", mode="r", encoding="utf-8") as file_handle:
    j = file_handle.read()
    print("Using x.read() provides the entire file in a string")
    print("\t", type(j), j)


with open("resources/read.txt", mode="r", encoding="utf-8") as file_handle:
    j = file_handle.readlines()
    print("Using x.readlines() provides a list of strings," +
          " where each element in the list is a line from the file.")
    print("\t", type(j), j)

with open("resources/write.txt", mode="w", encoding="utf-8") as file_handle:
    print("Write a line to the file")
    file_handle.write("line 1")

with open("resources/read.txt", mode="r", encoding="utf-8") as file_handle:
    print("This is the file we just wrote")
    print(file_handle.readlines())

with open("resources/write.txt", mode="w", encoding="utf-8") as file_handle:
    print("Lets add another line")
    file_handle.write("line 2")

with open("resources/read.txt", mode="r", encoding="utf-8") as file_handle:
    print("Oh, we overwrote our previous line")
    print(file_handle.readlines())

with open("resources/write.txt", mode="a", encoding="utf-8") as file_handle:
    print("Adding another line after opening the file as append")
    file_handle.write("line 3")

with open("resources/read.txt", mode="r", encoding="utf-8") as file_handle:
    print(file_handle.readlines())

with open("resources/write.txt", mode="a", encoding="utf-8") as file_handle:
    print("We can use write lines to add multiple lines")
    file_handle.writelines(["line 4", "line 5"])

with open("resources/read.txt", mode="r", encoding="utf-8") as file_handle:
    print(file_handle.readlines())
