
import random
from Account1 import Account

# No super()
# class EvilAccount(Account):
#     def inquiry(self):
#         if random.randint(0,4) == 1:
#            return self.balance * 1.10
#         else:
#            return self.balance

#With super()
class EvilAccount(Account):
    def inquiry(self):
        if random.randint(0,4) == 1:
           return 1.10 * super().inquiry()
        else:
           return super().inquiry()

a = EvilAccount('Guido', 1000.0)
a.deposit(10.0)          # Calls Account.deposit(a, 10.0)
print(a.balance)
available = a.inquiry()  # Calls EvilAccount.inquiry(a)
print(available)