
filename = "coffee.txt"

with open(filename, mode='r') as file:# r= read
    lines = file.readlines() #read each lines until EOF = End of File
        #just a variable could be named jason
    for line in lines: #passsing the text file to the line for loop variable
        description, ProdNum, price = line.strip().split(',')
        print(f"{description},{ProdNum},${price}")

        #point to the description and
        #extract the word Bolivian
        if "21-003" in ProdNum: 
            print(f"{description},{ProdNum},${price}")


