import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue to prompt the user for a number until a valid
    integer is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{0} is not a valid number".format(temp))


print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)

help(get_integer)

highest = 10
answer = random.randint(1, highest)
print(answer)  # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = get_integer(": ")

# Challenge
while guess != answer:
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Pleas guess lower")
    else:
        print("You got it first time")
        break
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

# if guess == answer:
#     print("Well done, you guessed it")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
