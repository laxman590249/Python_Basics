
even = range(0,10,2)
odd = range(1,10,2)

for o in odd:
    print(o)

for e in even:
    print(e)

print(range(0, 5, 2) == range(0, 6, 2))

print(range(0, 100)[::-2] == range(99, 0, -2))

for i in range(0, 100, -2):
    print('Nothing will print, because negative slice and order is ascending')
    print(i)



