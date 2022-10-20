import math


class Circle :
    def __init__(self, radius) :
        self.radius = radius
    
    def area(self) :
        return round(math.pi * self.radius ** 2, 2)
    
    def perimeter(self) :
        return round(2 * math.pi * self.radius, 2)

    def __str__(self) :
        print('==info==')
        print(f'radius: {self.radius}')
        print(f'area: {self.area()}')
        print(f'radius: {self.perimeter()}')

        return " "