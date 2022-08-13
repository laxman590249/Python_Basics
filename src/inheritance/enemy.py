class Enemy:

    # def __init__(self):
    #     self.name = 'Hello'
    #     self.hit_points = 20
    #     self.lives = 2

    def __init__(self, name="Enemy", hit_points=0, lives=0):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_revenge(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print(f'I took {damage} points and remaining points are {self.hit_points}')
        else:
            self.lives -= 1

    def __str__(self):
        return f'Name: {self.name}, Lives: {self.lives}, HIT Points: {self.hit_points}'

    def kill(self):
        print('Killing Enemy')


class Troll(Enemy):

    def __init__(self, name):
        super().__init__(name=name, hit_points=1, lives=2)

    def kill(self):
        print('Killing Troll')
        super().kill()
