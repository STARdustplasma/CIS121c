
#create an if then statement regarding income. if more than 450000, respond with snarky remark

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
