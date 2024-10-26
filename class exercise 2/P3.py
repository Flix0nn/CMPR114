males = int(input('Enter amount of males in the class: '))
females = int(input('Enter amount of females in the class: '))

totalstudents = males + females
maledecimal = males / totalstudents
femaledecimal = females / totalstudents
malepercentage = maledecimal * 100
femalepercentage = femaledecimal * 100
print('\tMale %' + str(malepercentage) + '\n' + '\tFemale %' + str(femalepercentage))