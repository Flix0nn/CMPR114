weight = float(input("\nEnter weight of package: "))

def shipprice(weight):
    if weight <= 2:
        price = 1.50
    elif weight >= 2 and weight <= 6:
        price = 3.00
    elif weight >= 6 and weight <= 10:
        price = 4.00
    elif weight >= 10:
        price = 4.75
    else:
        return

    return f"\nWeight: {weight}, Price: {price}\n"

result = shipprice(weight)
print(result)
