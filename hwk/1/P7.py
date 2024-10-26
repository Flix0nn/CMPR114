from dis import dis

def calculatediscount():
    while True:
        retailprice = 99
        quantity = int(input("\nHow much of the product would you like to buy?: "))
        total = retailprice * quantity

        if quantity < 1:
            print("\nYou need to buy at least 1 of this item.")
            continue
        print(f'Amount bought: {quantity} \n')

        if 1 <= quantity <= 9:
            print("No discount applied \n" + f"Total: ${total} \n")
        elif 10<= quantity <= 19:
            total10 = total * 0.1
            print("10% discount applied \n" + "Total: $" + str(round(total10, 2)) + "\n")
        elif 20 <= quantity <= 49:
            total20 = total * 0.2
            print("20% discount applied \n" + f"Total: $" + str(round(total20, 2)) + "\n")
        elif 50 <= quantity <= 99:
            total30 = total * 0.3
            print("30% discount applied \n" + f"Total: $" + str(round(total30, 2)) + "\n")
        elif quantity > 100:
            total40 = total * 0.4
            print("40% discount applied \n" + f"Total: $" + str(round(total40, 2)) + "\n")
        break

calculatediscount()