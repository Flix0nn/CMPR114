sugar48 = 1.5
butter48 = 1
flour48 = 2.75

cpr = 48

amount = int(input('How many cookies do you want to make: '))

sugarneeded = (sugar48 / cpr) * amount
butterneeded = (butter48 / cpr) * amount
flourneeded = (flour48 / cpr) * amount

print('\tData:' + '\n'
 + 'amount of sugar: ' + str(round(sugarneeded, 2)) + '\n'
 + 'amount of butter: ' + str(round(butterneeded, 2)) + '\n'
 + 'amount of flour: ' + str(round(flourneeded, 2)) + '\n'
 + 'For ' + str(amount) + ' ' + 'cookies')
