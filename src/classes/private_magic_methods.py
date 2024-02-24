"""
__ methods does not accessible directly outside the class or child class

"""

class Base:

    # Declaring public method
    def fun(self):
        print("Public method")

    # Declaring private method
    def __fun(self):
        print("Private method")

    def __fun__(self):
        print("Magic method")


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        super().__init__()

    def call_public(self):
        # Calling public method of base class
        print("\nInside derived class")
        self.fun()

    def call_private(self):
        # Calling private method of base class
        self.__fun()
        # self._Base__fun() *** Accessible with this
        # super().__fun()   # *** Not Accessible with this -> It tries to call super()._Derived__fun()
        # super()._Base__fun() *** Accessible with this

    def call_magic(self):
        self.__fun__()
        # super().__fun__() # Accessible


# Driver code
obj1 = Base()

# Calling public method
obj1.fun()

obj2 = Derived()
obj2.call_public()

# obj1.__fun() *** Raise an error
# obj1._Base__fun() *** Accessible with this
# raise an AttributeError

# obj2.call_private()
obj2.call_magic()