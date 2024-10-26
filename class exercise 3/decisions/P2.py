def roulet(number):
    if number < 0 and number > 36:
        return "Error: number must be between 0 - 36"
    elif number >= 1 and number <= 10:
        if number % 2 == 0:
            color = "Black"
        else:
            color = "Red"
    elif number >= 11 and number <= 18:
        if number % 2 == 0:
            color = "Red"
        else:
            color = "Black"
    elif number >= 19 and number <= 28:
        if number % 2 == 0:
            color = "Black"
        else:
            color = "Red"
    elif number >= 29 and number <= 36:
        if number % 2 == 0:
            color = "Red"
        else:
            color = "Black"
    else:
        return "Error: Invalid number"

    return f"{color} {number}"

number = int(input("\nEnter a number 1 - 36: "))
result = roulet(number)
print(result)
