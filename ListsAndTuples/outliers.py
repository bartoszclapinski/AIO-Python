data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
print(data)

del data[0:2]
print(data)

del data[-2:]
print(data)

min_valid = 100
max_valid = 200

data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):        
        del data[index]
print(data)

data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break;

print(stop)
del data[:stop]
print(data)

data = [4, 5, 104, 105, 110, 120, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break;

print(start)
del data[:start]
print(data)
