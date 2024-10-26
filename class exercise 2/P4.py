numberofshares = 2000
pricepershare = 40.00
brokercommsionrate = 0.03 #3%
sellingpricepershare = 42.75

totalpurchasecost = numberofshares * pricepershare

commision2broker = totalpurchasecost * brokercommsionrate

totalsalesrevenue = numberofshares * sellingpricepershare

profit = totalsalesrevenue - totalpurchasecost - commision2broker

print('\n' + 'the amount Joe paid for the stock is $ ' + str(totalpurchasecost) + '\n' 
    + 'the amount of money Joe paid the broker is $ ' + str(commision2broker)
    + '\n' + 'joe profited $ ' + str(profit) + '\n' + 'Press any key to continue . . .' + '\n')