

name = "this is a variable" # <string
### ^^ this is how you create a variable "variable name = variable"
### var names cannot have spaces

name = "tou"

print("tou")
### ^^ hard coding 
print(name)

name = "t"

print(name)
### integers are whole numbers and floats are numbers with decimal



#create a variable to store human age and calculate it in dog years

dogyr = 7
manyr = 18

print("At age", manyr, "a human should be", manyr*dogyr, "years old.")

#try to use as many variables as you can

    # int makes it read as an integer and not a string, input allows for user input with prompt
#<remove   manyr = int(input("How old are you?"))
    # (asking user for age/converting input string into int)

mandogyr = manyr * dogyr
print("At age", manyr, "a human should be", mandogyr, "years old.")



##start of lab 9/1/2022
##start of lab 9/1/2022
##start of lab 9/1/2022
print(" ")
print(" ")
print(" ")
print("lab start")
name = input("what is your name? ")
lastname = input("what about your last name? ")
print("hi", name, lastname)
manyr = float(input("how old are you? "))

month = 30

manmon = (manyr - int(manyr)) * 12
## converts excess year into months
manday = (manmon - int(manmon)) * 30
## converts excess month into days

print("so you are", int(manyr), "years,", int(manmon), "months, and", int(manday), "days old")
mandogyr = manyr * dogyr
## converts human years to dog years
dogmanmon = (mandogyr - int(mandogyr)) * 12
## converts excess dog year into months
dogmanday = (dogmanmon - int(dogmanmon)) * 30
## converts excess dog month into days
print("in dog years, you would be", int(mandogyr), "years old,", int(dogmanmon), "months, and", int(dogmanday), "days")

catyr = 9
mancatyr = manyr / catyr
## converts human years to cat years
catmanmon = (mancatyr - int(mancatyr)) * 12
## converts excess cat year into months
catmanday = (catmanmon - int(catmanmon)) * 30
## converts excess cat month into days
print("in cat years, you would be", int(mancatyr), "years old,", int(catmanmon), "months, and", int(catmanday), "days")


manhoryr = 3 * ((((manyr**2) - 47)/ 7) + 12)
## converts human years to cat years
hormanmon = (manhoryr - int(manhoryr)) * 12
## converts excess cat year into months
hormanday = (hormanmon - int(hormanmon)) * 30
## converts excess cat month into days
print("in horse years, you would be", int(manhoryr), "years old,", int(hormanmon), "months, and", int(hormanday), "days")
print("damn.")

    ## when you want to ask use input() to create a string
    ## int(input()) will convert it into an interger

height = manyr ** 2
## exponents^^
print(" ")
print("if youre", manyr, "then youre probably around", round(height, 2), "cm tall.")
print("probably...")
print(" ")
