# Python program to illustrate the concept
# of threading
# importing the threading module
import threading


def print_cube(num, n1):
    """
    function to print cube of given num
    """
    print("Cube: {}".format(num * num * num))

    for i in range(num):
        print(f'print_cube : {i} {threading.current_thread().name}')


def print_square(num, n2):
    """
    function to print square of given num
    """
    print("Square: {}".format(num * num))

    for i in range(num):
        print(f'print_square : {i} {threading.current_thread().name}')


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(100,20), name="t1")
    t2 = threading.Thread(target=print_cube, args=(100,20), name="t2")

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")