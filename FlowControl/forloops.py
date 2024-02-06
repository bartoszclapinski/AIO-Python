parrot = "Norwegian Blue"

for char in parrot:
    print(char)

number = "9,223;372:036 854,775;807"
separators = ""
numbers = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
    else:
        numbers = numbers + char

print(separators)
print(numbers)
print(sum(int(i) for i in numbers))

# Challenge
# Create a program to print out the capital letters in the quote
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

capitals = ""
for char in quote:
    if char.isupper():
        capitals = capitals + char

print(capitals)


    