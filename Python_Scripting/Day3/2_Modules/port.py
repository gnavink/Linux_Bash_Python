# port.py


import readport
#import readport as rp
#from readport import *

filename = '../../data/portfolio.csv'
my_portfolio = readport.read_portfolio('../../data/portfolio.csv')
#my_portfolio = rp.read_portfolio(filename)
#my_portfolio = read_portfolio(filename)

total = 0
for name, shares, price in my_portfolio:   # for _, shares, price in my_portfolio:
    total += shares * price

print(total)


