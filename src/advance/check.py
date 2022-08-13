
def MyGenerator():
    num = 0
    while num < 10:
        num += 1
        yield num

class MyOwn:

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num >= 0:
            self.num += 1
            return self.num

iterator = iter(MyOwn())
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


