import sys


def check_exception_1():

    try:
        print('Hello Try')
        x = 10 / 0
    except ZeroDivisionError:
        print('Hello Error')
        return 0
    finally:
        print('Hello Finally')


def check_exception_2():

    try:
        print('Hello Try_2')
        x = 10 / 0
    except ZeroDivisionError:
        print('Hello Error 2')
        sys.exit(0)
    finally:
        print('Hello Finally 2')

check_exception_1()
check_exception_2()

