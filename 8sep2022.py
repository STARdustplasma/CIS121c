
## Lab 3 (September 9th)
## create a tax calculator

## objective: asks for income, maritial status and deduces the tax 

print(" ")
print("Start of Lab 3")
print(" ")

##creating all the variables
earnedincome = 0
taxowed = 0
tax10 = .10
tax12 = .12
tax22 = .22
maritalstatus = 0
invalid = 0

print("please enter your martial status")
maritalstatus = str(input("input an s for single and an m for marriage: "))

while maritalstatus != "m" or maritalstatus != "s" :
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
    elif earnedincome >= 86375 :
        print("sorry!")
        print("this calculator only calculates earnings below 86376 for single users")
        invalid = 1

if maritalstatus == "m" :
    if earnedincome >=0 and earnedincome <= 19900 :
        taxrate = 10
    elif earnedincome >=19901 and earnedincome <=81050 :
        taxrate = 12
    elif earnedincome >=81051 and earnedincome <=172750 :
        taxrate = 22
    elif earnedincome >= 172751 :
        print("sorry!")
        print("this calculator only calculates earnings below 172751 for married users")
        invalid = 1
## defines taxrate based on user's earning and marital status (top is s, bot is m)


if invalid == 1 :
    print(" ")
    print("you earned too much for this calculator")
    exit()
## excludes invalid ammounts
if maritalstatus == "s" :
    if earnedincome >= 40526 :
        tax22 = (earnedincome - 40525) * tax22
        tax12 = (40525 - 9950) * tax12
        tax10 = 9950 * tax10
        taxowed = tax22 + tax12 + tax10
    elif earnedincome >=9951 and earnedincome <=40525 :
        tax12 = (earnedincome - 9950) * tax12
        tax10 = 9950 * tax10
        taxowed = tax12 + tax10
    elif earnedincome >=0 and earnedincome <= 9950 :
        tax10 = earnedincome * tax10
        taxowed = tax10
## this calculates the tax owed of single users

elif maritalstatus == "m" :
    if earnedincome >= 81051 :
        tax22 = (earnedincome - 81050) * tax22
        tax12 = (81050 - 19900) * tax12
        tax10 = 19900 * tax10
        taxowed = tax22 + tax12 + tax10
    elif earnedincome >=19901 and earnedincome <=81050 :
        tax12 = (earnedincome - 19900) * tax12
        tax10 = 19900 * tax10
        taxowed = tax12 + tax10
    elif earnedincome >=0 and earnedincome <= 19900 :
        tax10 = earnedincome * tax10
        taxowed = tax10
## this calculates the tax owed of married users

print(" ")
print("congratulations!")
print("you owe", round(taxowed, 2), "in taxes this year!")
## displays taxowed after calculating 