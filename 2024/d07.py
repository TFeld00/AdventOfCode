DAY,_,_=__file__.rpartition('.')

import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=[l]
        
        
def f(a,l,part):
    o=['+','*','|'][:part+1]
    s={l[0]}
    for q in l[1:]:
        s2=set()
        for v in o:
            for r in s:
                if v=='*':
                    r*=q
                elif v=='+':
                    r+=q
                else:
                    r=r*10**len(str(q))+q
                if r<=a:
                    s2|={r}
        s=s2
    return a in s


print(sum(a for a,*l in r if f(a,l,1)))

print(sum(a for a,*l in r if f(a,l,2)))

