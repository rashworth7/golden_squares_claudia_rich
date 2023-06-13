from lib.music_library import MusicLibrary
from lib.track import Track

"""
Given MusicLibrary
Add two track from Track
Check track added to library
"""

def test_integrate_add_two_tracks():
    music_library = MusicLibrary()
    track_1 = Track("Yellow", "Coldplay")
    track_2 = Track("Paradise", "Coldplay")
    music_library.add(track_1)
    music_library.add(track_2)
    result = music_library.track_list
    assert result == [track_1, track_2]


"""
Given MusicLibrary
Add two tracks as Track instances
Search returns track instances that match keyword
"""

def test_integrate_search():
    music_library = MusicLibrary()
    track_1 = Track("Yellow Brick Road", "Coldplay")
    track_2 = Track("Paradise", "Coldplay")
    music_library.add(track_1)
    music_library.add(track_2)
    result = music_library.search("Yellow")
    assert result == [track_1]