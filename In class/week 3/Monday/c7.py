CONTRIBUTION_RATE = 0.05 #global constant

def main():
    gross_pay = float(input('enter the gross pay: '))
    bonus = float(input('enter the bonus: '))

    show_pay_contrib(gross_pay, bonus)
    show_take_home_pay(bonus, gross_pay)

def show_pay_contrib(gross, bonus):
    contrib = gross * CONTRIBUTION_RATE
    contrib = bonus * CONTRIBUTION_RATE

    print(f'contribution for gross pay: ${contrib:,.2f}.')
    print(f'contribution for bonus pay: ${contrib:,.2f}.')

#challenge exc #5, take the bonus pay, and
#calculate or add to the gross pay
def show_take_home_pay(num1, num2): 
    contrib = num1 + num2

    print(f'contribution for take home pay: ${contrib:,.2f}.')

main()