#global variable: is where you can see the variable
#anywhere on your program

number = 0

def main():
    global number#global means the number variable can be called anywhere
                 #on the program
    number = int(input('enter a number'))

    show_number()

def show_number():
    print(f'the num is {number}')

main()

#challenge exc 4 have the user avility to type in three numbers
#starting with num1, num2, and the global number variables
def add():
    num1 = int(input('enter number 1: '))
    num2 = int(input('enter number 2: '))
    number = int(input('enter the global number: '))
    total = num1 + num2 + number

    print(total)
    return total
    
add()#calling the add function here
