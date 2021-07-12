import graph_functions

def track_data():
    concentrations = []
    trials_per_concentration = []
    data = []
    trial_validity = []
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
                    data.append(float(next_trial_input))x`
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
        trials_per_concentration.append(int(current_trial))
    print("concentrations: " + str(concentrations))
    print("trials_per_concentration: " + str(trials_per_concentration))
    print("trial_validity statuses: " + str(trial_validity))
    print("Data stored in csv file *insert file path here*.")
    return concentrations, trials_per_concentration, trial_validity  # eventually, return path of csv file instead
