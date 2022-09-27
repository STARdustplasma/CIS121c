## Tou Hmong Thao


## 1a. does not work because age is defined as a string and not an integer. it is not innately wrong but the code also does not utilize the variable 'random.number'
## you could fix it by converting the input in age to an integer with int() and utilize 'random_number' by printing it or removing it.
 
## 1b. does not work because 'number' is not a defined variable and the while loop as no way to end.
## you could fix defining 'number' as any integer and then making sure that the variable 'number' increases by at least 1 at the end of each loop with 'number +=1'.

## 1c. the code works

## 1d. does not work because there is no indent in the for loop. the loop is not doing anything and then when it comes time to print i, i no longer exists
## you could fix it by indenting print to make sure it is nested in the for statement

## 1e. does not work because the end of the loop is written incorrectly
## you could fix it by defining user_number as an integer when it is asking for input


## 2.)
milk = int(input('how much milk would you like to buy? '))
egg = int(input('how much egg would you like to buy? '))
bacon = int(input('how much bacon would you like to buy? '))
## these variables ask for how many of each

milkcost = float(milk*2)
eggcost = float(egg*1.5)
baconcost = float(bacon*3)
total = milkcost+eggcost+baconcost
tax = round(total*.11, 2)
## these variables calculate the costs of everything, the total, and the taxes

print(milk,'milk -', '$'+str(milkcost))
print(egg,'egg -', '$'+str(eggcost))
print(bacon,'bacon -', '$'+str(baconcost))
print('Total - $'+str(total+tax))
## these print statements display the required information


## 3.)

number = input('please input 10 digit phone number: ')
## this variable asks for the 10 digit number
print('('+number[0:3]+')', number[3:6]+'-'+number[6:10])
## this statement prints it out as a readable string


## 4.) 
from random import randint
count = 0
#this variable will count how many divisors there are
while count <10: 
    x = randint(1,60) # this creates random integers
    if 48 % x == 0 : # this asks if 48 is divisible by the number
        if x % 2==0 : # this determines if it is even
            if x >= 15: # this determines if it is greater than 15 and even
                print("i generated the number", x, "randomly")
            else: # if it is not greater than 15, but it is even, then this is what the statement will do
                print(x)
        count +=1 # this tells the function that a divisible number has been found regardless of whether the number is displayed or not

