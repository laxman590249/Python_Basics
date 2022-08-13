x = 10
a = 100


def foo():
    global x
    print('Foo x', x)
    x += 1
    print('Foo Locals : ', locals())
    print('Foo Globals : ', globals())


foo()
print('Global x', x)
y = 11


def foo2():
    global y
    a = 30
    y = 10
    z = 100
    a = 10

    def foo3():

        a = 100

        def foo4():
            global a
            a = -1
            print('Foo4 a', a)
            print('Foo4 Locals : ', locals())
            print('Foo4 Globals : ', globals())
        foo4()
        print('Foo3 a', a)
        print('Foo3 Locals : ', locals())
    foo3()
    print('Foo2 a', a)
    print('Foo2 Y', y)
    print('Foo2 Locals : ', locals())
    print('Foo2 Globals : ', globals())


foo2()
print('Global a', a)
print('Global y', y)
print('Module Locals : ', locals())
print('Module Globals : ', globals())
