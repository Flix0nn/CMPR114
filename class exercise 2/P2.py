foodcost = float(input('Enter charge of food: '))
tip = foodcost * 0.18
tax = foodcost * 0.07

total = foodcost + tip + tax

print('Cost: ' + str(foodcost))
print('Tip: ' + str(tip))
print('Tax: ' + str(round(tax,1)))
print('The total is: $' + str(total))