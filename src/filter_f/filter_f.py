import timeit


menu = [['Egg', 'Meat', 'Spam'],
        ['Egg', 'Meat', 'Dahi'],
        ['Egg', 'Meat', 'Icecrea'],
        ['Icecrea', 'Dahi', 'Spam'],
        ['Egg', 'Meat', 'Dhokla']]


def spamless_compresension():
    return [meal  for meal in menu if 'Spam' not in meal]


def spamless_compresension_f():
    return [meal for meal in menu if not_spam(meal)]


def not_spam(list_menu : list):
    return 'Spam' not in list_menu


def spamless_filter():
    return list(filter(not_spam, menu))

if __name__ == '__main__':
    print(spamless_compresension())
    print(spamless_filter())
    print(timeit.timeit(spamless_compresension, number=100000))
    print(timeit.timeit(spamless_compresension_f, number=100000))
    print(timeit.timeit(spamless_filter, number=100000))

