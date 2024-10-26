while True:
    fn = input("enter last and first name: ")

    i = 0
    scores = []
    while i < 3:
        score = float(input("Enter scores: "))
        scores.append(score)
        i += 1

    total = sum(scores)
    avg = total/len(scores)
    
    if avg > 100:
        print("ERROR")
    else:
        break

if avg <= 100 and avg >= 90:
    letter = "A"
    print(f"Grade: {letter}")
elif avg <= 89 and avg >= 80:
    letter = "B"
    print(f"Grade: {letter}")
elif avg <= 79 and avg >= 70:
    letter = "C"
    print(f"Grade: {letter}")
elif avg <= 69 and avg >= 60:
    letter = "D"
    print(f"Grade: {letter}")
else:
    letter = "F"
    print(f"Grade: {letter}")