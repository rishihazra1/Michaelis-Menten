import matplotlib.pyplot as plt
import file_interpretation


def plot_single_file(file):
    first_column, second_column = file_interpretation.read_file(file)
    all_y_values = file_interpretation.initialize_array(first_column, second_column)
    x_values = []
    y_values = []
    yes_or_no = input("Would you like to select a specific range to plot?\n")
    if str.lower(yes_or_no) == "no":
        start = 0
        end = len(all_y_values) - 1
    else:
        start = int(input("Enter your desired start time for the plot.\n"))
        end = int(input("Enter your desired end time for the plot.\n"))
    index = start
    while index <= end:
        try:
            y_values.append(all_y_values[index])
            index += 1
        except IndexError:
            print(
                "Index Error. Data point(s) are missing in given file. Plot will be truncated to the length of your "
                "data set. ")
            break
    for time in range(start, index):
        x_values.append(time)
    print(x_values)
    print(y_values)
    plt.scatter(x_values, y_values)
    plt.show()

# note that erorrs can be made due to incorrect data files (data from certain seconds missing from file).
