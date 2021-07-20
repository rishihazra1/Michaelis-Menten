import numpy as np
import scipy
from matplotlib import pyplot as plt

def find_line_of_best_fit(x_numpy, y_numpy):
    slope, intercept = np.polyfit(x_numpy, y_numpy, 1)
    print(slope, intercept)
    return slope, intercept

# below is in progress function for michaelis-menten curve fit
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