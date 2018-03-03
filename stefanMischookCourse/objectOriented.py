class Car():
    ''' a simple class that describes a car '''

    def __init__(self, model, cost):
        self.model = model
        self.cost = cost

    def start (self):
        '''starts the car'''
        print (self.model.title() + " is now starting")

myCar = Car("audi","$98k")
myCar.start()

my2ndCar = Car("nissan","40k")
my2ndCar.start()

