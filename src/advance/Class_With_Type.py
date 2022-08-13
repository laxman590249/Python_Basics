

def method(self):
    print('Called')

class A:
    def __init__(self):
        print('A')


# Creating dynamic classes
Test = type('Test', (A,), dict(x='Name', y=method))

obj =Test()

print(obj.x)
print(obj.y())


