import copy
from operator import itemgetter

"""
The __slots__ attribute in Python allows you to explicitly define the attributes that an object can have. 

So for immutability we do not give anything in it so it can not be added later

We are inherting tuple and calling the __new__ of it

"""


class Point(tuple):
    __slots__ = [] # Restricts you not to add any new properties

    def __new__(cls, x, y, k):
        return tuple.__new__(cls, (copy.deepcopy(x), copy.deepcopy(y), copy.deepcopy(k)))

    x = property(copy.deepcopy(itemgetter(0)))
    y = property(copy.deepcopy(itemgetter(1)))
    z = property(copy.deepcopy(itemgetter(2)))


print(property(itemgetter((5,21))))

li = [1]
p = Point(2, 3, li)
print(p.x)
# p.x = 20
# 2
print(p.z)
li[0] = 30
print(p.z) # Didn't Change



