
class A:
    def __init__(self):
        self.db = self.Inner()

    def display(self):
        print('In Parent Class')

    # this is inner class
    class Inner:

        def display1(self):
            print('Inner Of Parent Class')


class B(A):
    def __init__(self):
        super().__init__()
        print('In Child Class')


    class Inner(A.Inner):

        def display2(self):
            print('Inner Of Child Class')


# creating child class object
p = B()
p.display()

# create inner class object
x = p.db
x.display1()
x.display1()

inner_b = B.Inner
inner_b().display2()