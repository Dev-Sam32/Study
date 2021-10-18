# instance(object, class) 인스턴스, 클래스명
# 입력받은 인스턴스가 입력받은 클래스의 인스턴스인지 확인

class Person:pass

a=Person()
print(isinstance(a,Person))

b=3
print(isinstance(b,Person))