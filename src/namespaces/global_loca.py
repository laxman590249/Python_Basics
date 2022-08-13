# Global Name Space object Creation
var_1 = 20

def test():
    # Local Name Space object Creation
    var_1 = 30
    print(var_1)

test()
print(var_1)