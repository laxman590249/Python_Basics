"""
The Builder design pattern in Python is a creational design pattern that allows you to construct complex
objects step by step. It separates the construction of an object from its representation,
allowing different representations to be created using the same construction process.
The main idea is to abstract the construction of an object and provide a fluent interface for setting its properties.

"""

class Product:
    def __init__(self, part1, part2):
        self.part1 = part1
        self.part2 = part2

class ProductBuilder:
    def __init__(self):
        self.part1 = None
        self.part2 = None

    def build_part1(self, value):
        self.part1 = value
        return self

    def build_part2(self, value):
        self.part2 = value
        return self

    def get_product(self):
        return Product(self.part1, self.part2)

# Usage example
builder = ProductBuilder()
product = builder.build_part1("Part 1").build_part2("Part 2").get_product()
print(product.part2, builder.part1)