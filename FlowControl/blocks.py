for i in range(1, 13):
    print(i)
    if i == 7:
        break

# printing separator
print('#' * 40)

for i in range(1, 13):
    print("Number {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# printing separator
print('#' * 40)

# if - elif - else
if age >= 18:
    print("You are old enough to vote")
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("Please come back in {0} years".format(18 - age))
