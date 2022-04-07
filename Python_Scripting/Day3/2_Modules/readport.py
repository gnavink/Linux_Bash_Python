# readport.py
#
# Reads a file of 'NAME,SHARES,PRICE' data



def read_portfolio(filename):
    portfolio = []
    with open(filename) as file:
        for line in file:
            row = line.split(',') #['TATAMOTORS', '500', '294' ]
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            holding = (name, shares, price)
            portfolio.append(holding)
            
    return portfolio

if __name__ == '__main__':
    filename = '../../data/portfolio.csv'  #'portfolio.csv'  #portfolio_bad.csv
    portfolio = read_portfolio(filename)
    print(portfolio)

