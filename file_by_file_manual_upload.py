import fileinput
import tkinter.filedialog
import file_interpretation

startTime = 0
endTime = 20

print("Enter molar extinction coefficient of your substrate.")
molarExtinction = float(input())

print("Enter concentration of your enzyme (in µM).")
enzymeConcentration = float(input())

print("How many concentrations did you run trials for?")
concentrationsRun = int(input())
print("Enter the concentrations (in µM) at which you ran trials.")
trialConcentrations = []
t = 0
while t < concentrationsRun:
    trialConcentrations.append(input())
    t += 1

print(trialConcentrations)

numberOfTrials = []
n = 0
while n < len(trialConcentrations):
    numberOfTrials.append(int(input("How many trials did you run at the " + trialConcentrations[n] + " µM\n")))
    n += 1

print(numberOfTrials)

for i in range(0, len(trialConcentrations) - 1):
    m = 1
    while m < numberOfTrials[i] + 1:
        print("Select file with data for Trial " + str(m) + " at " + trialConcentrations[i] + " µM.\n")
        path = tkinter.filedialog.askopenfilename()
        print(path)
        startValue = file_interpretation.get_absorption(path, startTime)
        endValue = file_interpretation.get_absorption(path, endTime)
        file_interpretation.find_velocity(startValue, startTime, endValue, endTime, enzymeConcentration, molarExtinction)
        m += 1
