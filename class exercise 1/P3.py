#Write a program that will ask to enter the last and first names, the hours, 
#with pay for two people, then get the output. Finally, get the average pay of 
#the two people

first1 = input("First Employee's First name: ")
last1 = input("First Employee's Last name: ")
hours1 = float(input("First Employee's Hours Worked: "))
payrate1 = float(input("Enter pay rate for first employee: "))

first2 = input("Second Employee's First name: ")
last2 = input("Second Employee's Last name: ")
hours2 = float(input("Second Employee's Hours Worked: "))
payrate2 = float(input("Enter pay rate for second employee: "))

employee1 = first1 + ', ' + last1
employee2 = first2 + ', ' + last2

totalpay1 = (hours1 * payrate1)
totalpay2 = (hours2 * payrate2)

avgpay = (totalpay1 + totalpay2) / 2

print('\tData:' + '\n' + employee1 + ' ' + 'worked ' + str(hours1) +
    ' at a pay rate of ${:.2f}'.format(payrate1) + '\n' + employee2 + ' ' +
    'worked ' + str(hours2) + ' at a pay rate of ${:,.2f}'.format(payrate2))
print('The average pay of ' + employee1 + ' and ' + employee2 + ' is: {:,.2f}'.format(avgpay))