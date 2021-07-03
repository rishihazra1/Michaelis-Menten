def track_data():
    concentrations = []
    trials_per_concentration = []
    data = []
    while True:
        while True:
            next_occurrence = input("Enter the current substrate concentration. Enter 'no' to exit "
                                    "loop.\n")
            if next_occurrence == "no":
                break
            try:
                concentrations.append(next_occurrence)
                break
            except TypeError:
                print("Input not recognized. Enter the concentration or enter 'no' to exit loop.")
        if next_occurrence == "no":
            break
        current_trial = 0
        while True:
            current_trial += 1
            next_trial_input = input("Enter data for Trial " + str(current_trial) + " at " + str(
                next_occurrence) + ". Enter 'no' to exit loop.\n")
            if next_trial_input == "no":
                current_trial -= 1
                break
            else:
                data.append(next_trial_input)
        trials_per_concentration.append(current_trial)
    print("concentrations: " + str(concentrations))
    print("trials_per_concentration: " + str(trials_per_concentration))
    print("Data stored in csv file *insert file path here*.")
    return concentrations, trials_per_concentration  # eventually, return path of csv file instead

track_data()