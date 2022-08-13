
class Player:

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return  self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print('Lives can not be negative')
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score


    def __str__(self):
        return f'Name : {self.name}, lives : {self.lives}, Score : {self.score}'


if __name__ == '__main__':
    tim_player = Player('Tim')
    tim_player.lives = 10
    tim_player.score_set = 20
    print(tim_player)

