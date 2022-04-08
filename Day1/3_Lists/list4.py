# File containing lines of the form "name,shares,price"
filename = 'portfolio.csv'

portfolio = []
with open(filename) as file:
    for line in file:
        row = line.split(',')
        # print(row)
        name = row[0]
        shares = int(row[1])
        price = float(row[2])
        holding = (name, shares, price)
        portfolio.append(holding)
    

print(portfolio)

#Do the normal method of calculating the total value of the portfolio
#price[]
total = 0
for _, shares, price  in portfolio:
    total += shares * price

print(f'Total cost of portfolio: {total}')
         


