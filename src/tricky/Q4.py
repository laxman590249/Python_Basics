def foo(a):
    def foo1(b):
        def foo2(c):
            def foo3(d):
                return b(a+c+d)
            return foo3
        return foo2
    return foo1

@foo(1)
def sq(num):
    return num ** 2


print(sq(3)(2))
