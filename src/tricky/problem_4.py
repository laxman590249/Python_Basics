

def method():
    print('Hello Method')

local = method

del method

# method()
local()