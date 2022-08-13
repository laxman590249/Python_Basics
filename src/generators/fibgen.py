
def fib_gen():
    print('Cam')
    current, previous = 0, 1
    while True:
        current, previous = current + previous, current
        yield current


fib = fib_gen()
fib_gen()
fib_gen()
fib_gen()
print('After')

print(next(fib_gen()))
print(next(fib_gen()))
for i in range(10):
    print(next(fib))
