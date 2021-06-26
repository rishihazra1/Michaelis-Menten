import numpy as np


def get_time_bounds(data_set):
    input_valid = False
    while input_valid is False:
        yes_or_no = input("Would you like to select a specific range to plot? Enter yes or no.\n")
        if str.lower(yes_or_no) == "no":
            start = 0
            end = len(data_set) - 1
            input_valid = True
        elif str.lower(yes_or_no) == "yes":
            start = int(input("Enter your desired start time for the plot.\n"))
            end = int(input("Enter your desired end time for the plot.\n"))
            input_valid = True
        else:
            print("Input not recognized. Enter yes or no.")
            input_valid = False
    return start, end


def time_bound_input_checker():
    input_valid_individual = False
    input_valid_overall = False
    yes_or_no_overall = "no"
    while input_valid_individual is False:
        yes_or_no_individual = input("Do you have different desirable time bounds for each file?\n")
        if str.lower(yes_or_no_individual) == "yes" or str.lower(yes_or_no_individual) == "no":
            input_valid_individual = True
        else:
            print("Input not recognized. Please enter yes or no.")
            input_valid_individual = False
    if yes_or_no_individual == "no":
        while input_valid_overall is False:
            yes_or_no_overall = input("Do you have a default desirable time bound for all files?\n")
            if str.lower(yes_or_no_overall) == "yes" or str.lower(yes_or_no_overall) == "no":
                input_valid_overall = True
            else:
                print("Input not recognized. Please enter yes or no.")
                input_valid_overall = False
    return yes_or_no_individual, yes_or_no_overall


def convert_to_numpy_float(x_array, y_array):
    x_numpy = np.array(x_array).astype(np.float64)
    y_numpy = np.array(y_array).astype(np.float64)
    return x_numpy, y_numpy


def convert_to_numpy_array(x_array, y_array):
    x_numpy = np.array(x_array)
    y_numpy = np.array(y_array)
    return x_numpy, y_numpy


def get_predicted_y(x_numpy, slope, intercept):
    print(x_numpy)
    predicted_y = []
    for i in range(0, len(x_numpy)):
        predicted_y.append((x_numpy[i] * slope) + intercept)
    return predicted_y
