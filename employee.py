

class Employee :
    def __init__(self,hourly, weekhours, position, name) :
        self.hourly = hourly
        self.position = position
        self.weekhours = weekhours
        self.name = name
    

    def salary(self) :
        return (self.hourly * self.weekhours) * 52

    def __str__(self) :
        print(f'==employee info==')
        print(f'name: {self.name}')
        print(f'position: {self.position}')
        print(f'hourly wage: {self.hourly}')
        print(f'hours per week: {self.weekhours}')
        print(f'\nyearly salary : {self.salary()}')

        return " "

    def changename(self,name) :
        self.name = name

    def changejob(self,position) :
        self.position = position

    def changehourly(self,hourly) :
        self.hourly = hourly
    
    def changeweekhours(self,weekhours) :
        self.weekhours = weekhours