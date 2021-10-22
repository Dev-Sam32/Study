import threading
import time

# say 함수는 1초마다 msg를 출력하는 무한 루프 함수


def say(msg):
    while True:
        time.sleep(1)
        print(msg)

# 변수 msg에 리스트에 담긴 값을 차례로 입력하고
# threading 모듈의 Tread 함수를 호출한다 
# 타겟 함수와 인자 튜플을 정의한 threading.Thread를
# t에 정의한다.
# deamon flag를 설정하여 주 프로그램이 종료되는 순간 daemon 스레드도 종료
for msg in ['you', 'need', 'python']:
    t=threading.Thread(target=say, args=(msg,))
    t.deamon=True

    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)