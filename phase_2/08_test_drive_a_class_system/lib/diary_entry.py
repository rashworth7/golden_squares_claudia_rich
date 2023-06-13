class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.start_index = 0
        self.words_read = []

    def count_words(self):
        words_list = self.contents.split()
        return len(words_list)
        # Returns:
        #   An integer representing the number of words in the contents

    def reading_time(self, wpm):
        return round(self.count_words()/wpm)
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass

    def reading_chunk(self, wpm, minutes):
        num_words = wpm * minutes
        contents = self.contents.split()

        if contents == self.words_read:
            self.words_read = []

        if self.words_read != []:
            reading_chunk = contents[len(self.words_read):]
            if num_words < len(reading_chunk):
                words_to_read = reading_chunk[:num_words]
                
            else:
                words_to_read = reading_chunk

        else:
            words_to_read = contents[:num_words]

        for word in words_to_read:
            self.words_read.append(word)
        
        return " ".join(words_to_read)

        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
       


diary_entry = DiaryEntry("Title 1", "Contents of the Diary")
diary_entry.reading_chunk(1, 3)
result = diary_entry.reading_chunk(1, 3)
print(result)