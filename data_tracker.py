in_data = input("Enter the current substrate concentration. Enter 'no' to exit "
                "loop.\n")
concentrations = {}


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


while not in_data == "no":
    concentration = float(in_data)
    concentrations[concentration] = []
    next_occurrence = input("Enter trial\n")
    while not next_occurrence == "no":
        keep_value = str2bool(input("keep?"))
        concentrations[concentration].append((float(next_occurrence), keep_value))
        next_occurrence = input("Enter trial\n")
    in_data = input("Enter the current substrate concentration. Enter 'no' to exit "
                    "loop.\n")
print(concentrations)

for i, concentration in enumerate(concentrations.keys()):
    print("data for trial: ", str(i))
    for j, trial in enumerate(concentrations[concentration]):
        trial_value, trial_validity = trial
        print("trial" + str(j) + "value: ", trial_value)
        print("trial" + str(j) + "validity: ", trial_validity)


def track_data():
    continue_running = True
    concentrations = []
    trials_per_concentration = []
    data = []
    while continue_running is True:
        concentration_valid = False
        while concentration_valid is False:
            next_occurrence = input("Enter the current substrate concentration. Enter 'no' to exit "
                                    "loop.\n")
            if next_occurrence == "no":
                concentration_valid = True
            else:
                try:
                    concentrations.append(next_occurrence)
                    concentration_valid = True
                except TypeError:
                    print("Input not recognized. Enter the concentration or enter 'no' to exit loop.")
                    concentration_valid = False
                    break
        current_trial = 0
        are_more_trials = True
        while are_more_trials is True:
            current_trial += 1
            next_trial_input = input("Enter data for Trial " + str(current_trial) + " at " + str(
                next_occurrence) + ". Enter 'no' to exit loop.\n")
            if next_trial_input == "no":
                current_trial -= 1
                are_more_trials = False
            else:
                data.append(next_trial_input)
        trials_per_concentration.append(current_trial)
    print("concentrations: " + str(concentrations))
    print("trials_per_concentration: " + str(trials_per_concentration))
    print("Data stored in csv file *insert file path here*.")
    return concentrations, trials_per_concentration  # eventually, return path of csv file instead

# track_data()
