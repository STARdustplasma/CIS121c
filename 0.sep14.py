
name = 'tou' ## str
number = 1 ## int
distance = 1.2 ## float
finished = True ## boolean

print('tou')
print(name,number,distance)


## nested if
if number > 10 :
    print('something')
elif number < 10 :
    print('something else')
else :
    print('nothing')

## not nested if
if number > 10 :
    print('something')
if number < 10 :
    print('something else')

while number <= 10 :
    print(number)
    number +=1


## write a script that keeps asking user for a number and check if it is even or odd. let the user know which it is. if it asks for 0 end code

number = int(input('input number: '))

while number != 0 :
    if number % 2 ==0 :
        print('that number is even')
    else :
        print('that number is odd')
    number = int(input('input another number: '))
print('you have inputted 0')

## Kendrick
done = False

while done !=True :
    number = int(input('please enter number: '))

    if number == 0 :
        print('bye')
        done = True
    elif number %2 == 0 :
        print('number is even')
    else :
        print('number is odd')

## create a script to ask a user for their name and income. let the user know how much money they would have if they dont spend any money in 20 years
## if user inputs 40k (hey _name_ you make _income_) (this is ho much money you would have in 20 years) (income*1) (income*2)

name = input('please enter name: ')
income = int(input('plese enter income: '))
year = 1

print('hi', name, 'you make', income, 'a year')

# print('this is how much youd have in 20 years')
# while year <=20 :
#     print('$'+str(income*year), 'in year', year)
#     year +=1


## make it so you can tell the person how many years they need to make 10,000 instead of for the next 20 years
print('this is how long it would take for you to make 10k')
outcome = income
while outcome <= 10000 :
    outcome = income*year
    print('$'+str(outcome), 'in year', year)
    year +=1