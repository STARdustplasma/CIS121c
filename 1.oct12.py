import random
import statistics

# def createlist(number) :
#     temp1 = []
#     temp2 = []
#     for i in range(number):
#         temp1.append(random.randint(1,9))
#         temp2.append(random.randint(1,9))

#     return [temp1,temp2]

# print(createlist(5))

# def countletter(word) :
#     a = 0
#     u = 0
#     for i in word :
#         if i == 'a' :
#             a +=1
#         elif i == 'u' :
#             u +=1
#     count = {
#         'a count' : a,
#         'u count' : u
#     }
#     print(count)

# countletter('assitance')

# def miletime() :
#     time = []
#     total = 0
#     for i in range(10): 
#         j = int(input('mile time: '))
#         time.append(j)
#         total += j

#     temp = {
#         'times' : time,
#         'avg' : round(total/10, 2),
#         'worst' : max(time),
#         'best' : min(time)
#     }

#     return temp


# print(miletime())


list1 = [1,2,3]
list2 = ['number 1', 'number 2', 'number 3']

def list2dict(key,data) :
    temp = {}

    for i in range(len(key)) :
        temp[key[i]] = data[i]
        
        temp['number '+str(data[i]*5)] = data[i]*5
        
    return temp

print(list2dict(list2,list1))
        
