
def odd_gen():
    x = 1
    while True:
        yield x
        x += 2


def pi_series():
    odds = odd_gen()
    approximation = 0
    while True:
        approximation += (4 / next(odds))
        yield approximation
        approximation -= (4 / next(odds))
        yield approximation


pi_ = pi_series()

for i in range(1000):
    print(next(pi_))
