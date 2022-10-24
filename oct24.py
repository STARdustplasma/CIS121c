from oct24a import Animal
from oct24b import cat

class dog(Animal) :
    def __init__ (self,name,color,eye,height,length,weight, Animal) :
        super().__init__(name)
        self.color = color
        self.eye = eye
        self.height = height
        self.length = length
        self.weight = weight

    def __str__(self) :
        print('==info==')
        print(f'name: {self.name}')
        print(f'color: {self.color}')
        print(f'eye color: {self.eye}')
        print(f'height: {self.height}')
        print(f'length: {self.length}')
        print(f'weight: {self.weight}')
        return ''

    def shake(self) :
        print(f'{self.name} is shaking')

    def sit(self) :
        print(f'{self.name} is sitting')

    def lay(self) :
        print(f'{self.name} is laying')

    def come(self) :
        print(f'{self.name} is coming')
