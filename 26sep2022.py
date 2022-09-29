# ## list
# names = ["kendrick", 'gabriel']
# ## lists are not limited to 1 data type
# random_Stuff = ['ken', 1, 1.22, False,[]]

# ## ho to access values
# print(names[0])
# print(names[1])
# print(names[-1]) ## gives you the LAST value

# for value in random_Stuff:
#     print(value)


# ## create a script that goes through the list [2, 45, 32, 43,22] and displays the square of every number
# numbers = [2, 45, 32, 43,22]

# for i in numbers:
#     print(i**2) ## alt print(i**2, end='')

# # for i in numbers:
# #     result.append(i**2)

# ## know the length of a list with
# print(len(numbers))

# ## crete a script to ask for age name and number dd the values to a display and display them
# name = input('what is your name? ')
# age = int(input('what is your age? '))
# num = int(input('what is a number? '))

# info = [name, age, num]
# print(info)


## create a script that creates a list wo the number 20 in it [20,34,23,2,11,24,4,20,21,12,20,20,20]
numbers = [20,34,23,2,11,24,4,20,21,12,20,20,20]
newnum = []
for i in numbers:
    if i != 20:
        newnum += [i]
    
    ## varname.append(list)
print(newnum)

## alternative
newnum = []
for i in numbers:
    if i != 20:
        newnum.append(numbers)

print(newnum)