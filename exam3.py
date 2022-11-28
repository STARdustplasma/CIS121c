## 1
class Vehicle :
    def __init__(self, numPassengers, manufacturer, numWheels) :
        self.numPassengers = numPassengers
        self.manufacturer = manufacturer
        self.numWheels = numWheels
    
class Automobile(Vehicle) :
    def __init__(self, numPassengers, manufacturer, numWheels, mpg, model, numDoors):
        super().__init__(numPassengers, manufacturer, numWheels)
        self.mpg = mpg
        self.model = model
        self.numDoors = numDoors 

class TwoWheeler(Vehicle) : 
    def __init__(self, numPassengers, manufacturer, numWheels, model, weight):
        super().__init__(numPassengers, manufacturer, numWheels)
        self.model = model
        self.weight = weight 

class Sedan(Automobile) :
    def __init__(self, numPassengers, manufacturer, numWheels, mpg, model, numDoors, type, numCylinders, horsepower):
        super().__init__(numPassengers, manufacturer, numWheels, mpg, model, numDoors)
        self.type = type
        self.numCylinders = numCylinders
        self.horsepower = horsepower

class Truck(Automobile) :
    def __init__(self, numPassengers, manufacturer, numWheels, mpg, model, numDoors, type, numAxels, maxTowPayload):
        super().__init__(numPassengers, manufacturer, numWheels, mpg, model, numDoors)
        self.type = type
        self.numAxels = numAxels
        self.maxTowPayload = maxTowPayload

class Motorcycle(TwoWheeler) :
    def __init__(self, numPassengers, manufacturer, numWheels, model, weight, type, mpg, horsepower):
        super().__init__(numPassengers, manufacturer, numWheels, model, weight)
        self.type = type
        self.mpg = mpg
        self.horsepower = horsepower

class Bicycle(TwoWheeler) :
    def __init__(self, numPassengers, manufacturer, numWheels, model, weight, hasGears, hasSuspensions, wheelSize):
        super().__init__(numPassengers, manufacturer, numWheels, model, weight)
        self.hasGears = hasGears
        self.hasSuspensions = hasSuspensions
        self.wheelSize = wheelSize


## 2
## Truck and Sedan are child classes of Automobile and Motorcycle and Bicycle are child classes of TwoWheeler.
## Automobile and TwoWheeler are child classes of Vehicle.
## Vehicle, Automobile, and TwoWheeler are parent classes.
## There are a total of 6 child classes and 3 parent classes.
## The goal of the uml diagram seems to be to create classes that take into account the details of various vehicles.
## None of the classes appear to have methods.


## 3
class Customer :
    def __init__(self, customerName) : ## general class creating in order to create all the variables
        self.name = customerName ## just a name to put down
        self.progress = 0 ## keeps track of how close customer is to discount
        self.purchases = 0 ## keeps track of total purchases independent from progress to discount
        self.status = False ## will tell the class when to apply discount
        self.disCOUNT = 0 ## counting the number of discounts given

    def makePurchase(self, amount) :
        self.progress += amount ## adds to progress
        
        if self.status == True : ## adds discount if status is true
            self.purchases += (amount-10)
            print(f'You got a discounted purchase of {amount - 10}')
            self.status = False
        else : ## doesnt if not
            self.purchases += amount
            print(f'You made a purchase of {amount}')
        
        print(f'You have spent a total of {self.purchases}')
        

    def discountReached(self) :
        print('checking...') ## auditing
        if self.progress < 100 : ## tells the customer how close they are to discount
            print(f'Currently at {self.progress}')
            print(f'Spend {100-self.progress} to get discount')
        else :## changes status to true so they will get the discount next time
            print(f'Claimed discount!') 
            self.status = True 
            self.progress = 0
            self.disCOUNT += 1

    def loyalty(self) :
        print(f'Number of discounts: {self.disCOUNT}')