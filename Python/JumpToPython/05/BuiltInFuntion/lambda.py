# lambda 는 함수 생성 예약어
# 간략하게 함수 생성시 필요
# *** def 와 동일하지만, def를 사용할 수 없는 곳에서도 사용 가능
# 리스트 안도 들어 갈 수 있다.

myList=[lambda a,b:a+b, lambda a,b:a*b]
print(myList)
print(myList[0])
print(myList[0],(3,4))