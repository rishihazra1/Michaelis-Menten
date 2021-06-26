import matplotlib.pyplot as plt
import file_interpreter
import numpy as np
from scipy import stats
import other_functions


def plot_single_file(file):
    first_column, second_column = file_interpreter.read_file(file)
    all_y_values = file_interpreter.initialize_array(first_column, second_column)
    x_values = []
    y_values = []
    start, end = other_functions.get_time_bounds(all_y_values)
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
    print("y-values: " + str(y_values))
    for time in range(start, index):
        x_values.append(time)
    print("x-values: " + str(x_values))
    x_numpy, y_numpy = other_functions.convert_to_numpy_float(x_values, y_values)
    plt.scatter(x_numpy, y_numpy, s=10)
    plt.plot()
    plot_best_fit_line(x_numpy, y_numpy)


def plot_from_arrays(x_array, y_array):
    print(x_array, y_array)
    x_numpy, y_numpy = other_functions.convert_to_numpy_float(x_array, y_array)
    plt.scatter(x_numpy, y_numpy, s=10)
    plot_best_fit_line(x_numpy, y_numpy)


# note that errors can occur due to incorrect data files (data from certain seconds missing from file).

def plot_best_fit_line(x_numpy, y_numpy):
    result = stats.linregress(x_numpy, y_numpy)
    r_squared = float(result.rvalue) ** 2
    print(f"r_squared: {r_squared}")
    print(str(result.slope) + ", " + str(result.intercept))
    plt.plot(x_numpy, result.intercept + result.slope * x_numpy)
    plt.show()
    print("Plot opened in alternate window.")
    return result, r_squared
