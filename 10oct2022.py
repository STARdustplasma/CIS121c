## create a function that takes two lists and makes them a dictionary

import random

list1 = [1,2,3]
list2 = ['number 1', 'number 2', 'number 3']

def list2dict(key,data) :
    temp = {}
    ## if len(data) == len(key) :
    for i in range(len(key)) :
        temp[key[i]] = data[i]
    ## else :
    ##  temp = 'lists are not the same length'
    return temp

# print(list2dict(list2, list1))


## create a function that can multiply all the numbers in a dictionary by a given number. 
## make sure that the values are numerical

info = {
    'num 1' : '12',
    'num 2' : 'abcs',
    'num 3' : '56'
}

def multiply(data, number) :
    temp = {}
    for i in data :
        if data[i].isdigit() :
            temp[i] = int(data[i])*number
    return temp

# print(multiply(info, 2))

## create a function that generates a dictionary with 5 numebrs, 
## then make another function that generates random numbers until it generates one within that dictionary

def randomdict() :
    temp = {}
    for key in range(1,6):
        temp[key] = random.randint(1,100)
    return temp

def guess(data) :
    found = False
    while found != True :
        x = random.randint(1,100)
        # print(x)
        for key in data :
            if x == data[key] :
                print('found one', x)
                found = True        


dict1 = randomdict()
print(dict1)
guess(dict1)