# names = ['tou',2,3.45,18]

# print(names[2])

# ## empty dictionary
# info = {}


# ## filled dictionary
# info = {
#     'patient 0': ['tou','thao',18],
#     'patient 1' :23,
#     'patient 2' : ['bob','builder',134]
# }

# ## how to add to dictionaries
# info['patient 3'] = ['roger','na','na']

# ## lists are index bsaed while dictionaries are key based

# info = {
#     'name0' : [input('what is first name? '),
#      input('what is last name? '),
#      input('what is your age? ')]
# }



# name = input('please enter name')
# last = input('please input last name')
# age = input('please input age')

# info = {
#     name : [name,last,age]
# }

def avg_goals(info) :
    sum = 0
    for info in info :
        sum += info[info]

    return sum/len(info)

# name = []
# goals = []

# for i in range(0,5) :
#     players = input('give me a soccer player ')
#     name.append(player)
#     count = input('how many goals ')
#     goals.append(int(count))

# info = {}

# for i in range(0, len(name)) :
#     info['name'+str(i)] = [name[i], goals[i]]

# print('average was', avg_goals())



# info = {}
# for i in range(5) :
#     name = input('player name')
#     goals = int(input('score'))

#     info[name] = [goals]

# print('average was: ', avg_goals(info) )


## checking to see if it has dupes
info = {
    'test 0' : 0,
    'test 1' : 1,
    'test 2' : 2
}

def check_keys(data,key):
    
    for keys in data :
        if keys == key:
            return True
    
    return False

# print(check_keys(info,'test 1'))


# def adddict(key1,key2) :
#     results = 0
#     results = key1 + key2
#     return results

info1 = {
    'data' : [1,2,3,4,5]
}

info2 = {
    'data' : [6,7,8,9,10]
}

def addtoget(data,data2) :
    total = []
    for i in range(len(data['data'])) :
        total.append(data['data'][i] + data2['data'][i])
    print(total)

addtoget(info1, info2)