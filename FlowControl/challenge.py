name = input(print('Please enter your name: '))
age = int(input(print('How old are you, {0}? '.format(name))))

if age and name:
    if 18 <= age < 31:
        print("Welcome to the holiday {}.".format(name))
    else:
        print("Sorry, you are not allowed to join the holiday")
else:
    print("Please enter your name and age")
