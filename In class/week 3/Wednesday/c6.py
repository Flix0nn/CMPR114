def main():

    names = ['Jason','Joe','Jane']

    print('list of names ')
    print(names)

    NameRemove = input ('enter a name: ')

    names.insert(0,"Mike")
    names.insert(1,"Dell")
    names.remove(NameRemove)
    names.remove('Mike')

    print('list of names after')

    print(names)

#main()

def total():

    numbers = [1,2,3,4,5]

    sum = 0
    #challenge Exc #3 output the sum and average to an external file
    for value in numbers:
        sum+=value

    average = sum / len(numbers)
    print('sum ', sum, "\navg " , average)

    openFile = open('sum_avg.txt','w')

    openFile.write(f'{sum}, {average}\n')

    openFile.close()
    
total()