
class Kettle(object):

    power_source = 'Electricity'

    def __new__(cls, *args, **kwargs):
        print('Called New')
        return super().__new__(Kettle)

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle('Kenwood', 99.09)
print(kenwood.make, kenwood.price, kenwood.on)

hamilton = Kettle('Hamilton', 100)

kenwood.switch_on()  # Calling by object name
Kettle.switch_on(hamilton)  # Calling by class Name and passing the object

print(kenwood.make, kenwood.price, kenwood.on)
print(hamilton.make, hamilton.price, hamilton.on)

print('-' * 80)

kenwood.power = 200
print(kenwood.power)

print('-' * 80)

print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)
# Printing attributes
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
print('-' * 80)


Kettle.power_source = 'Moon'
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)
# Printing attributes
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
print('-' * 80)

kenwood.power_source = 'Sun'
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)
# Printing attributes
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
print('-' * 80)

Kettle.power_source = 'Moon'
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.power_source)
# Printing attributes
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
