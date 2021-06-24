from array import array

import matplotlib.pyplot as plt
import numpy
import file_interpretation
import numpy as np
from scipy import stats


def plot_single_file(file):
    first_column, second_column = file_interpretation.read_file(file)
    all_y_values = file_interpretation.initialize_array(first_column, second_column)
    x_values = []
    y_values = []
    input_valid = False
    while input_valid is False:
        yes_or_no = input("Would you like to select a specific range to plot? Enter yes or no.\n")
        if str.lower(yes_or_no) == "no":
            start = 0
            end = len(all_y_values) - 1
            input_valid = True
        elif str.lower(yes_or_no) == "yes":
            start = int(input("Enter your desired start time for the plot.\n"))
            end = int(input("Enter your desired end time for the plot.\n"))
            input_valid = True
        else:
            print("Input not recognized. Enter yes or no.")
            input_valid = False
    index = start
    while index <= end:
        try:
            y_values.append(float(all_y_values[index]))
            index += 1
        except IndexError:
            print(
                "Index Error. Data point(s) are missing in given file. Plot will be truncated to the length of your "
                "data set. ")
            break
    for time in range(start, index):
        x_values.append(time)
    plot_with_linear_fit(x_values, y_values)


# note that errors can occur due to incorrect data files (data from certain seconds missing from file).


def plot_with_linear_fit(x_array, y_array):
    x, y = convert_to_np_array(x_array, y_array)
    m, b = np.polyfit(x, y, 1)
    plt.scatter(x_array, y_array, s=10)
    plt.plot(x, m * x + b)
    plt.show()


def get_r_squared(x_array, y_array):
    x, y = convert_to_np_array(x_array, y_array)
    res = stats.linregress(x, y)
    r_squared = float(res.rvalue) ** 2
    print(f"r_squared: {r_squared}")
    return r_squared


def convert_to_np_array(x_array, y_array):
    x = np.array(x_array)
    y = np.array(y_array)
    return x, y