from collections import OrderedDict


d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'a': 1}

od1 = OrderedDict()
od2 = OrderedDict()

od1['a'] = 1
od1['b'] = 2

od2['b'] = 2
od2['a'] = 1

print(d1 == d2)
print(od1 == od2)
