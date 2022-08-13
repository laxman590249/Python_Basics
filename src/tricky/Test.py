test_cases = int(input())
for test in range(test_cases):
    line = str(input()).split()
    n = int(line[0])
    k = int(line[1])
    p = int(line[2])
    list_1 = list(range(1, n+1))

    line_2 = str(input()).split()
    for i in line_2:
        list_1.remove(int(i))

    if p <= len(list_1):
        print(list_1[p-1])
    else:
        print(-1)
