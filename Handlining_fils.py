# """
# ============================
#         Python File Handling
# ============================

# Table of Contents:
# ------------------
# 1. Introduction to File Handling
# 2. Basic Operations:
#     a. Opening Files
#     b. Reading Files
#     c. Writing Files
#     d. Closing Files
# 3. File Modes:
#     a. Read Mode ('r')
#     b. Write Mode ('w')
#     c. Append Mode ('a')
#     d. Read and Write Mode ('r+')
#     e. Binary and Text Modes ('b', 't')
# 4. Working with File Paths
# 5. Handling Exceptions in File Operations
# 6. Advanced File Handling:
#     a. Working with File Pointers
#     b. Using 'with' Statement for File Handling


# ============================

# 1. Introduction to File Handling
# ----------------------------
# Why file handling is important in Python:
# When the program is terminated, the memory is freed, any data stored in variables during the program’s execution is erased. This data is not stored permanently unless you explicitly save it to a file, database, or another non-volatile storage medium.
# Data Storage: Files are essential for storing data persistently. Whether it's configuration settings, logs, or user data, files help maintain information even when the program isn't running.
# Data Processing: Many applications need to read and process data from files, such as reading a CSV (Comma-separated values file - like spreadsheets) file to analyze data.
# Automation: Automated tasks often involve generating or manipulating files, like creating reports or scraping data.
# File handling is an essential concept in Python that allows you to store, retrieve, and manipulate data stored in files. 
# A file is a collection of data stored on a disk with a specific name and a directory path.
# Python provides various functions and methods to perform operations on files, such as opening, reading, writing, and closing them.

# 2. Basic Operations:
# ----------------------
# Let's start with the basic operations you can perform on files.

# ### a. Opening Files

# To open a file in Python, you can use the `open()` function. The `open()` function takes two arguments: the file name and the mode in which you want to open the file.

# ```python
# file = open('example.txt', 'r')
# ```

# Here, the file `example.txt` is opened in read mode (`'r'`). We'll discuss different modes later in this lesson.

# ### b. Reading Files

# Once a file is opened, you can read its content using methods like `read()`, `readline()`, or `readlines()`.

# ```python
# content = file.read()  # Reads the entire file
# print(content)
# ```

# ### c. Writing Files

# To write data to a file, open it in write mode (`'w'`) or append mode (`'a'`). Use the `write()` method to add content to the file.

# ```python
# file = open('example.txt', 'w')
# file.write('Welcome in Python!')
# file.close()
# ```

# ### d. Closing Files

# After performing operations, it's crucial to close the file using the `close()` method to free up system resources.

# ```python
# file.close()
# ```

# 3. File Modes:
# ----------------
# File modes determine how the file is to be handled once opened. Below are the most common modes:

# ### a. Read Mode ('r')

# Opens a file for reading (default mode). The file pointer is placed at the beginning of the file.

# ```python
# file = open('example.txt', 'r')
# ```

# ### b. Write Mode ('w')

# Opens a file for writing. If the file exists, its content is erased. If the file does not exist, a new file is created.

# ```python
# file = open('example.txt', 'w')
# ```

# ### c. Append Mode ('a')

# Opens a file for appending. The file pointer is at the end of the file if it exists. If the file does not exist, a new file is created.

# ```python
# file = open('example.txt', 'a')
# ```

# ### d. Read and Write Mode ('r+')

# Opens a file for both reading and writing. The file pointer is placed at the beginning of the file.

# ```python
# file = open('example.txt', 'r+')
# ```

# ### e. Binary and Text Modes ('b', 't')

# Text mode is the default mode in Python, which handles files as text files. Binary mode (`'b'`) is used for handling binary files like images or executable files.

# ```python
# file = open('example.jpg', 'rb')  # Binary read
# file = open('example.txt', 'wt')  # Text write (default)
# ```

# 4. Working with File Paths:
# -----------------------------
# Files are often stored in directories (folders), and Python provides ways to handle file paths effectively.

# ### Absolute vs. Relative Paths

