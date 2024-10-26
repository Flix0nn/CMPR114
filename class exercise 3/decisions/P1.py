def get_grade(score):

    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

score = float(input("Enter the score: "))

if score >=0 and score <=100:
    grade = get_grade(score)
    print("Grade: ", grade)

elif score>=80 and score<=89:
    grade = get_grade(score)
    print("Grade: ", grade)

elif score>=70 and score<=79:
    grade = get_grade(score)
    print("Grade: ", grade)

elif score>=60 and score<=69:
    grade = get_grade(score)
    print("Grade: ", grade)

elif score < 60:
    grade = get_grade(score)
    print("Grade: ", grade)

else:
    print("invalid score, Score must be between 0 - 100")
