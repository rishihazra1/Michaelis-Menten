import matplotlib.pyplot as plt
import file_interpretation

start_time = int()
end_time = int()

def produce_scatter_plot(start_time, end_time):


def plot_single_file(file, start, end, concentrations):
    x_values = concentrations
    y_values = []
    for temp_time in range(start, end + 1):
        y_values.append(file_interpretation.get_absorption(file, temp_time))
    plt.scatter(x_values, y_values)
    plt.show()

