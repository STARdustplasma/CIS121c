
def clearletter(data) :
    temp = []
    for i in data :
        if i.isdigit() :
            temp.append(int(i))
    return temp

def readfile(filename) :
    file = open(filename,'r')
    temp = file.read().splitlines()
    temp = clearletter(temp)
    return temp

data = readfile('randomValues.txt')

## recursion > when we ues the same function to solve itself

def findmin(index, current, data) :
    if len(data) == 0:
        print('list empty')
    if len(data) == 1:
        return data[0]

    min = data[index]

    if min <= current :
        current = min

    if index >= len(data)-1 :
        return current
    else :
        return findmin(index+1, current, data)


def findmax(index, current, data) :
    if len(data) == 0:
        print('list empty')
    if len(data) == 1:
        return data[0]

    max = data[index]

    if max >= current :
        current = max

    if index >= len(data)-1 :
        return current
    else :
        return findmax(index+1, current, data)



def extrema(data, minstatus = True, maxstatus =True) :
    if minstatus != False :
        print(findmin(0, data[0], data))
    if maxstatus != False :
        print(findmax(0, data[0], data))
    if maxstatus == False and minstatus == False :
        print('nothing was done')

extrema(data, False, False)