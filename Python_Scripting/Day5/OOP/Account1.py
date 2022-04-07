class Account:
    '''
    A simple bank account
    
    owner: str
    balance: float
    '''

    def __init__(self, owner:str, balance:float):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        # return f'Account({self.owner!r}, {self.balance!r})'
        return f'{type(self).__name__}({self.owner!r}, {self.balance!r})' #Class variable set 

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def inquiry(self):
        return self.balance

if __name__ == "__main__":
    a = Account('Navin', 1000.0,)
    b = Account('Nikhil', 10.0)
    print(vars(a))

