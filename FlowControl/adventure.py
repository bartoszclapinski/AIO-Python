available_exits = ["north", "south", "east", "west"]
chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit == "quit":
        print("Game Over")
        break
    else:
        print("Aren't you glad you got out of there!")

# Challenge: create a while loop which stops when i is greater than 0 and divisible by 11
i = 0
while i < 100:
    if i > 0 and i % 11 == 0:
        break
    i += 1

# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

# Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5.
for i in range(0, 21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
