def multiply(x, y):
    """
    Multiplies two numbers

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
 
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    return x * y
    #return result


def is_palindrome(word):
    """
    Check if a word is a palindrome.

    A palindrome is a word that reads the same forwards and backwards.

    :param word: The word to check.
    :return: True if the word is a palindrome, False otherwise.
    """
    backwards = word[::-1].casefold()
    return backwards == word.casefold()


def palindrome_sentence(sentence):
    """
    Check if a sentence is a palindrome.

    A palindrome is a sentence that reads the same forwards and backwards.

    :param sentence: The sentence to check.
    :return: True if the sentence is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


def sum_eo(n, t):
    """
    Sum even or odd numbers in a given range.

    :param n: The end of the range (inclusive).
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of even or odd numbers in the range.
    """
    if t not in ['e', 'o']:
        return -1
        
    start = 2 if t == 'e' else 1
    return sum(range(start, n, 2))


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

word = input("Enter a word: ")
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

sentence = input("Enter a sentence: ")
if palindrome_sentence(sentence):
    print(f"{sentence} is a palindrome")
else:
    print(f"{sentence} is not a palindrome")


answer = multiply(18, 3)
print(answer)
