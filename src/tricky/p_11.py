
x = 10
y = 20


def get_sum(x = 1, y= 2):
    # global x
    x = 20
    print(x)
    return x + y


get_sum(30, 30)
print(x, y)
