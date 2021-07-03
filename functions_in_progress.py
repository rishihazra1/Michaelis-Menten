import numpy as np
import matplotlib.pyplot

def find_line_of_best_fit(x_numpy, y_numpy):
    slope, intercept = np.polyfit(x_numpy, y_numpy, 1)
    print(slope, intercept)
    return slope, intercept
