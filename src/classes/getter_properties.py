
class Song:

    title = 'Apna Song'

    def __init__(self, title, duration, album):
        self.title = title
        self.duration = duration
        self.album = album

    def get_title(self):
        return self.title

    def set_title(self, s):
        self.title = s

    def get_album(self):
        return self.album

    def del_title(self):
        del self.title

    name = property(get_title, set_title, del_title, "I am the album property.")

    def __str__(self):
        return 'Hello'



song = Song('Aaja Mitwa', 'Laxman', 'Kabhi Alvida na Kahna')
print(song.name)

song.name = '2'
print(song.name)
print('Before delete', song.__dict__)
del song.name
print('After Delete', song.__dict__)


