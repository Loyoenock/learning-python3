def make_album(artist_name, music_title, song_num=""):
    """
        Return Dictionary with artist name and music title
    
    """
    if song_num:
        album = {'name': artist_name, 'music': music_title, 'songs': song_num}
    else:
        album = {'name': artist_name, 'music': music_title}
    return album

musician = make_album('Aaron Joshua', 'Kadosh Ata')
print(musician)
musician = make_album('Paul Wilbur', 'Let God Araise', 6)
print(musician)
musician = make_album('Aaron Strout', 'He reigns')
print(musician)
