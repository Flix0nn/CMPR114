def write_to_file(name, age, address):#parameters

    file_name = "output.txt"

    with open (file_name, 'a') as file:
        file.write(f"Name: {name} \n")
        file.write(f"Age: {age} \n")
        file.write(f"Address: {address} \n")

        print(f"Data written to the {file_name} was transferred")

def get_user_input():
    name = input("Enter the name: (or type q to stop) ")
    if name.lower()=='q': #allows for case sensitivity
        return None, None, None #dont return anything
    print("BYE")

    age = input("Enter the age: ")
    
    address = input('Enter the address: ')
    return name, age, address

while True:#loop through lines 24-34
    name, age, address = get_user_input()
    if name is None or age is None or address is None:
        break #breaks the while loop

    #strip function allows for no white spaces or tabs
    if name.strip() and age.strip() and address.strip():
        write_to_file(name, age, address)#calling the function to write to
    
    #a text file
    else:
        print("name and age cannont be blank, did not record")
