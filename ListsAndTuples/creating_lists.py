empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = sorted("432985617")
print(digits)
print(digits.sort())
print(digits.sort(reverse=True))

more_numbers = list(numbers)
print(more_numbers)
print(id(numbers))
print(id(more_numbers))

another_numbers = numbers[:]
print(another_numbers)
print(id(numbers))
print(id(another_numbers))
print(numbers is another_numbers)
print(numbers == another_numbers)

and_another_numbers = numbers.copy()
print(and_another_numbers)
print(id(numbers))
print(id(and_another_numbers))
print(numbers is and_another_numbers)
print(numbers == and_another_numbers)
