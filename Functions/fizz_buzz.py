def fizz_buzz(number: int) -> str:
    """
    Play Fizz Buzz game.
    
    Return 'fizz' if number is divisible by 3.
    Return 'buzz' if number is divisible by 5.
    Return 'fizz buzz' if number is divisible by both 3 and 5.
    Return the number as string if none of the above conditions are met.
    
    :param number: The number to check.
    :return: The appropriate response as a string.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


# Test loop for numbers 1-100
for i in range(1, 101):
    print(f"{i}: {fizz_buzz(i)}")