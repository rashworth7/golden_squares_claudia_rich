
class Diary:
    def __init__(self):
        self._list = [] #_list -> list is not to be used outside of the Diary class

    def add(self, entry):
        self._list.append(entry)
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._list

    def count_words(self):
        count = 0
        entries = self.all()
        for entry in entries:
            count += entry.count_words()
        return count
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        return round(self.count_words()/wpm)
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        

    def find_best_entry_for_reading_time(self, wpm, minutes):

        entries = self.all()

        reading_time_dict = {}
        for entry in entries:
            reading_time_dict[entry] = entry.reading_time(wpm)
       
        max = 0
        for item, value in reading_time_dict.items():
            if value <= minutes:
                if value > max:
                    max = value
                    best_value = item
        
        return best_value


        

        



        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass