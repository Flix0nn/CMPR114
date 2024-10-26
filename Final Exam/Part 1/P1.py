students = []

while True:
    fn = input("Enter last and first name: ")

    scores = []

    for _ in range(3):
        score = float(input("Enter score: "))
        scores.append(score)

    total = sum(scores)
    avg = total / len(scores)
    roundavg = round(avg, 2)

    student_data = (fn, scores, total, roundavg)
    students.append(student_data)

    print(f"{fn} Total: {total} Average: {roundavg}")

    with open("Final Exam/scores.txt", "a") as file:
        file.write(f"{fn} Total: {total} Average: {roundavg}\n")

    again = input("Do you want to enter another student's data? (Y/N): ")
    if again.upper() != "Y":
        break
    else:
        print()

print("\nFinal list of students and their scores:")
for student in students:
    name, scores, total, average = student
    print(f"Name: {name}, Scores: {scores}, Total: {total}, Average: {average:.2f}")
