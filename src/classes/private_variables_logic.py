


class Account:

    def __init__(self, balance ,name):
        self.__balance = balance
        self.__name = name
        self.__height__ = 30

    def deposit(self, amount):
        self.__age = 20
        self.__country = 'America'
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def show_balance(self):
        print(self.__balance)


if __name__ == '__main__':
    laxman = Account(700, 'Laxman')
    laxman.deposit(100)
    print('Printing All Attributes of Class :')
    laxman.__country = 'India'
    laxman.deposit(100)
    print(laxman.__dict__)
    laxman._Account__balance = 200
    print(laxman.show_balance())

