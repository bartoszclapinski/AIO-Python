current_choice = "-"
available_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat", "hdmi cable"]
computer_parts = [] # create an empty list
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)
        
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
        print("0: to finish")

    current_choice = input()

print(computer_parts)
