class Song:
    """Class to represent song
    Attributes:
        title (str):The Title of the song
        artist (Artist):An Artist object represne the singer
        duration(int):Time of playing the song"""

    def __init__(self, title, artist, duration):
        """Song init method

        Args:
            title (str): Initialises the title attribute
            artist (Artist): An Artist object representing the creator of Song
            duration (Optional[int]): Initial value of duration, will be 0 if not provided
        """
        self.title = title
        self.artist = artist
        self.duration = duration


class Artist:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    song = Song('No One', Artist('Laxman', 23), 4)
    # With help of help() mthod
    help(Song)
    help(Song.__init__)

    # Using __doc__ attribute
    print(Song.__doc__)
    print(Song.__init__.__doc__)

    Song.__init__.__doc__ =  """Updated the documentation"""
    help(Song)
    #print(Song.__init__.__doc__)
