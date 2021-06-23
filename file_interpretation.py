import csv

startTime = int()
endTime = int()
startValue = float()
endValue = float()
molarExtinction = float()
x_values = []
rows = []
first_column = []
second_column = []


def read_file(csv_file):
    with open(csv_file) as current_file:
        csv_reader = csv.reader(current_file, delimiter=',')
        for row in csv_reader:
            rows.append(row)
        index = 0
        while index < len(rows):
            if len(rows[index]) == 0:
                first_column.append("NULL")
                second_column.append("NULL")
            else:
                first_column.append(rows[index][0])
            if len(rows[index]) >= 2:  # only concerned with first two columns, can use while loop to read remaining columns
                second_column.append(rows[index][1])
            else:
                second_column.append("NULL")
            index += 1
    print(first_column)
    print(second_column)
    return first_column, second_column


def get_x_values(csv_file):
    time_stamps, absorption_values = read_file(csv_file)
    print(time_stamps)
    print(absorption_values)
    for index in range(0, len(time_stamps)):
        if time_stamps[index] == "HH:MM:SS":
            zero_index = index + 1 # identifying data start location
            print("zero-index: " + str(zero_index))
        if time_stamps[index] == "ID#":
            end_index = index - 2
            print("end-index: " + str(end_index))
            break
    trial_duration = end_index - zero_index
    for time in range(zero_index, end_index + 1):
        x_values.append(absorption_values[index])
    print(x_values)
    return x_values


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
    return instantaneous_absorption


def find_velocity(start_value, start_time, end_value, end_time, enzyme_concentration, molar_extinction):
    slope = (end_value - start_value) / (end_time - start_time + 1)
    velocity = (slope * 60) / (enzyme_concentration * molar_extinction)
    return float(velocity)
