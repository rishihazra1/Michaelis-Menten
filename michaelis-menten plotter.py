import tkinter.filedialog
import matplotlib.pyplot as plt
import other_functions
import graph_functions
import file_interpreter

molar_extinction = float(input("Enter molar extinction coefficient of your substrate.\n"))
enzyme_concentration = float(input("Enter concentration of your enzyme (in µM).\n"))
concentrations_run = int(input("How many concentrations did you run trials for?\n"))

trial_concentrations = []
print("Enter the concentrations (in µM) at which you ran trials. Press enter after each value.")
for t in range(0, concentrations_run):
    trial_concentrations.append(input())
print(trial_concentrations)

number_of_trials = []
for n in range(0, len(trial_concentrations)):
    number_of_trials.append(int(input("How many trials did you run at  " + trial_concentrations[n] + " µM\n")))

yes_or_no_individual, yes_or_no_overall = other_functions.time_bound_input_checker()
need_time_bounds = True
if yes_or_no_overall == "yes":
    start_time = int(input("Enter your desired default start_time.\n"))
    end_time = int(input("Enter your desired default end time.\n"))
    need_time_bounds = False
elif yes_or_no_individual == "yes":
    need_time_bounds = False

average_velocities = []
for i in range(0, len(trial_concentrations)):
    temp_value_holder = []  # stores individual trial values per concentration; resets each iteration
    m = 1
    while m < number_of_trials[i] + 1:
        print("Select file with data for Trial " + str(m) + " at " + trial_concentrations[i] + " µM.\n")
        path = file_interpreter.request_file()
        first_column, second_column = file_interpreter.read_file(path)
        x_values, y_values = file_interpreter.initialize_array(first_column, second_column)
        if yes_or_no_individual == "yes":
            start_time, end_time = other_functions.get_time_bounds(x_values)
            need_time_bounds = False
        if need_time_bounds is True:
            start_time, end_time = graph_functions.find_best_bounds(x_values, y_values)
            print("bounds: " + str(start_time) + ", " + str(end_time))
        start_value = file_interpreter.get_absorption(y_values, start_time)
        end_value = file_interpreter.get_absorption(y_values, end_time)
        velocity = abs(
            file_interpreter.find_velocity(start_value, start_time, end_value, end_time, enzyme_concentration,
                                           molar_extinction))
        temp_value_holder.append(velocity)
        print("velocities: " + str(temp_value_holder))
        m += 1
    index = 0
    velocity_sum = 0
    for index in range(0, m - 1):
        velocity_sum += temp_value_holder[index]
    concentration_velocity_average = velocity_sum / (m - 1)
    average_velocities.append(concentration_velocity_average)
print("Average Velocities: " + str(average_velocities))
graph_functions.plot_from_arrays(trial_concentrations, average_velocities)

