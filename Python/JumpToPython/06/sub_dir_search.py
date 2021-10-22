import os

def search(dirname):
    filenames=os.listdir(dirname)                       # 해당 디렉터리의 '파일'리스트를 리턴 하는 함수
    for filename in filenames:
        full_filename=os.path.join(dirname,filename)    # 디렉터리와 파일명을 이어 리턴하는 함수
        if os.path.isdir(full_filename):                # 해당 디렉터리(인수)가 디렉터리면 True 파일이면 false
            search(full_filename)                       # 재귀 호출
        else:
            ext=os.path.splitext(full_filename)[-1]     # 파일명을 확장자를 기준으로 둘로 나눈다
            if ext =='.py':                             # 뒤에서 첫번째, 즉 확장자
                print(full_filename)

search("/Users/Sam/Documents/Git/Study/Python")