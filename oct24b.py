from oct24 import Animal

class cat(Animal):
    def __init__(self,name) :
        super().__init__(name)
        self.animal = Animal()
