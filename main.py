import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

print("Enter molar extinction coefficient of your substrate.")
molarExtinction = float(input())

print("How many concentrations did you run trials for?")
concentrationsRun = int(input())
print("Enter the concentrations (in µM) at which you ran trials.")
trialConcentrations = []
t = 0
while t < concentrationsRun:
    trialConcentrations.append(input())
    t += 1

print(trialConcentrations)
n = 0
while n < concentrationsRun:
    truncationTimes = []
    print("Enter your desired start time and end time in seconds (pressing enter between each time) for your " + trialConcentrations[n] + " µM trials.")
    while len(truncationTimes) < 2:
        truncationTimes.append(input())
    print("Select the folder containing your data at " + trialConcentrations[n] + " µM")
    path = askdirectory(title='Select Folder')  # shows dialog box and return the path
    print(path)
    n += 1

