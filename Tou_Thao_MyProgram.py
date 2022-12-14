## modules
import Tou_Thao_Stats

file = open('50DayFruitData.txt', 'r')
data = file.read().splitlines() ## splitlines removes the new lines from your imported code \n


# print(data[1].split()) ## splits the individual thing into another list
data.pop(0)

banana_tracker = []
strawberry_tracker = []
apple_tracker = []

for i in data :
    temp = i.split() # splits every individual thing into lists

    if temp[1] == "apple" : ## checking to see if it is apple
        apple_tracker.append(int(temp[2])) ## converts number to an int and adds the number to list
    elif temp[1] == "banana" : ## checking to see if it is banana
        banana_tracker.append(int(temp[2])) ## converts number to an int and adds the number to list
    else : ## if it is not banana or apple then it will go to strawberry
        strawberry_tracker.append(int(temp[2])) ## converts number to an int and adds the number to list

amedian = round(Tou_Thao_Stats.mean(apple_tracker), 2) # taking the mean and median of apple
amean = round(Tou_Thao_Stats.median(apple_tracker), 2)

bmedian = round(Tou_Thao_Stats.mean(banana_tracker), 2) # taking the mean and median of banana
bmean = round(Tou_Thao_Stats.median(banana_tracker), 2)

smedian = round(Tou_Thao_Stats.mean(strawberry_tracker), 2) # taking the mean and median of strawberry
smean = round(Tou_Thao_Stats.median(strawberry_tracker), 2)


# with open("tou_thao_output.txt", "w") as f: ## creating and exporting to another type of file
#     ## command('name.filetype', write)
#     f.write("APPLE DATA"+"\n""the mean of apples eaten is "+ str(amean)+"\n"+"the median of apples eaten is "+ str(amedian)+"\n")
#     f.write("\n"+"BANANA DATA"+"\n""the mean of banana eaten is "+ str(bmean)+"\n"+"the median of banana eaten is "+ str(bmedian)+"\n")
#     f.write("\n"+"STRAWBERRY DATA"+"\n"+"the mean of strawberry eaten is "+ str(smean)+"\n"+"the median of strawberry eaten is "+ str(smedian))


summary = {
    'mean' : str(round(Tou_Thao_Stats.mean(apple_tracker), 1)),
    'median' : str(Tou_Thao_Stats.median(apple_tracker)),
    'mode' : str(Tou_Thao_Stats.mode(apple_tracker))
}

with open('tou_thao_output.txt', 'w') as f:
    for i in summary :
        f.write('The '+ i +' number of apples eaten is/are ' + summary[i] + '\n')