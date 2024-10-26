
with open('numbers.txt', 'r') as file:
    lines = file.readlines()

numbers = []

for line in lines:
    number = int(line)
    numbers.append(number)

total_sum = sum (numbers)
average = total_sum / len(numbers)

print("#'s: ", numbers)
print("sum: ", total_sum)
print("average: ", average)

with open ("output.txt",'w') as file1:
    for number in numbers:
        file1.write(str(number) + '\n')

print('nums written to output file')

