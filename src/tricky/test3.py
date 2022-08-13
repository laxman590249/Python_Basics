#!/usr/bin/env python3
from dataclasses import dataclass

@dataclass(frozen=True)
class User:

    name: str
    occupation: str

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __eq__(self, other):

        return self.name == other.name \
            and self.occupation == other.occupation

    # def __hash__(self):
    #     return id(self)

    def __str__(self):
        return f'{self.name} {self.occupation}'


u1 = User('John Doe', 'gardener')
u2 = User('John Doe', 'gardener')

print(set([u1, u2]))

if (u1 == u2):
    print('same user')
    print(f'{u1} == {u2}')
else:
    print('different users')

# users = {u1, u2}
# print(len(users))



class A:
    pass


obj = A()
obje2 = A()
d = {
obj: 1
}
print()
print(d.get(obj))
# print(set([obj, { 'A': 1}]))

