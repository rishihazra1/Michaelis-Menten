import csv
import math
import fileinput
import tkinter.filedialog

startTime = int()
endTime = int()
startValue = float()
endValue = float()
molarExtinction = float()


def getStart(csv_file, startTime):
    with open(csv_file) as current_file:
        csv_reader = csv.reader(current_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 26 + startTime:
                initialAbsorption = row[1]
                print(initialAbsorption)
                break
            line_count += 1
        line_count = 0
    return float(initialAbsorption)


def getEnd(csv_file, endTime):
    with open(csv_file) as current_file:
        csv_reader = csv.reader(current_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 26 + endTime:
                finalAbsorption = row[1]
                print(finalAbsorption)
                break
            line_count += 1
    return float(finalAbsorption)


def findVelocity(startValue, startTime, endValue, endTime, molarExtinction):
    slope = (endValue - startValue) / (endTime - startTime + 1)
    print(slope)
    velocity = (slope * 60) / (.002 * molarExtinction)
    print(velocity)
    return float(velocity)
