t = "a", "b", "c"
print(t)

t = ("a", "b", "c")
print(t)

name = "Tim"
age = 28
print(name, age, "Python", 2024)
print((name, age, "Python", 2024))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# metallica[0] = "Master of Puppets"
# We cannot assign to a tuple, tuples are immutable

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
         ("Bad Company", "Bad Company", 1974),
         ("Nightflight", "Budgie", 1981),
         ("More Mayhem", "Emilda May", 2011),
         ("Ride the Lightning", "Metallica", 1984)]

print(len(albums))

for album in albums:
    print("Album: {}, Artist: {}, Year: {}".format(album[0], album[1], album[2]))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

