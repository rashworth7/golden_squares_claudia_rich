from lib.diary_entry import DiaryEntry
from lib.diary import Diary

"""
test that diary.add returns instance of diary entry
"""
def test_diary_add_adds_diary_entry():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Title 1", "Contents 1")
    diary_entry_2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    result = diary.all()
    assert result == [diary_entry_1, diary_entry_2]

def test_count_words_diary_integrated_with_diary_entry_count_words():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Title 1", "Contents of the Diary")
    diary_entry_2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    result = diary.count_words()
    assert result == 6
    
def test_diary_reading_time_integrated_diary_entry_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Title 1", "Contents of the Diary")
    diary_entry_2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    result = diary.reading_time(5)
    assert result == 1

def test_diary_best_entry_for_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Title 1", "Contents of the Diary")
    diary_entry_2 = DiaryEntry("Title 2", "Contents 2")
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    result = diary.find_best_entry_for_reading_time(1, 2)
    assert result == diary_entry_2