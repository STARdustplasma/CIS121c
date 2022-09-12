# write a script to ask the user for a number beteen 35 and 1000
# when user enters number your program should prn tthe n umbers from thaat x number to 100


number = int(input('please enter a number between 35 and 1000: '))

while number < 35 or number > 1000 :
    print('your number was too big or too small')
    number = int(input('please enter a number between 35 and 1000: '))

while number >= 35 and number <= 1000 :
    if number < 100 :
        if number % 2 == 0:
            ## '%' checks for the remainder, not the answer
            print(number)
        number +=1
    elif number >=100 :
        print('100')
        exit()



## kendrick example
x = int(input('please enter a number between 35-1000'))
if 35 <= x <= 100 :
    if x >= 100 :
        print('100')
        exit()
    else :
        while x <= 100 :
            if x % 2 == 0 :
                print(x)
            x+=1
else:
    print('you did not enter a valid number')


## Boolean
winner = True
loser = False