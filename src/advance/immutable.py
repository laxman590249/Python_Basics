from operator import itemgetter

class Point(tuple):
    __slots__ = []
    def __new__(cls, x, y, k):
        return tuple.__new__(cls, (x, y, k))
    x = property(itemgetter(0))
    y = property(itemgetter(1))
    z = property(itemgetter(2))


print(property(itemgetter((5,21))))

li = [1]
p = Point(2, 3, li)
print(p.x)
# p.k = 20
# 2
print(p.z)
# 3

