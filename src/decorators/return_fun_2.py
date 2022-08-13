

def super_cool(decorated_function):
    print('Called super_cool')
    def called_function():
        print('Called called_function')                                                             
        decorated_function()

    return called_function


@super_cool
def decarator_function():
    print('decarator_function')


a = decarator_function
print(a())