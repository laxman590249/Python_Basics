

def MyGenerator():
    """
    It is a generator
    """
    num = 0
    while num < 10:
        num += 1
        yield num


class MyOwn:
    """
    Here we defined the Iterator
    """

    def __init__(self, limit):
        self.num = 0
        self.limit = limit

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num > self.limit:
            raise StopIteration
        if self.num >= 0:
            self.num += 1
            return self.num


for i in MyOwn(10):
    print(i)

iterator = MyOwn(10)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

gen = iter(MyGenerator())
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


