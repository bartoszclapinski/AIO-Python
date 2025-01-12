albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
        (1, "Welcome to my Nightmare"),
        (2, "Devil's Food"),
        (3, "The Black Widow"),
        (4, "Some Folks"),
        (5, "Only Women Bleed")
     ]
    ),
    ("Bad Company", "Bad Company", 1974,
     [
        (1, "Can't Get Enough"),
        (2, "Rock Steady"),
        (3, "Ready for Love"),
        (4, "Don't Let Me Down"),
        (5, "Bad Company"),
        (6, "The Way I Choose"),
        (7, "Movin' On"),
        (8, "Seagull")
     ]
    ),
    ("Nightflight", "Budgie", 1981,
     [
        (1, "I Turned to Stone"),
        (2, "Keeping a Rendezvous"),
        (3, "Reaper of the Glory"),
        (4, "She Used Me Up")
     ]
    ),
    ("More Mayhem", "Emilda May", 2011,
     [
        (1, "Pulling the Rug"),
        (2, "Psycho"),
        (3, "Mayhem"),
        (4, "Kentish Town Waltz")
     ]
    )
]

for name, artist, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}, Songs: {}".format(name, artist, year, songs))

print("=" * 50)

album = albums[2]
print(album)

print("=" * 50)

songs = album[3]
print(songs)

print("=" * 50)

song = songs[3]
print(song)

print("=" * 50)

title, track = song
print(title)
print(track)

print("=" * 50)

title, artist, year, songs = album
print(title)
print(artist)
print(year)
print(songs)

print("=" * 50)

print(song)
print(song[1])

mayhem = albums[3][3][3]
print(mayhem)

print("=" * 50)

print(albums[3][3][2][1])

print("=" * 50)

print(albums[3])
print(albums[3][3])
print(albums[3][3][2])
print(albums[3][3][2][1])

# Tytuł piosenki "The Way I Choose" z albumu "Bad Company"
print(albums[1][3][5][1])

# Rok wydania albumu "Nightflight"
print(albums[2][2])

# Numer ścieżki piosenki "Kentish Town Waltz"
print(albums[3][3][3][0])

# Krotka reprezentująca piosenkę "Keeping a Rendezvous"
print(albums[2][3][1])
