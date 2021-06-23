import csv
import math
import fileinput
import tkinter.filedialog

startTime = int()
endTime = int()
startValue = float()
endValue = float()
molarExtinction = float()


def get_absorption(csv_file, time_stamp):
    with open(csv_file) as current_file:
        csv_reader = csv.reader(current_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 26 + time_stamp:
                instantaneous_absorption = row[1]
                print("(time (sec), absorption): " + "(" + str(time_stamp) + "," + str(instantaneous_absorption) + ")")
                break
            line_count += 1
        line_count = 0
    return float(instantaneous_absorption)


def find_velocity(start_value, start_time, end_value, end_time, enzyme_concentration, molar_extinction):
    slope = (end_value - start_value) / (end_time - start_time + 1)
    velocity = (slope * 60) / (enzyme_concentration * molar_extinction)
    return float(velocity)
