
class Account:
    """ Its an Bank's account  """

    @staticmethod
    def _current_time(self):
        print('Hello Current')

    @staticmethod
    def current_time():
        print('Hello Time')

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            Account.current_time()
            Account._current_time(10)

    def withdraw(self, amount):
        if 0 > amount < self.balance:
            self.balance -= amount
        else:
            print('Amount is not valid...')

    def show_balance(self):
        print('Balance is ', self.balance)

    @staticmethod
    def test(kevin):
        kevin.show_balance()


if __name__ == '__main__':
    laxman = Account(0)
    laxman.deposit(1000)
    laxman.withdraw(10000)
    laxman.show_balance()
    laxman.test(laxman)




