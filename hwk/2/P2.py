classA = 20
classB = 15
classC = 10
def tickets():
    ticketsA = int(input("Enter amount of tickets sold for Class A: "))
    ticketsB = int(input("Enter amount of tickets sold for Class B: "))
    ticketsC = int(input("Enter amount of tickets sold for Class C: "))
    soldA = ticketsA * classA
    soldB = ticketsB * classB
    soldC = ticketsC * classC
    total = soldA + soldB + soldC
    print(f"Amount of income generated from ticket sales: ${total} ")

tickets()