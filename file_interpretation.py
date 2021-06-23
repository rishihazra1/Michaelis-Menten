import csv

data_points = []
absorption_values = []
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


def initialize_array(time_column, absorption_column):
    for index in range(0, len(time_column)):
        if time_column[index] == "HH:MM:SS":
            zero_index = index + 1    # identifying desired data start location
        if time_column[index] == "ID#":
            end_index = index - 2
            break
    for time in range(zero_index, end_index + 1):
        data_points.append(absorption_column[time])
    print(data_points)
    print(len(data_points))
    return data_points


def get_absorption(data_array, time_stamp):
    index_valid = False
    input_time = time_stamp
    while index_valid is False:
        try:
            instantaneous_absorption = data_array[time_stamp]
            index_valid = True
        except IndexError:
            print("Index Error. Data point(s) are missing in given file. Final time will be truncated by 1 second. "
                  "Please verify trial actually ran for " + str(input_time) + " seconds." )
            index_valid = False
            time_stamp -= 1

#    print("(time (sec), absorption): " + "(" + str(time_stamp) + "," + str(instantaneous_absorption) + ")")
    return instantaneous_absorption


def find_velocity(start_value, start_time, end_value, end_time, enzyme_concentration, molar_extinction):
    slope = (float(end_value) - float(start_value)) / (int(end_time) - int(start_time))
    velocity = (slope * 60) / (float(enzyme_concentration) * float(molar_extinction))
    return velocity
