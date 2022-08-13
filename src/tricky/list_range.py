import sys

big_range = range(1000)
big_list = list(big_range)

print('Size of Range : ', sys.getsizeof(big_range))
print('Size of List : ', sys.getsizeof(big_list))