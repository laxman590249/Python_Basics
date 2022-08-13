

class MyAide():
    def run(self):
        print('My Aide')


class Jupyter():
    def run(self):
        print("Running")

class Laptop():
    def code(self, ide):
        ide.run()

ide = MyAide()

laptop = Laptop()

laptop.code(ide)