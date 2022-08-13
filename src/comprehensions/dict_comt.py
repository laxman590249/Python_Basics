

list_1 = [1, 2, 3, 4, 5]

d = {x : x **2 for x in list_1}

k = {x: y for x, y in d.items()}


print(d)

print(k)