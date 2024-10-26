def main():
    first_name = input('enter the first name: ')
    last_name = input('enter the last name: ')
    address = input('enter the address: ')
    city = input('enter the city name: ')
    state = input('enter the state : ')
    zipcode = int(input('enter the zipcode: '))

    print ('your name reversed is ')

    reverse_name (first_name, last_name)
    other_info (address, zipcode, city, state)

def reverse_name(first, last):
    print(last, first)


    #challenge exc 2, allow the user to input
    #the address, city, state, with zipcode

def other_info(address, zipcode, city, state):
    print(f'{address}, {city}, {state}, {zipcode}')
main()