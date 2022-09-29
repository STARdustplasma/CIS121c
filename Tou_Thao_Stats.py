

# def mean(data) : ## peremeters, something the function ill ork ith from outside the function
#     result = 0
#     sum_ = 0
#     print(data)
#     for item in data :
#         sum_ += item
#     result = sum_ / len(data)

#     return result


data = [1, 5, 4, 2, 3]
import statistics

def median(data) :
    result = statistics.median(data)
    return result

def mean(data) :
    result = statistics.mean(data)
    return result

print(median(data))
print(mean(data))