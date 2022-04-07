from Account1 import Account

class EvilAccount(Account):
     pass


if __name__ == '__main__':
    a = EvilAccount('Eva', 10.0)
    print(a)             # Account('Eva', 10.0)     # Notice misleading output
    print( type(a) )      # class 'EvilAccount'