import random

class Company :
    def __init__(self, name, year):
        self.name = str(name)
        self.year = int(year)

class Car :
    def __init__(self, wheels, company, color, miles, status, speed) :
        self.wheels = wheels
        self.company = company
        self.color = color
        self.miles = miles
        self.status = status
        self.speed = speed

    def updatemiles(self,amount) :
        self.miles += amount

    def accelerate(self, amount) :
        self.speed += amount
        self.status = 'accelerating'
        return self.updatemiles(amount)

    

    def stop(self) :
        self.speed = 0
        self.status = 'stopped'

    def decrease(self) :
        self.speed -= 20
        if self.speed <= 0 :
            self.speed = 0
            self.status = 'stopped'
        else :
            self.status = 'deccelerating'

company1 = Company('chevy', 1967)
company2 = Company('mitsubishi', 2008)
company3 = Company('toyota', 1995)
company4 = Company('suzuki', 1986)

car1 = Car(4, company1, 'black', 0, 'stopped', 0)
car2 = Car(4, company2, 'red', 0, 'stopped', 0)
car3 = Car(4, company3, 'white', 0, 'stopped', 0)
car4 = Car(4, company4, 'green', 0, 'stopped', 0)


def sixty(car, speed) :
    seconds = 0
    while car.speed < 60 :
        seconds +=1
        car.accelerate(random.randint(1,speed))
        print(f'car is moving at {car.speed} mph at {seconds} seconds')
    print(f'took {seconds} seconds to reach 60 mph')
    print(f'car has driven {car.miles} miles')

def hundred(car, speed) :
    seconds = 0
    while car.speed < 60 :
        seconds +=1
        car.accelerate(random.randint(1,speed))
        print(f'car is moving at {car.speed} mph at {seconds} seconds')
    print(f'took {seconds} seconds to reach 100 mph')
    print(f'car has driven {car.miles} miles')

def twofifty(car, speed) :
    seconds = 0
    while car.speed < 250 :
        seconds +=1
        car.accelerate(random.randint(1,speed))
        print(f'car is moving at {car.speed} mph at {seconds} seconds')
    print(f'took {seconds} seconds to reach 250 mph')
    print(f'car has driven {car.miles} miles')

sixty(car1, 25)
hundred(car2, 25)
twofifty(car3, 25)


## create 5 cars that check 0 to 60, 100, 250
## display the amount of miles ran