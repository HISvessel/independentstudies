#!/usr/bin/python3

import os
import shutil

folder_path = input("Enter the folder path to organize:")

if not os.path.exists(folder_path):
    """this handles the edge case for when a relative path
    is not found"""

    print("Relative path does not exists")
    exit()

for filename in os.listdir(folder_path):
    """we begin to iterate through the list of folders by comparing the input given
    to the listed folder as provided by the listdir builtin"""
    file_path = os.path.join(folder_path, filename)

    if os.path.isdir(file_path):
        continue

    file_ext = filename.split('.')[-1]
    ext_folder = os.path.join(folder_path, file_ext)

    if not os.path.exists(ext_folder): #this makes the folder extension if it doesnt exists
        os.makedirs(ext_folder)

    #this will move the file to the given folder
    shutil.move(file_path, os.path.join(ext_folder, filename))

print("File successfully organized")
