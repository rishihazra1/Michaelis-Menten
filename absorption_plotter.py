import matplotlib.pyplot as plt
import file_interpretation

start_time = int()
end_time = int()


def plot_single_file(file, start, end):
    first_column, second_column = file_interpretation.read_file(file)
    all_y_values = file_interpretation.initialize_array(first_column, second_column)
    x_values = []
    y_values = []
    index = start
    while index <= end:
        try:
            y_values.append(all_y_values[index])
            index += 1
        except IndexError:
            print(
                "Index Error. Data point(s) are missing in given file. Plot will be truncated to the length of your data set. ")
            break
    for time in range(start, index):
        x_values.append(time)
    print(x_values)
    print(y_values)
    plt.scatter(x_values, y_values)
    plt.show()

# note that erorrs can be made due to incorrect data files (data from certain seconds missing from file).
