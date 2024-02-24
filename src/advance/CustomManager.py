"""
Managing Resources using context manager: Suppose a block of code raises an exception or if it has a complex algorithm
with multiple return paths, it becomes cumbersome to close a file in all the places. Generally in other languages when
working with files try-except-finally is used to ensure that the file resource is closed after usage even if there is
an exception. Python provides an easy way to manage resources: Context Managers. The with keyword is used. When it gets
evaluated it should result in an object that performs context management. Context managers can be written using classes
or functions(with decorators).
"""

# Define our own Context Manager


class CustomContextMgr:
    """
    This class supports the Context Manager Protocol

    """
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')


with CustomContextMgr() as mgr:
    print('with statement block')

