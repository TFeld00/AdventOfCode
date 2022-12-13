DAY,_,_=__file__.rpartition('.')

from alg.util import parse_no_headers
from functools import cmp_to_key

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

r=parse_no_headers(r)

def cmp(a,b):
    if type(a)==type(b)==int:
        return (a>b)-(a<b)
    elif type(a)==type(b)==list:
        for x,y in zip(a,b):
            if (v:=(cmp(x,y))):return v
        return cmp(len(a),len(b))
    elif type(b)==list:
        return cmp([a],b)
    else:
        return cmp(a,[b])
    
#part 2
d1,d2=[[2]],[[6]]
X=[d1,d2]

#part 1
s=0
for i,(a,b) in enumerate(r,1):
    a=eval(a)
    b=eval(b)
    X+=a,b #part 2
    if cmp(a,b)<0:
        s+=i
print(s) #part 1

#part 2
X.sort(key=cmp_to_key(cmp))
print(-~X.index(d1)*-~X.index(d2))
