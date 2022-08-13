
a = 10

class A:

    def __init__(self):
        self.a = 1
        globals()['a'] = 20
        print(globals()['a'])


A()