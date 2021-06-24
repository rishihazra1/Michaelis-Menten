import graph_functions
import file_interpreter

print("Select the file you wish to plot.")
path = file_interpreter.request_file()
graph_functions.plot_single_file(path)

