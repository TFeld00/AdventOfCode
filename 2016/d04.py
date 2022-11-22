DAY,_,_=__file__.rpartition('.')

from collections import *
from alg.string import shift_caesar

from alg.file import download_input
download_input(DAY)

r=[]
n=0
s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.rsplit('-',1)
        b,c=b[:-1].split('[')
        r+=[(a,int(b),c)]
        pass

#part 1
s=0
for a,b,c in r:
    m=Counter(sorted(a.replace('-',''))).most_common(5)
    if c==''.join(x for x,_ in m):
        s+=b
print(s)

#part 2
for a,b,c in r:
    a=shift_caesar(a,b).replace('-','')
    if 'pole' in a:
        print(a,b)