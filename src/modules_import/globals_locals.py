
y = 1


class MyClass:
    print(y)
    y = 20


    def my_method(self):
        y = 30
        print(y)


MyClass().my_method()
print(y)

