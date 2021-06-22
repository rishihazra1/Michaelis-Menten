import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

print("Enter molar extinction coefficient.")
molarExtinction = float(input())

print("Please select the folder containing your UV-Visible Light Spectroscopy Data")
path = askdirectory(title='Select Folder')  # shows dialog box and return the path
print(path)

os.chdir(path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())


# iterate through all file
for file in os.listdir():

