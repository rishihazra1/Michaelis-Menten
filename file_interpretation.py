import csv
import numpy
import math
import fileinput
import tkinter.filedialog

startTime = int()
endTime = int()
startValue = float()
endValue = float()
molarExtinction = float()
x_values = []
rows = []


def read_file(csv_file):
    with open(csv_file) as current_file:
        csv_reader = csv.reader(current_file, delimiter=',')
        for row in csv_reader:
            rows.append(row)
    print(rows)
    print(row[1])
    return rows


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


def get_x_values(csv_file):
    with open(csv_file) as current_file:
        csv_reader = csv.reader(current_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if row[0] == "HH:MM:SS":
                zero_index = line_count + 1  # identifying data start location
                print("zero-index: " + str(zero_index))
            if row[0] == "ID#":
                end_index = line_count - 2
                print("end-index: " + str(end_index))
                break
            line_count += 1
    trial_duration = end_index - zero_index
    for time in range(0, trial_duration + 1):
        x_values.append(get_absorption(csv_file, time))
    print(x_values)
    return x_values


def find_velocity(start_value, start_time, end_value, end_time, enzyme_concentration, molar_extinction):
    slope = (end_value - start_value) / (end_time - start_time + 1)
    velocity = (slope * 60) / (enzyme_concentration * molar_extinction)
    return float(velocity)
