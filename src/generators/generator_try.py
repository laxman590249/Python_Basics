

def generator_1():

    for x in range(10):
        print(x)
        yield x


a =generator_1()
next(a)
next(a)
next(a)

generator_1()