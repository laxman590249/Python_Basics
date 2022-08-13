from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass


class Triangle(Polygon):
    def sides(self):
        print('I have 3 Sides')


class Rectangle(Polygon):
    def sides(self):
        print('I have 4 Sides')

t = Triangle()
t.sides()

r = Rectangle()
r.sides()