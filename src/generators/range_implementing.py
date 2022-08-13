import sys

_ = input('We are at line 3')

#generator
def my_range(n : int):
    _ = input('We are in my_range line 5')
    start = 0
    print('Starting my_range method...')
    while start < n:
        print('Printing value : ', start)
        _ = input('We are in my_method line 11')
        yield start
        start += 1


def simple_method(n : int):
    _ = input('We are in simple_method line 15')
    print('printing number ', n)
    return n


_ = input('We are at line 18')
m_range = my_range(5)
v_range = range(1000)
m_list = list(v_range)
k = simple_method(10)

# print(sys.getsizeof(m_range))
# print(sys.getsizeof(v_range))
# print(sys.getsizeof(m_list))

_ = input('We are at line 23')
for i in m_range:
    pass

