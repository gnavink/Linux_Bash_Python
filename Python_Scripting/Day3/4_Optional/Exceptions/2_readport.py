# readport.py
#
# Reads a file of 'NAME,SHARES,PRICE' data

filename = 'portfolio_bad.csv'  #'portfolio.csv'  #portfolio_bad.csv

def read_portfolio(filename):
    portfolio = []
    with open(filename) as file:
        for line in file:
            row = line.split(',') #['TATAMOTORS', '500', '294' ]
            try:
                name = row[0]
                shares = int(row[1])
                price = float(row[2])
                holding = (name, shares, price)
                portfolio.append(holding)
            except ValueError as err:
                print('Bad row:', row)
                print('Reason:', err)
    return portfolio

portfolio = read_portfolio(filename)
print(portfolio)

