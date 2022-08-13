# Global Name Space object Creation
var_1 = 20



def test():
    # Overriding Build in Object in local name space, it will be reflected into local also
    sum = 30
    print(var_1)

print(sum([1, 2, 3]))
test()
print(var_1)