import tkinter.filedialog
import matplotlib.pyplot as plt
import file_interpretation

start_time = 0
end_time = 45

print("Enter molar extinction coefficient of your substrate.")
molar_extinction = float(input())

print("Enter concentration of your enzyme (in µM).")
enzyme_concentration = float(input())

print("How many concentrations did you run trials for?")
concentrations_run = int(input())
print("Enter the concentrations (in µM) at which you ran trials. Press enter after each value.")
trial_concentrations = []
t = 0
while t < concentrations_run:
    trial_concentrations.append(input())
    t += 1

print(trial_concentrations)

number_of_trials = []
n = 0
while n < len(trial_concentrations):
    number_of_trials.append(int(input("How many trials did you run at the " + trial_concentrations[n] + " µM\n")))
    n += 1

print(number_of_trials)

average_velocities = []
x_values = []

for i in range(0, len(trial_concentrations)):
    temp_value_holder = []  # stores individual trial values per concentration; resets each iteration
    m = 1
    while m < number_of_trials[i] + 1:
        print("Select file with data for Trial " + str(m) + " at " + trial_concentrations[i] + " µM.\n")
        path = tkinter.filedialog.askopenfilename()
        print(path)
        first_column, second_column = file_interpretation.read_file(path)
        x_values = file_interpretation.initialize_array(first_column, second_column)
        start_value = file_interpretation.get_absorption(x_values, start_time)
        end_value = file_interpretation.get_absorption(x_values, end_time)
        velocity = abs(
            file_interpretation.find_velocity(start_value, start_time, end_value, end_time, enzyme_concentration,
                                              molar_extinction))
        temp_value_holder.append(velocity)
        print("velocities: " + str(temp_value_holder))
        m += 1
    index = 0
    velocity_sum = 0
#    print("m = " + str(m))
    for index in range(0, m - 1):
        velocity_sum += temp_value_holder[index]
    concentration_velocity_average = velocity_sum / (m - 1)
    average_velocities.append(concentration_velocity_average)
print("Average Velocities: " + str(average_velocities))

plt.scatter(trial_concentrations, average_velocities)
plt.show()
