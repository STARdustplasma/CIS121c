## doc.python.org <== python cheatsheet

import random


names = ['tou', 'thao']

info = {
    'tou' : 18,
    'bob' : 3456
}

## function to convert numbers in str to digit
def str2int(data) :
    new = []
    for i in data : ## explores each individual cell inside of a list
        if i.isdigit() :
            new.append(int(i))
    return new

## function to add 5 to nunmbers            
def plus5(data) :
    temp = []
    for i in data:
        i += 5
        temp.append(i)
    return temp



## Opening a file
file = open('5oct.txt','r')
## get data from file and split them
data = file.read().splitlines()

print(data)

## create a function that takes a list of values in str and returns a new list with only ints (move to top)
data = str2int(data)
print(data)

## create a function that takes a list of values and adds 5 (moved to top)
data = plus5(data)
print(data)

## write the results to a new file
with open('5octresults.txt', 'w') as f:
    for i in data :
        f.write(str(i) + '\n')

## generate a list with 100 random numbers. then write the values onto a file called 'random_numbers_generated.txt'
## creta a function that counts how many times each number appears and use a dictionary to keep track

numbers = []
for i in range(0,100) :
    temp = random.randint(1,100)
    numbers.append(temp)

with open('100random.txt', 'w') as f:
    for i in numbers :
        f.write(str(i) + '\n')

file = open('100random.txt','r')
data = file.read().splitlines()
print(data)

def count(data) :
    info = {}
    for i in data:
        if i in info :
            pass
        else :
            info[str(i)] = 'appeared ' + str(data.count(i)) + ' times'
    return info


data = count(data)


## write the info from dictionary to a file called final.txt

with open('final.txt', 'w') as f:
    for i in data :
        f.write(i +' : ' +data[i] + '\n')