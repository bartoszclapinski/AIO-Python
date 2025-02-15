LOW = 1
HIGH = 1000

#print("Please think of a number between {} and {}".format(low, high))
#input("Press ENTER to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        guess = low + (high - low) // 2
        if guess < answer:
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        else:
            return guesses
        
        guesses += 1


correct_count = 0   
max_guesses = 0

for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))
    
    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1

print("I guessed without being told {} times".format(correct_count))
print("The maximum number of guesses was {}".format(max_guesses))

