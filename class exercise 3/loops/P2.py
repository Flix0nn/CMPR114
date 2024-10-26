def sales():
    salecommission = []
    count = 0
    while count < 4:
        sale = float(input("enter the sales with commission: "))
            
        salecommission.append(sale)
        count += 1

    total = sum(salecommission)

    print(f"\nThe sum of the sales and commissions are: {total}")

sales()