def main():
    temps = []
    count = 0
    while count < 4:
        temp = float(input("Enter a temperature under 102.5: "))
        if temp >= 102.5:
            print("Temperature over 102.5 entered. Please try again.")
        else:
            temps.append(temp)
            count += 1

    total = sum(temps)
    average = total / 4

    print(f"\nThe sum of the temperatures is: {total}")
    print(f"The average temperature is: {average}")

main()
