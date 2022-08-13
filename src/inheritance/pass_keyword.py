
class MyClass:
    pass


def checking_pass(i):
    if i == 3:
        pass
    print("Passed")

    for i in range(10):
        pass

    print(i)

checking_pass(3)

class A:

    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        print('a')

    def __call__(self, *args, **kwargs):
        print('Call')


class B(A):

    def __init__(self):
        # super().__init__(self)
        print('B')


print(B())