class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = '0.15'
        else:
            self.tax = '0.12'

    def display_all(self):
        print 'price: ' + self.price
        print 'speed: ' + self.speed
        print 'fuel: ' + self.fuel
        print 'mileage: ' + self.mileage
        print 'tax: ' + self.tax
        print '\n'

car1 = Car("$120000","80 mph", "1 gallon", "35 in city")

car1.display_all()
