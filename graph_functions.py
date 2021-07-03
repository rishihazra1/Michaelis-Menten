import matplotlib.pyplot as plt
import numpy as np
import file_interpreter
from scipy import stats
import scipy.optimize
import other_functions


def plot_single_file(file):
    first_column, second_column = file_interpreter.read_file(file)
    all_x_values, all_y_values = file_interpreter.initialize_array(first_column, second_column)
    desired_x_values = []
    desired_y_values = []
    start, end = other_functions.get_time_bounds(all_y_values)
    index = start
    while index <= end:
        try:
            desired_y_values.append(float(all_y_values[index]))
            index += 1
        except IndexError:
            print(
                "Index Error. Data point(s) are missing in given file. Plot will be truncated to the length of your "
                "data set. ")
            break
    print("y-values: " + str(desired_y_values))
    for time in range(start, index):
        desired_x_values.append(time)
    print("x-values: " + str(desired_x_values))
    x_numpy, y_numpy = other_functions.convert_to_numpy_float(desired_x_values, desired_y_values)
    plt.scatter(x_numpy, y_numpy, s=10)
    plt.plot()
    plot_best_fit_line(x_numpy, y_numpy)


def plot_from_arrays(x_array, y_array):
    print(x_array, y_array)
    x_numpy, y_numpy = other_functions.convert_to_numpy_float(x_array, y_array)
    plt.scatter(x_numpy, y_numpy, s=10)
    plot_best_fit_line(x_numpy, y_numpy)


# note that errors can occur due to incorrect data files (data from certain seconds missing from file).

"""
def rational(x, p, q):
    return np.polyval(p, x) / np.polyval(q + [1.0], x)



def plot_rational_function_fit(x_numpy, y_numpy):
    plt.plot(x_numpy, y_numpy, 'b-', label='data')
    rng = np.random.default_rng()
    y_noise = 0.2 * rng.normal(size=x_numpy.size)
    y_predicted = rational(x_numpy, 2.5, 1.3) + y_noise
    popt, pcov = scipy.optimize.curve_fit(rational, x_numpy, y_predicted)
    plt.plot(x_numpy, rational(x_numpy, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    popt, pcov = scipy.optimize.curve_fit(rational, x_numpy, y_predicted, bounds=(0, [3., 1., 0.5]))
    plt.plot(x_numpy, rational(x_numpy, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
    plt.show()
    print("In Progress")
"""


def plot_best_fit_line(x_numpy, y_numpy):
    result = stats.linregress(x_numpy, y_numpy)
    r_squared = float(result.rvalue) ** 2
    print(f"r_squared: {r_squared}")
    print(str(result.slope) + ", " + str(result.intercept))
    plt.plot(x_numpy, result.intercept + result.slope * x_numpy)
    plt.show()
    print("Plot opened in alternate window.")
    return result, r_squared


def get_r_squared(x_numpy, y_numpy):
    result = stats.linregress(x_numpy, y_numpy)
    r_squared = float(result.rvalue) ** 2
    return r_squared


def find_best_bounds(x_values, y_values):
    max_r_squared = 0
    max_bounds = [0, len(x_values) - 1, "ERROR: reverted to full plot"]
    for start_index in range(0, len(x_values) - 15):
        for end_index in range(start_index + 15, len(x_values)):
            new_x_values = []
            new_y_values = []
            i = start_index
            while i < end_index + 1:
                new_x_values.append(x_values[i])
                new_y_values.append(y_values[i])
                i += 1
            print("new_x_values: " + str(new_x_values))
            print("new_y_values: " + str(new_y_values))
            new_x_numpy, new_y_numpy = other_functions.convert_to_numpy_float(new_x_values, new_y_values)
            r_squared = get_r_squared(new_x_numpy, new_y_numpy)
            print(start_index, end_index, r_squared)
            if r_squared == 1 or r_squared == 0:
                print("Calculated r-value incorrect.")
            elif max_r_squared < r_squared:
                max_bounds = [start_index, end_index, r_squared]
                max_r_squared = r_squared
                print("New max at: " + str(max_bounds))
    print(max_bounds)
    return max_bounds[0], max_bounds[1]
