

class Car :
    def __init__(self,number_of_wheels, engine, model, year) :
        self.number_of_wheels = number_of_wheels
        self.engine = engine
        self.model = model
        self.year = year


    def __str__(self) :
        print(f'car info')
        print(f'model: {self.model}' )
        print(f'engine: {self.engine}' )
        print(f'year: {self.year}' )
        print(f'number of wheels: {self.number_of_wheels}' )

        return ' '

    def changeyear(self,newyear) :
        self.year = newyear

    def changeengine(self,newengine) :
        self.engine = newengine

