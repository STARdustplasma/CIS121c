number = int(input('please enter number '))
count = 1

count2= 1
divisor = 1
divisorsum = 0
perfect = 0
abundant = 0
deficient = 0


while count <= number:
    while count2 < count:
        if count % count2 == 0 :
            divisorsum += count2
        count2 +=1
            
            
    if count > divisorsum :
        deficient +=1
    elif count < divisorsum :
        abundant +=1
    else :
        perfect +=1

    count +=1
    divisorsum = 0
    count2 = 1

print(perfect, abundant, deficient)

