a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down towards minus infinity
print(a % b)    # 0 modulo: the remainder after integer division

print('#############')
for i in range(1, a // b):
    print(i)

print('#############')
i = 1
print(i)
i = 2
print(i)
i = 3
print(i)

print('#############')
# Operator precedence
print(a + b / 3 - 4 * 12)   # 12 + 1 - 48 = -35
print(a + (b / 3) - (4 * 12))   # 12 + 1 - 48 = -35
print((((a + b) / 3) - 4) * 12)   # ((15 / 3) - 4) * 12 = 12
print(((a + b) / 3 - 4) * 12)   # ((15 / 3) - 4) * 12 = 12

c = a + b
d = c / 3
e = d - 4
print(e * 12)   # 12

# PEMDAS - Parentheses, Exponents, Multiplication and Division (left-to-right), Addition and Subtraction (left-to-right)
# BODMAS - Brackets, Orders, Division and Multiplication (left-to-right), Addition and Subtraction (left-to-right)
# BIDMAS - Brackets, Indices, Division and Multiplication (left-to-right), Addition and Subtraction (left-to-right)
# BEDMAS - Brackets, Exponents, Division and Multiplication (left-to-right), Addition and Subtraction (left-to-right)
print('#############')
print(a / (b * a) / b)   # 12 / 36 / 3 = 0.1111111111111111
print(a / (b * (a / b)))   # 12 / (36 / 3) = 1.0
