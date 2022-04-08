class Account:
    num_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        Account.num_accounts += 1

    def __repr__(self):
        return f'{type(self).__name__}({self.owner!r}, {self.balance!r})'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.deposit(-amount)    # Must use self.deposit()

    def inquiry(self):
        return self.balance

if __name__ == '__main__':
    a = Account('Guido', 1000.0)
    b = Account('Eva', 10.0)
    print(Account.num_accounts)
    c = Account('Ben', 50.0)
    print(c.num_accounts)