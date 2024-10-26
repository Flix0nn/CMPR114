firstname = input("First Name: ")
lastname = input("Last Name: ")
address = input("Address: ")
city = input("City: ")
state = input("State: ")
zipcode = int(input("Zipcode: "))
phonenumber = int(input("Phone Number: "))
major = input('College Major: ')

print ('\tData:\n' + firstname + ',' + lastname + 
    '\n' + address + '' + city + ' ' + 
    state + ' ' + str(zipcode) + '\n' + 
    str(phonenumber) + '\n' + major)