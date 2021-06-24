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
    for time in range(start, index):
        x_values.append(time)
    plot_with_linear_fit(x_values, y_values)


# note that errors can occur due to incorrect data files (data from certain seconds missing from file).

def plot_with_linear_fit(x_array, y_array):
    x, y = convert_to_np_array(x_array, y_array)
    m, b = np.poly.fit(x, y, 1)
    plt.scatter(x_array, y_array, s=10)
    plt.plot(x, m * x + b)
    plt.show()
    print("Plot opened in alternate window.")


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
