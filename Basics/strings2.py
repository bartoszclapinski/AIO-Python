#         0123456789
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])

# Challenge: Print "We win" using the parrot variable
print('Challenge: Print "We win" using the parrot variable')
print(parrot[3])    # w
print(parrot[4])    # e
print(parrot[9])    # _
print(parrot[3])    # w
print(parrot[6])    # i
print(parrot[8])    # n

print('#' * 20)
print(parrot[-1])   # e

# Challenge: Print "We win" using the parrot variable and negative indices
print('Challenge: Print "We win" using the parrot variable and negative indices')
print(parrot[-11])  # w
print(parrot[-10])  # e
print(parrot[-5])   # _
print(parrot[-11])  # w
print(parrot[-8])   # i
print(parrot[-6])   # n

print('#' * 20)
print(parrot[0:6])  # Norweg
print("[start(including):stop(not including)]")
print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
print(parrot[:9])   # Norwegian

# Challenge: Print "Blue" using the parrot variable and slicing
print('Challenge: Print "Blue" using the parrot variable and slicing')
print(parrot[10:])

print('#' * 20)
print(parrot[:6])
print(parrot[6:])
print(parrot[:6] + parrot[6:])
print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"

print('#' * 20)
print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl

print('#' * 20)
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

print('#' * 20)
number = "9,223;372:036 854,775;807"
print(number[1::4])     # ,;: ,;
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
