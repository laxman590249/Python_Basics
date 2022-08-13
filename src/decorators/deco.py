

def deco(a):
    def foo1(fun):
        def foo2(c):
            def foo(b):
                print(fun(a))
                print('Coming', a)
                return 2
            return foo
        return foo2
    return foo1

# Whatever paramter we are passing here, will be decorators argument the inner method's argument will be the calling funcion
@deco(3)
def sq(a):
    return 2**10

print(sq(2)(20))