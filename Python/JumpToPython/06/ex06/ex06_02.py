#0~9까지의 문자로 된 숫자를 입력 받고
# 0~9까지 모든 숫자가 각각 한번씩만 사용된 것인지 확인하는 함수
# 0123456789 01234 01234567890 6789012345 012322456789
# true false false true false

# string='0123456789'

# for i in string:
#     for j in range(10):
#         if i == j:

#     else:
#         print()

def chkDupNum(s):
    result=[]
    for num in s:
        if num not in result:   # not in 으로 유무를 확인... 
            result.append(num)  # not in이 참일 때, 없는 것이므로 result 문자열에 추가
        else:
            return False        # not in 이 거짓인경우 이미 있으므로 False 리턴
    return len(result)==10      # for문을 수행하고 문자열길이가 10인지,(0~9 한번씩 사용하려면 10이여야함..)

chkNum=input("확인할 숫자열을 입력하시오(0~9) : ")
print(chkDupNum(chkNum))