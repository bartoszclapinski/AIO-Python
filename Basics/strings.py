print("Today is a good day to learn Python")
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("Hello" + " world")

greeting = "Hello"
name = "Bruce"

# if we want a space, we can add that too
print(greeting + ' ' + name)

# The above is a bit messy, so we can do this instead:
print(greeting + name)

# We can also do this:
name = input("Please enter your name ")
print(greeting + ' ' + name)

age_in_words = "2 years"
print(name + " is " + age_in_words + " years old")
age = 24
print(name + " is " + age + " years old") # This will throw an error

# To fix the above error, we can do this:
print(name + " is " + str(age) + " years old")
print(type(age))
print(name + f" is {age} years old")
print(type(age))

print('#' * 40)
print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
