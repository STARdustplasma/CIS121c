# class person :
#     def __init__(self, name) :
#         self.name = name

#     def getname(self) :
#         print(self.name)

#     class employee(person) :
#         def isepmloyee(self) :
#             return True
import random
import re

## parent class
class student :
    def __init__(self, name, last)  :
        self.name = name
        self.last = last 
        self.__snn = random.randint(100000000,999999999)
    
    def display(self) :
        print(f'name : {self.name}')
        print(f'last name : {self.last}')
        print(f'ssn : {self.__snn}')
    
    def snn(self) :
        return self.__snn


## child class
class highschool(student) :
    def __init__(self, name, last, grade) :

        super().__init__(name, last)
        self.grade = grade

    def displayinfo(self) : ##polymorphism
        print(f'name : {self.name}')
        print(f'last name : {self.last}')
        # print(f'ssn : {self.__snn}') >> leads to an error
        print(f'snn : {student.snn(self)} ')
        print(f'grade : {self.grade}')

name = highschool('name', 'last', 11)

highschool.displayinfo(name)




class account :
    def __init__(self, username, password, recover) :
        self.__username = username
        self.__password = password
        self.__recover = recover

    def changeuser(self) :
        i = input('please input recovery phrase: ')
        if i == self.__recover :
            j = input('input new username: ')
            self.__username = j
        else:
            return account.changeuser(self)

    def changepass(self) :
        i = input('please input recovery phrase: ')
        if i == self.__recover :
            j = input('input new password: ')
            self.__password = j
        else:
            return account.changepass(self)

    def display(self) :
        print(f'user: {self.__username}')
        print(f'user: {self.__password}')
        print(f'user: {self.__recover}')

class update(account) :

    def __init__(self, username, password, recover):
        super().__init__(username, password, recover)

    def changeuser(self) :
        i = input('please input recovery phrase: ')
        if i == self.__recover :
            j = input('input new username: ')
            self.__username = j
        else:
            return account.changeuser(self)

    def changepass(self) :
        i = input('please input recovery phrase: ')
        if i == self.__recover :
            j = input('input new password: ')
            self.__password = j
