class Enemy():

    def __init__(self, name="Enemy", hit_points=0, lives=0):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def __init__(self, v):
        self.name = 'Hello'
        self.hit_points = 20
        self.lives = 2

    def __str__(self):
        return f'Name: {self.name.title()}, Lives: {self.lives}, HIT Points: {self.hit_points}'


enemy = Enemy()
print(enemy)
