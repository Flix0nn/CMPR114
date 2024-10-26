#assesment value is 60% of propertys actual value
#ex. 10,000 assesment value is 6,000
#Property tax is 72c for each 100 of assmsnt val
#tax for acre at $6000 will be 43.20
actual_value = float(input("Enter actual value of property: "))
assesment_value = actual_value * 0.6
tax = assesment_value * .72
finaltax = tax * 0.01
print(f'\nProperty value: {actual_value}')
print(f'Assesment Value: {assesment_value}')
print(f'Tax: {finaltax:,.2f}')