import random
from Account1 import Account

class EvilAccount(Account):
    def __init__(self, owner, balance, factor):
        super().__init__(owner, balance)
        self.factor = factor

    def inquiry(self):
        if random.randint(0,4) == 1:
           return self.factor * super().inquiry()
        else:
           return super().inquiry()

a = EvilAccount('Guido', 1000.0,1.10)
a.deposit(10.0)          # Calls Account.deposit(a, 10.0)
print(a.balance)
available = a.inquiry()  # Calls EvilAccount.inquiry(a)
print(available)