DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=re.split(r'[\[\]]',l)
        r+=[l]
        pass

#part 1
c=0
for s in r:
    x=0
    for a in s[::2]:
        if re.search(r'(.)(?!\1)(.)\2\1',a):x=1
    for b in s[1::2]:
        if re.search(r'(.)(?!\1)(.)\2\1',b):x=0
    c+=x
print(c)

#part 2
c=0
for s in r:
    p=set()
    for a in s[::2]:
        for i in range(len(a)-2):
            x,y,z=a[i:i+3]
            if x==z!=y:
                p|={y+x+y}
    c+=any(v in b for b in s[1::2]for v in p)

print(c)
