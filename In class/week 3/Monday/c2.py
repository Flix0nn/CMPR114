def display_user_info(name, hobbies):
    print(f"name: {name}")
    print(f"hobbies: {hobbies}")

    for hobby in hobbies:
        print(f" - {hobby}")
        
        file_name = "hobbies.txt"
        
    with open (file_name, 'a') as file:
        file.write(f"Name: {name} \n")
        file.write(f"Your Hobbys are: {hobbies} \n")
    
        print(f"Data written to the {file_name} was transferred")

name = input('enter your name: ')

#list
hobbies=[] #array variable allows for one variable but may assign many
#hobbies []

print("Enter your hobbies line by line, type q to stop ")

while True:
    hobby = input('enter a hobby: ')
    if hobby.lower()=='q':
        break

    hobbies.append(hobby)

display_user_info(name, hobbies)#calling the function name




