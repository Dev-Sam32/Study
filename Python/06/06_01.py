# 구구단
# def gugu(n):
#     result=[]
#     i=1
#     while i<10:
#         result.append(n*i)
#         i=i+1
#     return result

# print(gugu(2))

def gugu(n):
    for i in range(1,10):
       print(n,"x",i,"=",n*i)
    return ""

num=int(input("몇단의 구구단이 보고 싶나요? "))
print(gugu(num))