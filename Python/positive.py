from typing import Literal

def positive(l):
    result=[]
    for i in l:
#        if i>0:
            result.append(i)
    return result
#list 함수 사용
intA=[]
strA=input("숫자배열을 입력하세요.(띄어쓰기 구분):").split()
print(strA)
for i in strA:
    intA[i]=int(strA[i])
print(intA)
# intA=[int(x) for x in strA]
# #내장함수 map 사용
# #a=map(int,input("숫자배열을 입력하세요.(띄어쓰기 구분):").split())
# #print(positive([1,-3,2,0,-5,6]))
# print(positive(intA))