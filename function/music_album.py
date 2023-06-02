def make_album(artist_name, music_title):
    """Return Dictionary with artist name and music title"""
    album = {'name': artist_name, 'music': music_title}
    return album

musician = make_album('Aaron Joshua', 'Kadosh Ata')
print(musician)
musician = make_album('Paul Wilbur', 'Let God Araise')
print(musician)
musician = make_album('Aaron Strout', 'He reigns')
print(musician)
