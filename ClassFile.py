"""
#Name
#Date

This implements the RoboFriend class.
"""

class RoboFriend :
    def __init__(self,name, age) :
        self.name = name
        self.age = age


    def stateName(self) :
        print(f"Hello. My name is {self.name}\n")


    def stateAge(self) :
        print(f"I'm {self.age} years old\n")

