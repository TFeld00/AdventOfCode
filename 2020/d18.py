import os
DAY,_,_=__file__.rpartition('.')

import re

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

def calc(s):
    if '('in s:
        s=re.sub(r'\([^()]+\)',lambda m:str(calc(m[0][1:-1])),s)
        return calc(s)
    else:
        l=s.split()
        r=int(l[0])
        for o,n in zip(*[iter(l[1:])]*2):
            if o=='+':
                r+=int(n)
            elif o=='*':
                r*=int(n)
        return r

def calc2(s):
    if '('in s:
        s=re.sub(r'\([^()]+\)',lambda m:str(calc2(m[0][1:-1])),s)
        return calc2(s)
    else:
        l=s.split('*')
        r=[]
        for v in l:
            r+=str(eval(v)),
        return eval('*'.join(r))

print (sum(map(calc,r)))
print (sum(map(calc2,r)))