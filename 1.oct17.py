import random

def randomfile(b):
    with open(b, 'w') as f:
        for i in range(300) :
            f.write(str(random.randint(1,2000)) + '\n')
    file = open(b, 'r')
    data = file.read().splitlines()
    return data

data = randomfile('oct17.txt')

def isolate(data) :
    temp = {}
    count100 = 0
    count50 = 0
    count25 = 0
    for i in data :
        if i == '100' :
            count100 += 1
        elif i == '50' :
            count50 += 1
        elif i == '25' :
            count25 += 1
    temp = {
        '100' : count100,
        '50' : count50,
        '25' : count25
    }
    print(temp)

isolate(data)



# def combinedict(data1,data2) :
#     temp = {}
#     for i in data1 :
#         for j in data2 :
#             if i == j :
#                 temp[i] = [data1[i], data2[j]]
#             else :
#                 temp[i] = [data1[i]]
#                 temp[j] = [data2[j]]
#     return temp

# dict1 = {
#     'data' : [3],
#     'info' : 'na',
#     'stats': 'other filler'
# }

# dict2 = {
#     'data' : [0],
#     'stats' : 'filler',
#     'info' : 'eu'
    
# }

# print(combinedict(dict1,dict2))

def oddeven(data):
    temp = []
    for i in data :
        if i.isdigit():
            if int(i) % 2 == 0 :
                temp.append(i+' is even')
            else :
                temp.append(i+' is odd')
    with open('oct17results.txt', 'w') as f:
        for i in temp :
            f.write(i + '\n')
    return temp

print(oddeven(data))