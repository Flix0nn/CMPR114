#state sales tax rate is 5%
#county sales tax rate is 2.5%
sales = float(input("Enter total sales for the month: "))
def calculations():
    countytax = sales * 0.025
    statetax = sales * 0.05
    total = countytax + statetax
    print(f'\nCounty sales tax: {countytax:,.2f}')
    print(f'State sales tax: {statetax:,.2f}')
    print(f'Total sales tax: {total:,.2f}')

calculations()
