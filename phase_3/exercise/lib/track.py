class Track:
    def __init__(self, title, artist):
        if type(title) != str or type(artist) != str:
            raise Exception("Error, artist is not a string") 
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        # keyword is a string
        # Returns true if the keyword matches either the title or artist
        if keyword in self.title or keyword in self.artist:
            return True
        return False