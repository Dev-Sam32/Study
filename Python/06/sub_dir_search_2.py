import os
# os.walk(dir)는 인자로 전달된 경로에서 경로, 디렉터리, 파일명을 튜플형태로 넘겨준다.
# 하위 디렉터리 모두 방문하기 때문에 파일명의 확장자가 '.py'에 해당되는지만 질의하면 된다.
for (path, dir, files) in os.walk("/Users/Sam/Documents/Git/Study/Python"):
    for filename in files:
        ext=os.path.splitext(filename)[1]
        if ext == '.py':
            print("%s/%s"%(path,filename))