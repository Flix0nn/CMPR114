
#list is vavarible that can assign multiple values
#array variable

numbers = [1,2]
#indexes   0,1, etc
print(numbers[0])

sum_of_numbers = 0

for number in numbers:
    sum_of_numbers += number
    print (number)

print('the sum of the numbs are ', sum_of_numbers)

#project 2
numbers1 = [] #list that is empty

while True:
    EnterNumber = int(input('enter a number (or 0 to stop)'))
    if EnterNumber == 0:
        break #exit the while loop
    numbers1.append(EnterNumber) #appends the number from the input

index = 0
sum = 0 #define or declare the sum varible
while index < len(numbers1):#while the index is less than the length of
                            #list
    sum += numbers1[index] #add the numbers from the list
                            #init the sum var
    index +=1 #increment by 1

print('the total of the nums are ' , sum)




