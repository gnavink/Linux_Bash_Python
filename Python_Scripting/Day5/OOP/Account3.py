from Account1 import Account

class AccountPortfolio:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def total_funds(self):
        return sum(account.inquiry() for account in self.accounts)

    def __len__(self):
        return len(self.accounts)

    def __getitem__(self, index):
        return self.accounts[index]

    def __iter__(self):
        return iter(self.accounts)


class MyAccount(Account):
    def panic(self):
        self.withdraw(self.balance)

if __name__ == '__main__':
    
    
    # # Example
    port = AccountPortfolio()
    port.add_account(Account('Navin', 1000.0))
    port.add_account(Account('Nikhil', 50.0))

    print(port.total_funds())    # -> 1050.0
    print(len(port))                    # -> 2

    # Print the accounts
    for account in port:
        print(account)

    # Access an individual account by index
    print(port[1].inquiry())            # -> 50.0

    # #Iterate the AccountPortfolio using iter()
    port_iter = iter(port)
    for account in port_iter:
        print(account)

    print()
    print()

    #EvilAccount example of panic method added
    a = MyAccount('Guido', 1000.0)
    a.withdraw(23.0)         # a.balance = 977.0
    a.panic()                # a.balance = 0
    print(a.balance)

