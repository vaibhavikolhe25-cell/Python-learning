# write a python program to print the contest of directory using the os module .
#  search online for the function which does that.
import os

# Select the directory whose content you want to list 
directory_path = r"C:\Users\vaibhavi\Downloads\chapter 1"

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)