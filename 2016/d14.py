DAY,_,_=__file__.rpartition('.')

import re
from hashlib import md5

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s=l

i=0
h={}
p=[]
while 1:
    x=md5(str.encode(s+str(i),'ascii')).hexdigest()

    b=re.search(r'(.)\1\1\1\1',x)
    if b:
        c=b[0][0]
        for j in h.get(c,[]):
            if j>=i-1000:
                p+=j,
        del h[c]
    a=re.search(r'(.)\1\1',x)
    if a:
        c=a[0][0]
        h[c]=h.get(c,[])+[i]
    if len(p)>=64 and i>max(p)+1000:
        break
    i+=1

print(sorted(p)[63])

#part 2
i=0
h={}
p=[]
while 1:
    x=md5(str.encode(s+str(i),'ascii')).hexdigest()
    for _ in range(2016):
        x=md5(str.encode(x,'ascii')).hexdigest()

    b=re.search(r'(.)\1\1\1\1',x)
    if b:
        c=b[0][0]
        for j in h.get(c,[]):
            if j>=i-1000:
                p+=j,
        del h[c]
    a=re.search(r'(.)\1\1',x)
    if a:
        c=a[0][0]
        h[c]=h.get(c,[])+[i]
    if len(p)>=64 and i>max(p)+1000:
        break
    i+=1
print(sorted(p)[63])