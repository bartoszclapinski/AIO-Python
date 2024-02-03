letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[0:26:1])
backwards = letters[25:0:-1]
print(backwards)    # zyxwvutsrqponmlkjihgfedcba
print(letters[25::-1])  # zyxwvutsrqponmlkjihgfedcba

# Challenge: Use slicing to produce the following strings:
# qpo
# edcba
# the last 8 characters in reverse order
print("Challenge: Use slicing to produce the following strings:")
print(letters[16:13:-1])   # qpo
print(letters[25:17:-1])   # edcba
print(letters[:-9:-1])   # zyxwvuts

print('#' * 20)
print(letters[-4:])  # wxyz
print(letters[-1:])  # z
print(letters[:1])  # a
print(letters[0])  # a
