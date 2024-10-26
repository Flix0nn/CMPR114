
class Automobiles:

    #accesor method
    #

    def __init__(self, make, model, doors, mileage, price):

        self.make = make
        self.model = model
        self.doors = doors
        self.mileage = mileage
        self.price = price

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_doors(self, doors):
        self.doors = doors

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_price(self, price):
        self.price = price

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_doors(self):
        return self.doors

    def get_mileage(self):
        return self.mileage

    def get_price(self):
        return self.price
        