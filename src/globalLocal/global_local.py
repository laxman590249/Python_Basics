

var_1 = 20

class A:
    var_2 = 10

    def method(self):
        var_3 = 30
        print(locals())
        print(globals())


print(locals())
print(globals())

a = A()
a.method()