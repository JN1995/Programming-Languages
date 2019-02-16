## File Handling Basics

# 1) Read file from a default folder
# 2) Store file data into a variable
# 3) Find the current directory
# 4) Read a file from anywhere in th computer
# 5) Close the file

# 1) Read file from a default folder
my_file = open("The avengers.txt")
my_file.read()
my_file.read()
my_file.seek(0)
my_file.read()
my_file.seek(0)

my_file.readlines()
my_file.seek(0)

# 2) Store file data into a variable
new_file = my_file.read()
new_file

# 3) Find the current directory
# pwd
import os
pwd = os.getcwd()
pwd

# 4) Read a file from anywhere in th computer
my_file = open("/media/duanle/Data/Bach Khoa HCM/MA_CSE/HK182/pre_all/programming/Programming-Languages/python for Beginner/README.md")
print(my_file.read())
my_file.seek(0)
my_file.readlines()
# Close the file
my_file.close()

# read file with encoding utf-8
import io
my_file = io.open(
    "/media/duanle/Data/Bach Khoa HCM/MA_CSE/HK182/pre_all/programming/Programming-Languages/python for Beginner/README.md", 
    encoding="utf-8")
print(my_file.read())
my_file.close()


with io.open(
    "/media/duanle/Data/Bach Khoa HCM/MA_CSE/HK182/pre_all/programming/Programming-Languages/python for Beginner/README.md", 
    mode='r',
    encoding="utf-8") as f:
    print(f.read())
