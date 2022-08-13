

print('Line 5...')
def my_range(n : int):
    start = 0
    print('Starting my_range method...')
    while start < n:
        # print('Printing value : ', start)
        yield start
        start += 1


big_range = my_range(5)
print('Created')
print(next(big_range))
print('Line 15...')

for i in big_range:
    print(i)

