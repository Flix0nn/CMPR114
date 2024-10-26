def inputs():
    fn = input("\nenter your full name: ")
    midterm_grade = int(input("enter your grade for the midterm: "))
    finalexam_grade = int(input("enter your grade for the final exam: "))
    print('\n')

    grade(fn, midterm_grade, finalexam_grade)

def grade(full, mg, fg):
    if mg >= 90 and mg <= 100:
        grade1 = "A"
    elif mg >= 80 and mg <=89:
        grade1 = "B"
    elif mg >= 70 and mg <=79:
        grade1 = "C"
    elif mg >= 60 and mg <=69:
        grade1 = "D"
    elif mg < 60:
        grade1 = "F"
    else:
        print('Error number not entered')

    if fg >= 90 and fg <= 100:
        grade2 = "A"
    elif fg >= 80 and fg <=89:
        grade2 = "B"
    elif fg >= 70 and fg <=79:
        grade2 = "C"
    elif fg >= 60 and fg <=69:
        grade2 = "D"
    elif fg < 60:
        grade2 = "F"
    else:
        print('Error number not entered')

    sum = mg + fg
    avg = sum/200

    write(full, grade1, grade2, avg)

def write(one, two, three, four):
    try:
        openFile = open('Grades.txt','a')

        openFile.write(f'Full name: {one}\n')
        openFile.write(f'Midterm Grade: {two}\n')
        openFile.write(f'Final Exam Grade: {three}\n')
        openFile.write(f'Average Grade: {four}\n\n')
    
        openFile = open('Grades.txt','r')

        fileContents = openFile.read()
        print(fileContents)
        openFile.close()
    except:
        print('ERROR: Failed to write or read from file.')

inputs()