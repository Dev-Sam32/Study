import threading
import time

# 클래스 안에 threading.Thread 사용
# __init__ 생성자를 반드시 호출
class MyThread(threading.Thread):
    def __init__(self, msg):
        threading.Thread.__init__(self)
        self.msg=msg
        self.daemon=True

    def run(self):
        while True:
            time.sleep(1)
            print(self.msg)

for msg in ['you','need','python']:
    t=MyThread(msg)
    t.start()

for i in range(100):
    time.sleep(0.1)
    print(i)