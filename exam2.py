## 1 
def evenodds(data1,data2) :
    dataset = data1+data2 ## combines the to lists into 1 big list

    odds = [] ## creates a list for odds
    evens = [] ## and evens
    for i in dataset : # runs through each one in the big list to check if they are odd or even
        if i % 2 == 0 :
            evens.append(i) ## adds to even list if even
        else :
            odds.append(i) ## adds to odd list if odd
    
    ## creates final dictionary
    temp = {
        'odd' : odds,
        'even' : evens

    }
    return temp



from calendar import day_abbr, month, month_abbr, month_name, monthcalendar, monthrange
import random
## 2
def count(list1, list2) : ## function that counts
    data = list1+list2 ## adds 2 lists to make 1 big list
    info = {} ## creates dictionary
    for i in data: ## goes through each number
        if i in info : ## if ive already tracked the number then this ignores it
            pass
        else : ## counts the number of timse a number appears in the big data
            info[str(i)] = str(data.count(i))


    with open('RESULTS4.txt', 'w') as f: ## writes everything to a new file
        for i in info :
            f.write(i +' : repeats ' +info[i] + ' times \n')
    return info

def randomlist2count() : # <---- run this
    list1 = [] ## defining the lists
    list2 = []
    for i in range(200) : ## loop that repeats 200 times
        list1.append(random.randint(1,100)) ## creates the random lists
        list2.append(random.randint(1,100))

    count(list1,list2) ## executes count() with newly generated lists




import statistics
## 3
def tempname() :
    file = open('steps.txt', 'r')
    data = file.read().splitlines()
    temp = []
    for i in data :
        temp.append(int(data[i]))
    
    mean = statistics.mean(temp[0:30])
    print(mean)

## dont understand how to take into consideration each month as a seperate number to divide by sorry
