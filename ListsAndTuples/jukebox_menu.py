from albums_data import albums

SONGS_LIST_INDEX = 3

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")
    
    album_choice = int(input())
    if 1 <= album_choice <= len(albums):
        songs_list = albums[album_choice - 1][SONGS_LIST_INDEX]        
    else:
        break

    print(albums[album_choice - 1])
    print(songs_list)


    

