import csv

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
            if len(rows[index]) == 1:
                first_column.append(rows[index][0])
                second_column.append("NULL")
            if len(rows[index]) >= 2:
                first_column.append(rows[index][0])
                second_column.append(rows[index][1])
            index += 1
    return first_column, second_column


def get_x_values(csv_file):
    time_stamps, absorption_values = read_file(csv_file)
    for index in range(0, len(time_stamps)):
        if time_stamps[index] == "HH:MM:SS":
            zero_index = index + 1    # identifying desired data start location
        if time_stamps[index] == "ID#":
            end_index = index - 2
            break
    for time in range(zero_index, end_index + 1):
        x_values.append(absorption_values[time])
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
    slope = (float(end_value) - float(start_value)) / (int(end_time) - int(start_time))
    velocity = (slope * 60) / (float(enzyme_concentration) * float(molar_extinction))
    return velocity
