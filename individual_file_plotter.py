import absorption_plotter
import file_interpretation

print("Select the file you wish to plot.")
path = file_interpretation.request_file()
start_time = int(input("Enter the start time for the plot.\n"))
end_time = int(input("Enter the end time for the plot.\n"))
absorption_plotter.plot_single_file(path, start_time, end_time)