# - **Absolute Path**: The complete path from the root directory.
# - **Relative Path**: The path relative to the current working directory.
# # file_path = 'C:\Users\DELL\Desktop\oop.txt'       # error
# # file_path = r'C:\Users\DELL\Desktop\oop.txt'      solution1: raw string
# # file_path = 'C:\\Users\\DELL\\Desktop\\oop.txt'   solution2: double backslash
# file = open('C:/Users/DELL/Desktop/oop.txt', 'r')   solution3: make it a forwardslash

# ```python
# file = open('/Users/username/Documents/example.txt', 'r')  # Absolute Path
# file = open('example.txt', 'r')  # Relative Path
# ```

# ### Using `os` Module

# The `os` module allows you to work with file paths in a cross-platform way.

# ```python
# import os

# # Get the current working directory
# cwd = os.getcwd()
# print(cwd)

# # Joining paths
# path = os.path.join(cwd, 'example.txt')
# print(path)
# ```

# 5. Handling Exceptions in File Operations:
# -------------------------------------------
# When working with files, errors can occur. For example, trying to open a non-existent file in read mode will raise an `IOError`. To handle such cases, use `try-except` blocks.


# 6. Advanced File Handling:
# ----------------------------
# ### a. Working with File Pointers

# The file pointer keeps track of where you are in the file. You can use `seek()` and `tell()` methods to manipulate the pointer.

# ```python
# file = open('example.txt', 'r')
# file.seek(10)  # Move to the 10th byte
# position = file.tell()  # Get the current position
# print(f"Current position: {position}")
# ```


# # whence = 0 >> start from byte 0
# # with open('example.txt', 'w') as file:
# #     file.seek(10)
# #     file.write("4")
# #     curr_seek = file.tell()
# #     file.seek(curr_seek + 10)
# #     file.write("4")

# ### b. Using 'with' Statement for File Handling

# The `with` statement is used for resource management. It ensures that the file is properly closed after its suite finishes, even if an exception is raised.

# ```python
# with open('example.txt', 'r') as file:
#     content = file.read()
#     print(content)
# ```
import os
# to know main current working directory
print(os.getcwd()) 

# directory For the opened File
Abspath = os.path.abspath(__file__) # the file that i am in
print(Abspath)
print(os.path.dirname(Abspath))   # the folder that the file in   

# change current working directory
os.chdir(os.path.dirname(Abspath))
print(os.getcwd())


# read files =======================================
myfile = open (r"D:\SHOUSH\shehab.txt","r")
print(myfile)            # data object 
print(myfile.name)       # name object 
print(myfile.mode)       # mode object 
print(myfile.encoding)   # encoding object 

# print(myfile.read())
# print(myfile.readline(5)) 
# print(myfile.readline()) 
# print(myfile.readline()) 
# print(myfile.readlines())
# app 

for line in myfile: 
    if line.startswith("3"):
        break 
    print(line)
myfile.close()

# write file  
myFile = open (r"D:\SHOUSH\Ahamed.txt" , "w" )
myFile.write("How are you\n")
myFile.write("Ahmed\n")
myFile.write("welcome Man\n")

#  ============  App ===================================================
mylist = ['Shehab' , 'Elzero' , 'Sara','Basaent' , 'Elraq' , 'Saltah']
for i in range( 0 , len ( mylist ) ):
    myFile.write(f"What's up {mylist[i]}\n")
myFile.close()

# append to a file
myFile = open (r"D:\SHOUSH\Ahamed.txt" , "a" )
myFile.write("How are you\n")
myFile.write("Ahmed\n")
myFile.write("welcome Man\n")
myFile.close()

# truncate function
MyFile = r"D:\SHOUSH\khalied.txt" 
open(MyFile,"w").write("I love shehab\n")
appendtofile=open(MyFile,"a")
appendtofile.truncate(10)

# tell function
print(appendtofile.tell())

# seek function
appendtofile=open(MyFile,"r")
appendtofile.seek(5)
print(appendtofile.read())
appendtofile.close()

# Remove file
os.remove(MyFile)