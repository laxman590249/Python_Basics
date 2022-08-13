

class Song:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Album:

    def __init__(self, name, list_song):
        self.name = name
        list_song = list_song


class Artist:

    def __init__(self, name, age, list_album):
        self.name = name
        self.age = age
        self.list_album = list_album
