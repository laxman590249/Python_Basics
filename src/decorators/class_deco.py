

class MyDecoratorClass:

    def __init__(self, function):
        self.function = function

    def __call__(self, var_1):
        print('Called MyDecoratorClass')
        self.function(var_1)


@MyDecoratorClass
def my_function(var):
    print('Called my_function()')
    print(var)

my_function(10)
