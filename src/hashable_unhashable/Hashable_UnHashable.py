class Hashable(list):
    def __hash__(self):
        return hash(tuple(self))


class Unhashable:
    def __eq__(self, other):
        return  self == other


class HashableAgain:

    def __eq__(self, other):
        return self == other

    def __hash__(self):
        return id(self)


hashable = Hashable()
unhashable = Unhashable()
hashable_again = HashableAgain()


set_1 = set()
set_1.add(hashable_again)
