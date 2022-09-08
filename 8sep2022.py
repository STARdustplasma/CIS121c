
## Lab 3 (September 9th)
## create a tax calculator

## objective: asks for income, maritial status and deduces the tax 
from tkinter import E


print(" ")
print("Start of Lab 3")
print(" ")

##creating all the necessary variables
earnedincome = 0
taxowed = 0
taxrate = 0
maritalstatus = 0

print("please enter your martial status")
maritalstatus = str(input("input an s for single and an m for marriage: "))

while maritalstatus != "m" and maritalstatus != "s" :
    print("your answer was invalid")
    print("please try again")
    maritalstatus = str(input("input an s for single and an m for marriage: "))
## this makes sure the user input an s or an m

earnedincome = float(input("please input much you earned in 2021: "))
## asks for user's earning
if maritalstatus == "s" :
    if earnedincome >=0 and earnedincome <= 9950 :
        taxrate = 10
    elif earnedincome >=9951 and earnedincome <=40525 :
        taxrate = 12
    elif earnedincome >=40526 and earnedincome <=86375 :
        taxrate = 22

if maritalstatus == "m" :
    if earnedincome >=0 and earnedincome <= 19900 :
        taxrate = 10
    elif earnedincome >=19901 and earnedincome <=81050 :
        taxrate = 12
    elif earnedincome >=81051 and earnedincome <=172750 :
        taxrate = 22
## defines taxrate based on user's earning and marital status (top is s, bot is m)

taxowed = (earnedincome / 100) * taxrate
print("your taxrate is", taxrate)
print("therefore you owe", taxowed)
## displays taxrate and taxowed after calculating taxowed

print(" ")
print("congratulations!")
print("you actually earned", earnedincome - taxowed)
## tells earnings after tax