meal = int(input('Charge of meal: '))
tip = meal * 0.18
tax = meal * 0.07
total = meal + tip + tax

tipround = round(tip, 2)
taxround = round(tax, 2)
totalround = round(total, 2)

print('\n' + 'Meal: ' + str(meal) + '\n' +
 'Tip: ' + str(tipround) + '\n' + 'Tax: ' +
 str(taxround) + '\n' + 'Total: ' + 
 str(totalround))