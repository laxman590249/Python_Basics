# Global Name Space object Creation
var_1 = 20
# Overriding Build in Object, it will be refelected into local also
sum = 30

def test():
    sum([10, 20, 30])
    print(var_1)

test()
print(var_1)