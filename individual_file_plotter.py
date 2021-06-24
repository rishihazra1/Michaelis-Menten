import absorption_plotter
import file_interpretation

print("Select the file you wish to plot.")
path = file_interpretation.request_file()
absorption_plotter.plot_single_file(path)

