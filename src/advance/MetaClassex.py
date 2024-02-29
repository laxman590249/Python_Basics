"""
In Python, a metaclass is a class that defines the behavior of other classes.
It is often referred to as the "class of a class".

In Python, all classes are instances of a metaclass. By default, this metaclass is the type metaclass

Metaclasses can be used to achieve various objectives, such as:

1. Modifying class attributes or behavior: You can define a metaclass to automatically add or modify attributes or
methods of classes that are created using that metaclass.

2. Enforcing constraints or validations: Metaclasses can be used to enforce certain constraints or validations on the
definition of classes. This could include checks on attribute names, restrictions on inheritance, or other criteria.

3. Implementing class-level operations: Metaclasses can define class-level operations that are applied when classes are
created, such as registering classes in a registry, performing initialization logic, or modifying the class hierarchy.

"""


class A():
    pass


class MyMeta(type):
    pass


class MyClass(metaclass=MyMeta):
    pass


class MySubclass(MyClass):
    pass


print(type(A))
print(type(MyMeta))
print(type(MyClass))
print(type(MySubclass))

# Anotehr way
class MyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Modify attributes of the class being created
        attrs["custom_attribute"] = "Custom Value"

        # Create the class using the modified attributes
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMetaclass):
    pass

print(MyClass.custom_attribute)
m = MyClass()
print(type(MyClass))
# Output: "Custom Value"
