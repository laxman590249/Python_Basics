
list_numbers = [1, 2, 3, 4, 5, 6]


def double_it(number, n = 10):
    return str(number * 2)


list_result = list(map(double_it, list_numbers))
print(list_result)