from lib.track import Track
import pytest

"""
Given Track
Check track matches returns True if keyword in title
"""

def test_matches_true_title():
    track = Track("Yellow", "Coldplay")
    result = track.matches("Yellow")
    assert result == True

"""
Given Track
Check track matches returns False if keyword not in title
"""

def test_matches_false_artist():
    track = Track("Yellow", "Coldplay")
    result = track.matches("Kings of Leon")
    assert result == False

    """
Given Track
Check track matches returns True if keyword in artist
"""

def test_matches_true_artist():
    track = Track("Yellow", "Coldplay")
    result = track.matches("Coldplay")
    assert result == True

def test_raise_error_if_title_or_artist_not_string():
    with pytest.raises(Exception) as err:
        Track(1, "Coldplay")
    assert str(err.value) == "Error, artist is not a string"

