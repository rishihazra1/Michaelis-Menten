import graph_functions

def track_data():
    concentrations = []
    trials_per_concentration = []
    data = []
    trial_validity = []
    all_data = []
    index_tracker = 0
    while True:  # terminates when there are no more concentrations
        while True:  # terminates with valid user input
            next_occurrence = input("Enter the current substrate concentration (in µM). Enter 'no' to exit "
                                    "loop.\n")
            if next_occurrence == "no":
                break
            try:
                concentrations.append(float(next_occurrence))
                break
            except ValueError:
                print("Input not recognized. Enter the concentration or enter 'no' to exit loop.")
        if next_occurrence == "no":
            break
        current_trial = 0
        while True:  # terminates when there are no more trials for current concentration
            current_trial += 1
            while True:
                next_trial_input = input("Enter data for Trial " + str(current_trial) + " at " + str(
                    next_occurrence) + " µM. Enter 'no' to exit loop.\n")
                if next_trial_input == "no":
                    current_trial -= 1
                    break
                try:
                    data.append(float(next_trial_input))
                    break
                except ValueError:
                    print("Input not recognized. Enter the data value or enter 'no' to exit loop.")
            if next_trial_input == "no":
                break
            while True:  # terminates when user input for trial_validity is valid
                keep_trial = input("Would you like to keep the data for Trial " + str(current_trial) + " ? (yes/no)\n")
                if keep_trial == "yes":
                    trial_validity.append(True)
                    break
                elif keep_trial == "no":
                    trial_validity.append(False)
                    break
                else:
                    print("Input not recognized. Enter the concentration or enter 'no' to exit loop.")
            print(current_trial)
            temp_array = [next_occurrence, next_trial_input, trial_validity[len(trial_validity) - 1]]
            all_data.insert(index_tracker, temp_array)
            index_tracker += 1
            print(all_data)
        trials_per_concentration.append(int(current_trial))
    print("all_data: " + str(all_data))
    print("Data stored in csv file *insert file path here*.")
    return concentrations, data, trial_validity  # eventually, return path of csv file instead
