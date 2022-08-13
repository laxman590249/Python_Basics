import timeit

text = 'What is in the next meeting'


def comp_test():
    cap_1 = [char.upper() for char in text]
    cap_2 = [char.upper() for char in text.split(' ')]
    # print(cap_1)
    # print(cap_2)


# Converting into Map
def map_test():
    list_1 = list(map(str.upper, text))
    list_2 = list(map(str.upper, text.split(' ')))
    # print(list_1)
    # print(list_2)


if __name__ == "__main__" :
    print(timeit.timeit(map_test, number=100000))
    print(timeit.timeit(comp_test, number=100000))

