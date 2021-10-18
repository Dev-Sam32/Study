# sorted(iterable) 입력값을 정렬하여 다시 리스트로 리턴하는 함수

# print(sorted([3,1,2]))
# print(sorted('zero'))

a=[3,1,2]
result=a.sort()
# sort 함수는 return 값이 없다. 리스트를 정렬할 뿐이다.
# 반면 sorted 함수는 결과를 리턴한다.

print("result:",result)
print("a:",a)