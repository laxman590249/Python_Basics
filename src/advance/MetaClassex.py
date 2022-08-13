
class A():
    pass

class MyMeta(type):
    pass


class MyClass(metaclass=MyMeta):
    passlju


class MySubclass(MyClass):
    pass


print(type(A))
print(type(MyMeta))
print(type(MyClass))
print(type(MySubclass))
