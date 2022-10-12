# names = ["tou", "gabriel"]

# ## indexing
# print(names[0]) # = print('tou')

# for i in names:
#     print(names[0])


# ## createa script that creates the following sentence

# list1 = ['I','your','dude']
# list2 = ['am','boss','.']

# for i in range(0,3) :
#     print(list1[i], list2[i], end=' ')

# def asknums() :
#     count = 0

#     list1 = []
#     list2 = []
#     list3 = []
#     while count < 10 :
#         num = input('please enter a num: ')

#         if num.isdigit() :
#             if count < 5:
#                 list1.append(int(num))
#             else :
#                 list2.append(int(num))
#         else :
#             num = input('please input a number: ')
#         count += 1

#     for i in range(0,5) :
#         list3 += [list1[i]+list2[i]]
#     print(list3)



list1 = ['mom', 'dad', 'bro'] 
list2 = []
count = 0

while count < 3 :
        rank = input('what rank do you give your '+ list1[count] + '? ')
        if rank.isdigit():
            list2.append(int(rank))
        count +=1
    

print('rankings: ==========')
for i in range(0,3):
        print(list1[i], "-", list2[i])
print('====================')
