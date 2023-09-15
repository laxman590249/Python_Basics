import sys
import gc
a = 10000
print(sys.getrefcount(a))
print(gc.get_count())
del a
collected = gc.collect()


print("Garbage collector: collected %d objects." % (collected))

class MyClass:
    pass
obj = MyClass()
obj.value = obj
print(sys.getrefcount(obj))
print(gc.get_count())
del obj
collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))
print(gc.get_count())
