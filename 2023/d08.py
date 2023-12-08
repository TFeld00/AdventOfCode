DAY,_,_=__file__.rpartition('.')

from math import lcm
import re

from alg.file import download_input
download_input(DAY)

moves=''
d={}

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        if not moves:moves=l
        elif l:
            a,b,c=re.findall('[A-Z]+',l)
            d[a]=[b,c]
    
def f(s):
    i=0
    while s[-1]!='Z':
        m=moves[i%len(moves)]
        i+=1
        v=d[s]
        if m>'M':
            s=v[1]
        else:
            s=v[0]
    return i

print(f('AAA'))

s=[v for v in d if v[-1]=='A']
print(lcm(*map(f,s)))