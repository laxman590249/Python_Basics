

class A:
    def __init__(self):
        print("A", end=',')

class B:
    def __init__(self):
        print("B1", end=',')

    def __init__(self, temp= 2):
        print(f"B{temp}", end=',')

class C:
    def __init__(self):
        print("C", end=',')

class D(B, C, A):
    def __init__(self):
        super().__init__()
        print("D", end=',')

D()
print('Finish')