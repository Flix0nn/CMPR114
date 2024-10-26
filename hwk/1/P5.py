def findquarter():
    while True:
        choosemonth = int(input('\nEnter month (1-12): '))
            
        if choosemonth < 1 or choosemonth > 12:
            print("Invalid month. Please enter a month between 1 and 12.")
            continue
        print(f"\nChosen month: {choosemonth} \n")
        
        if 1 <= choosemonth <= 3:
            print("The month is in the first quarter \n")
        elif 4<= choosemonth <= 6:
            print("The month is in the second quarter \n")
        elif 7 <= choosemonth <= 9:
            print("The month is in the third quarter \n")
        elif 10 <= choosemonth <= 12:
            print("The month is in the fourth quarter \n")
        break

findquarter()