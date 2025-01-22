def multiply(x, y):
    result = x * y
    return result


def is_palindrome(word):
    backwards = word[::-1].casefold()
    return backwards == word.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)


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

