
"""
The *iterable syntax in Python is used to unpack an iterable (such as a list, tuple, or string) into individual elements.
It allows you to pass multiple arguments or values from an iterable to a function or to assign them to separate variables.

"""
numbers = [1, 2, 3]

# Unpacking iterable into a new list
new_list = [*numbers, 4, 5]
print(new_list)

# Unpacking iterable into separate variables
a, b, c = numbers
print(a, b, c)

def chain(n):
    print('value: ', n)
    return n

args = [1, 2, 3]

print('Generator Object: ', [chain(n) for n in args]) # It will be running
print('Generator Object: ', (chain(n) for n in args)) # Generator Object
print('Result: ', *(chain(n) for n in args)) # It unpacks the generator object (Iterable object)

print([*(chain(n) for n in args), 4, 5, 6]) # Think about it how is it working
