#python memo.py -a "Life is too short"
# 위의 명령이 실행될 수 있게...

import sys

option=sys.args[1]

if option=='-a':
    memo=sys.args[2]
    f=open('memo.txt','a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option=='-v':
    f=open('memo.txt')
    memo=f.read()
    f.close()
    print(memo)