# 문자열을 입력 받아
# 같은문자가 연속적으로 반복되는 경우, 반복횟수와 반복되는 문자열 표기
# input aaabbcccccca
# output a3b2c6a1

# 같은 문자인지 판단

## 내가 한 거...
# cnt=0

# str=input("문자열을 입력하시오.")

# for i in str:
#     if i == i-1:
#         cnt+1
#     else:
#         print(i,count)
#         cnt=0

# print(str)

def compress_string(s):
    _c=""
    cnt=0
    result=""
    for c in s:
        if c!=_c:
            _c=c
            if cnt:result+=str(cnt)
            result+=c
            cnt=1
        else:
            cnt+=1
    if cnt:result+=str(cnt)
    return result

input_str=input("입력하실 문자열을 작성하시오 :")
print(compress_string(input_str))