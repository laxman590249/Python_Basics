print(dir())

import turtle
import csv

# Returning the names of Local Modules
print(dir())

# Returning attributes of __builtin__ module.
print(dir(__builtins__))

class MyClass:
    def __dir__(self):
        return ['Mango', 'Orange']

object_class = MyClass()

print(dir(object_class))

print(globals())

