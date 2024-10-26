
class AnimalType:
    def eats(self):
        print("these animals (rabbit, birds, cat) likes to eat ?")

class rabbits():
    def munch(self):
        print("Carrots")
    
class birds(rabbits):
    def munch1(self):
        print('Seeds')

class cat(birds):
    def munch2(self):
        print('fish')

AnimalObject = AnimalType()
AnimalObject.eats()

RabbitObject = rabbits()
RabbitObject.munch()

BirdObject = birds()

BirdObject.munch1()

CatObject = cat()
CatObject.munch2()