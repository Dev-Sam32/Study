# a=[1,2,3,4]
# # a=[i*3 for i in a if i%2 ==0 else i]
# # 짝수면 3을 곱하고 홀수는 그대로인 리스트
# # 기대 결과 1, 6, 3, 12
# # [ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in data] 
# b=[i*3 if i%2==0 else i for i in a]
# b=[i*3 if i%2==0 for i in a]
# print(b)

a=[1,2,3]
b=a
print(id(a), id(b)) #서로 같음, 2086386592320 2086386592320

a[1]=4
print(a,b) #[1, 4, 3] [1, 4, 3]
print(id(a), id(b)) #불변, 2086386592320 2086386592320

c=3
d=c
print(id(c), id(d)) #서로 같음, 2206965825840 2206965825840
c=4
print(c,d) #4 3
print(id(c), id(d)) #c 메모리 달라짐, 2206965825872 2206965825840

