# 1000 미만의 자연수 중 3의 배수와 5의 배수의 합
total=0
for n in range(1,1000):
    if n%3==0 or n%5==0:
        print(n,end=' ')
        total+=n
print("")

print(total)

