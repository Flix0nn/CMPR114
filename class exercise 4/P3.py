
counter = 0
display = 0
while counter <= 30:
    if (counter % 5 == 0 and counter >= 10):
        display = counter * 4.2
        print("Calories burnned after " + str(counter) + " minutes: " + str(display))
    counter += 1
