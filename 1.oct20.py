# from car import Car
from employee import Employee
from circle import Circle


# r32 = Car(4, 'RB25', 'GTR R32', 1992)


#         ## v change this to get different parts
# print(r32.model)

# r32.changeyear(1998)
#     ## ^ avoid touching the variable directly, create a script to change parts of the formula instead



# p911 = Car(4, 'ww91', '911', 1993)

# print(p911)

## create a class called Employee which has hourly wage, position, hours a week and name
## method that calculates the yearly salary
## look the output look better

bob = Employee(70,70,'janitor','bob t')

print(bob)
bob.changehourly(90)
print(bob)

## add methods to change the values in class



## create a class called circle with a variable called radius
test = Circle(7)
print(test)