

l1 = ['a1', 'a2', 'a3']
l2 = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(l1, l2)):
    if i == 2:
        # print(i, a, b)
        pass


l = zip([1, 2, 3], [1, 2, 3], [1, 2, 3, 4])

for i in l:
    print(i)
