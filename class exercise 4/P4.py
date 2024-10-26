
laps = int(input("how many laps did you run? "))
total = 0
times = []

for i in range(laps):
    laptimes = float(input("how many second did lap " + str(i +1) + " take? "))
    times.append(laptimes)
    total += laptimes

times.sort()
print(f"\nThe fastest lap was lap {times[0]} seconds.")
print(f"The slowest lap was run in {times[-1]} seconds.")
print(f"The average lap time was {total / laps} seconds.")