
def chain(n):
    print('value: ', n)
    return n


args = [1, 2, 3]

print('Generator Object: ', (chain(n) for n in args))
print('Result: ', *(chain(n) for n in args)) # It calls the generator