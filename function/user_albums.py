def make_album(artist_name, music_title, song_num=""):
    """
        Return Dictionary with artist name and music title
    
    """
    if song_num:
        album = {'name': artist_name, 'music': music_title, 'songs': song_num}
    else:
        album = {'name': artist_name, 'music': music_title}
    return album
while True:
    print("\Please Enter Artist name: ")
    print("(Input 'q' to quit at anytime)")

    author = input("Artist name: ")
    if author == 'q':
        break
    album_title = input("Please enter album title ")
    if album_title == 'q':
        break

user_album = make_album(author, album_title)
print(f"\nUser Album: {user_album}")
