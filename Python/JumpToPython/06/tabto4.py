# python tabto4.py src dst
#      sys.argv[0] [1] [2]
# 터널에서 사용가능한 스크립트로....

from os import spawnl
import sys

src=sys.argv[1]
dst=sys.argv[2]

f=open(src)
tab_content=f.read()
f.close()

space_content=tab_content.replace(" ","_"*4)

f=open(dst,'w')
f.write(space_content)
f.close()