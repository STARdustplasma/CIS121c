
#create an if then statement regarding income. if more than 450000, respond with snarky remark

from random import randint


income = int(input("How much do you make? "))
## ^asks about income and converts it into int

alot = 450000
## variable determining alot

if income > alot:
    print(income, "is alot")
    print("damn u rich.")
##if more than 450k
else:
    print("dw u got it")
##if less than 450k

print(" ")
## ^creating space

## loops
## basic loop v
number = int(input("can i get a number less than 10? "))
while number <= 10 :
    print(number)
    number = number + 1


## create a guessing game that gives the user 3 chances to guess a number
print(" ")
print(" ")
print("guessing game")
answer = randint(1, 10)
round = 1
while round <=3:
    print(" ")
    print("round", round)
    guess = int(input("guess a number 1 to 10: "))
    if guess == answer :
        round = 4
        print("great job!")
        print("the answer was", answer)
    else :
        print("wrong!")
        round = round +1
        if round == 4 :
            print(" ")
            print("game over!")
            print("the answer was", answer)


## kendrick ver
win = 0
round = 0
while round <= 3 and win != 1 :
    guess = int(input("guess the number: "))
    if guess == answer:
        print("gj")
        win = 1
    else :
        round = round + 1

