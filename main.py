import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

print("Enter molar extinction coefficient.")
molarExtinction = float(input())

print("How many concentrations did you run trials for?")
trialsRun = int(input())
print("Enter the concentrations (in µM) at which you ran trials.")
trialConcentrations = []
t = 0
while t < trialsRun:
    trialConcentrations.append(input())
    t += 1

print(trialConcentrations)

print("Please select the folder containing your UV-Visible Light Spectroscopy Data")
path = askdirectory(title='Select Folder')  # shows dialog box and return the path
print(path)

