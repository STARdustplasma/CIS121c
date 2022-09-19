## create  scripte that asks for 6 numbers, add them, and then print out all the odd numbers starting at that number up to 2000
# if it is also a divisor of 96, print out found one!

def askForNumber() :
    number = int(input('give me a new number: '))
    return number

num1 = askForNumber()
num2 = askForNumber()
num3 = askForNumber()
num4 = askForNumber()
num5 = askForNumber()
num6 = askForNumber()

sum = (num1 +num2 +num3 +num4 +num5 +num6)

for numbers in range (sum, 2001) :
    if numbers % 2 == 1 :
        print(numbers)
    if 96 %sum == 0 :
        print("found one!")


dvd = int(input('ho many dvds are you buying: '))


cost = dvd*3
if cost >= 50 :
    print('you pay', cost - cost*.2)
elif cost >= 30 :
    print('you pay', cost - cost*.1)
else :
    print(cost)




for i in range(1,7) :
    for j in range (1,i):
        print(j,end =" ")
    print(" ")

## nest for statement
## end keeps it instead of sending it to the next line