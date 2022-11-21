DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

#part 1
print(sum(map(int,re.findall(r'-?\d+',s))))

#part 2
d=eval(s)

def f(d):
    r=0
    if type(d)==dict:
        w=d.values()
        if 'red' in w:
            return 0
    elif type(d)==list:
        w=d
    else:
        w=[d]
    for v in w:
        if type(v)==int:
            r+=v
        elif type(v)==list:
            r+=sum(f(x) for x in v)
        elif type(v)==dict:
            r+=f(v)
    return r
print(f(d))