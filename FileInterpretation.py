import csv
import fileinput
import tkinter.filedialog


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


# def findSlope(end, start):


# def convertToVelocity(slope):
