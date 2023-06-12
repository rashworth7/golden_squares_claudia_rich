from lib.diary_entry import DiaryEntry

def test_count_words():
    diary_entry = DiaryEntry("Title 1", "Contents of the Diary")
    num_words = diary_entry.count_words()
    assert num_words == 4

def test_reading_time():
    diary_entry = DiaryEntry("Title 1", "Contents of the Diary")
    result = diary_entry.reading_time(1)
    assert result == 4

def test_reading_chunk():
    diary_entry = DiaryEntry("Title 1", "Contents of the Diary")
    result = diary_entry.reading_chunk(1, 2)
    assert result == "Contents of"

def test_reading_chunk_loop():
    diary_entry = DiaryEntry("Title 1", "Contents of the Diary")
    diary_entry.reading_chunk(1, 3)
    result = diary_entry.reading_chunk(1, 3)
    assert result == "Diary"

def test_reading_chunk_loop():
    diary_entry = DiaryEntry("Title 1", "Contents of the Diary")
    diary_entry.reading_chunk(1, 5)
    result = diary_entry.reading_chunk(1, 3)
    assert result == "Contents of the"