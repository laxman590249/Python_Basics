class L1(list):

    def __add__(self, other):
        return L1()


class L2(L1):
    n = 0

    def __init__(self):
        L2.n += 1


a = L2()
print(a.n, end=" ")
b = L2()
try:
    c = a + b
    print(b.n, end=" ")
    print(c.n, end=" ")
except:
    print(0)