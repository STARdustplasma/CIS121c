
## while loops
from tkinter import N

number = 11
while number <= 10 :
    print(number)
## ^ conditional loop



## for loop
for number in range (1,11) : ## goes from 1 to 10 (first number to the second number -1)
    print(number)
## beginning to end loop

for number in range (1,11) :
    if number % 2 == 0 :
        print(number)


## functions
## defines short script as a variable
## format it as "lowerUpperUpper()""
def askUserForName() :
    name = input('please enter your name: ')
    return name
## whenever it is called, it will do everything inside the sunction
## return outputs the results exist outside of the scope and makes sure it exists
## scope is the innerds of a function
## w/o return, the value of name does not exist outside of the script

## create a function to ask the user for their age and then use that value to print out the nextt 20 years
## ex. i type 18 and it shows 19 20 21 all the way to 38

def askUserForAge() :
    age = int(input('please enter your age: '))
    return age


name = askUserForName()
age = askUserForAge()
for loop in range (1, 21) :
    print(age+loop)


##kendrick ver

name = askUserForName()
age = askUserForAge()
for number in range(age, age+21) :
    print(number)


## string manipulation
print(name[0:3])
## would print out the first 3 letters of your answer
print(name[1:3])
## would print out the first 3 letters of your answer except the first letter
print(name[2:3])
## would print out the first 3 letters of your answer except the two letters

for letter in name :
    print(letter)
## prints each letter individually

## for(x, y) loops run from x to y with a new variable

