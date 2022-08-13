

def factorial(n):
    try:
        if n == 1:
            return n
        else:
            return n * factorial((n-1))
    except (ArithmeticError, OverflowError, RecursionError, TypeError):
        print('Error is there')
        return n


print(factorial(900))


def get_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print('Eneter A valid number')


print(get_int('Enter First Number : '))
print(get_int('Enter Second Number : '))


