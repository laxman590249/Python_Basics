

class A:

    # def __new__(cls, *args, **kwargs):
    #     print('New A')

    def __init__(self):
        print('a', 1)
        # super().__init__()
        print('a', 2)


class B:

    # def __new__(cls, *args, **kwargs):
    #     print('New B')

    def __init__(self):
        print('b', 1)
        # super().__init__()
        print('b', 2)

class C(A,B):
    pass

    # def __new__(cls, *args, **kwargs):
    #     print('New C')

    def __init__(self):
        super().__init__()
        # A.__init__(self)
        # B.__init__(self)
        print('c')


p = C()
print(p)