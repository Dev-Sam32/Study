# 5줄
# def two_times(numberList):
#     result=[]
#     for number in numberList:
#         result.append(number*2)
#     return result

# result = two_times([1,2,3,4])
# print(result)

# map(f,iterable) 사용 2줄
# def two_times(x):return x*2
# print(list(map(two_times,[1,2,3,4])))

# map(f,iteralbe), lambda 사용 1줄
# print(list(map(lambda x:x*2,[1,2,3,4])))

def plus_one(x):
    return x+1

print(list(map(plus_one,[1,2,3,4,5])))