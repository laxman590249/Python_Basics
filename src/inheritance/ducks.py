class Wing:

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print('Wee This is fun')
        elif self.ratio == 0:
            print('Tough, But I can fly')
        else:
            print('I can walk only')


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print('Waddle Waddle, Waddle')

    def swim(self):
        print('Come on in, Water is lovely')

    def quack(self):
        print('Quack Quack')

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self._wing = Wing(0.5)

    def walk(self):
        print('Waddle Waddle, Waddle')

    def swim(self):
        print('Come on in, Water is chilly little bit')

    def quack(self):
        print('Alaf Alaf Alaf')

    def fly(self):
        self._wing.fly()

def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()
    duck.fly()

if __name__ == '__main__':
    duck = Duck()
    test_duck(duck)

    penguin = Penguin()
    test_duck(penguin)

