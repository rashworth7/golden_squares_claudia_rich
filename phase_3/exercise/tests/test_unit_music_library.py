from unittest.mock import Mock
from lib.music_library import MusicLibrary

"""
Check add returns a list of added tracks
"""
def test_add():
    music = MusicLibrary()

    fake_not_match = Mock()
    fake_not_match.matches.return_value = False
    music.add(fake_not_match)

    fake_match = Mock()
    fake_match.matches.return_value = True
    music.add(fake_match)

    assert music.search("Hello") == [fake_match]


