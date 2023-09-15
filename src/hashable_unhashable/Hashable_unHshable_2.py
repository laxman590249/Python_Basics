class X2(set):

    def __hash__(self):
        return hash(tuple(self))


set_1 = set()
hashable = X2()
set_1.add(hashable)