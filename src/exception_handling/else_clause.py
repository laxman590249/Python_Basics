import sys


def check_exception_1():

    try:
        print('Hello Try')
    except ZeroDivisionError:
        print('Hello Error')
    else:
        print('Hello else')
    finally:
        print('Hello Its Finally')


def check_exception_2():

    try:
        print('Hello Try_2')
        sys.exit(0)
    except ZeroDivisionError:
        print('Hello Error 2')
        sys.exit(0)
    else:
        print('Hello Finally 2')



check_exception_1()
check_exception_2()

