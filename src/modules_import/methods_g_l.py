
x = 1
def Foo():
    x = 20
    print(x)

    def Too():
        print(x)
        x = 10
    Too()
Foo()
print(x)
