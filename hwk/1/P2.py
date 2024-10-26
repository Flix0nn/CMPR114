one = int(input("Price of item 1: "))
two = int(input("Price of item 2: "))
three = int(input("Price of item 3: "))
four = int(input("Price of item 4: "))
five = int(input("Price of item 5: "))

subtotal = one + two + three + four + five
tax = subtotal * 0.07
roundedtax = round(tax, 1)
total = subtotal + roundedtax
print('\n' + 'Subtotal: ' + str(subtotal) + '\n' 
    + 'Tax: ' + str(roundedtax) + '\n' 
    + 'Total: ' + str(total))
    