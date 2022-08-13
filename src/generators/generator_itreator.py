

def my_range(n : int):
    start = 0
    while start < n:
        yield start
        start += 1


big_generator = my_range(3)
big_iterator = range(3)

for i in big_generator:
    print('Generator ', i)
print()

for i in big_iterator:
    print('Iterator ', i)
print()

# Not going to reset
for i in big_generator:
    print('Generator ', i)

# Going to reset when it get completes.
for i in big_iterator:
    print('Iterator ', i)
