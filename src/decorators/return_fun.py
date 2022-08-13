

def hello(name = 'Jose'):
    print('hello() Function is called.')

    def greet():
        print('The greet function from inside hello() function')

    def welcome():
        print('The welcome function from inside hello() function')

    if name == 'Jose':
        return greet
    else:
        return welcome


inside_function = hello()
print('Took in variable')

print(inside_function())