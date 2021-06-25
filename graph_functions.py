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
    x_numpy, y_numpy = convert_to_numpy_array(x_values, y_values)
    plt.scatter(x_numpy, y_numpy, s=10)
    slope, intercept, r_squared = find_linear_fit(x_values, y_values)
    plt.plot(x_values, slope * x_numpy + intercept)
    plt.show()


# note that errors can occur due to incorrect data files (data from certain seconds missing from file).

def find_linear_fit(x_array, y_array):
    slope, intercept, r, p, se = stats.linregress(x_array, y_array)
    r_squared = float(r) ** 2
    print(f"r_squared: {r_squared}")
    print(str(slope) + ", " + str(intercept))
    print("Plot opened in alternate window.")
    return slope, intercept, r_squared


def convert_to_numpy_array(x_array, y_array):
    x_numpy = np.array(x_array)
    y_numpy = np.array(y_array)
    return x_numpy, y_numpy