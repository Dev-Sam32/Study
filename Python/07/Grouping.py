import re
# \w 문자,숫자 매치 [a-zA-Z0-9]
# \s 문자 사이 whitespace 매치 [\t\n\r\f\v]
# \d 숫자와 매치
# [-] '-'와 매치
# + 한번 이상 
# search 문자열 전체 검색
# \b 단어 구분자(단어 경계를 구분) : 보통은 whitespace
#  ㄴ \s랑 헷갈려...
# . 줄바꿈 문자 \n을 제외한 모든 문자 매치

# p=re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
# m=p.search("park 010-1234-1234")
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))

# # 재참조 메탄 문자 \1 은 첫번째 그룹을 지칭한다.
# p=re.compile(r'(\b\w+)\s+\1')
# p.search('Paris in the the spring').group()
# # 첫번째 그룹인 (\b\w+)를 다시 참조 한다.
# # (\b\w+)\s+\b\w+ 즉 단어+" "+같은 단어 조합을 매칭한다
# # the the

# 그루핑 문자열에 이름 붙이기

# p=re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m=p.search("park 010-1234-1234")
# print(m.group("name"))

# 그룹명을 이용한 재참조
p=re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
m=p.search('Paris in the the spring')