import Vehicles

def main():

    user_car = Vehicles.Automobiles('Audi','a4','4-doors',100,40000)
    user_car1 = Vehicles.Automobiles('Nissan','gtr','2-doors',100,120000)

    print('Make: ', user_car.get_make())
    print('Model: ', user_car.get_model())
    print('Doors: ', user_car.get_doors())
    print('Mileage: ', user_car.get_mileage())
    print('Price $: ', user_car.get_price())

    print()

    print('Make: ', user_car1.get_make())
    print('Model: ', user_car1.get_model())
    print('Doors: ', user_car1.get_doors())
    print('Mileage: ', user_car1.get_mileage())
    print('Price $: ', user_car1.get_price())

main()
