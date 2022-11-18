DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

import hashlib

#part 1
n=1
while 1:
    h = hashlib.md5(bytes(s+str(n),'ascii')).hexdigest()
    if h[:5]=='0'*5:break
    n+=1
print(n)

#part 2
while 1:
    h = hashlib.md5(bytes(s+str(n),'ascii')).hexdigest()
    if h[:6]=='0'*6:break
    n+=1
print(n)