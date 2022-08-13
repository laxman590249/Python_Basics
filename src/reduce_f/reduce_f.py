from _functools import reduce

numbers = [1, 3, 5, 8, 12]


def sum_fun(a, b, c = 20):
    return a + b + c


result = reduce(sum_fun, numbers)

print(result)
