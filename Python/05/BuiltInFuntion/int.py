# int(x) 는 입력받은 숫자를 정수형으로 리턴한다.
print(int('3'))
print(int(3.4))

# int(x,radix) radix 진수로 표현된 문자열을 10진수로 변환하여 리턴한다.

print(int('11',2))
#2진수 11에 해당하는 10진수 값은 3이다.

print(int('1A',16))
# 16진수 1A에 해당하는 10진수 값은 26이다.(16 + 10(a))