DAY,_,_=__file__.rpartition('.')

from collections import Counter

from alg.file import download_input
download_input(DAY)

r=[]

s1='AKQJT98765432'[::-1]
s2='AKQT98765432J'[::-1]

def value1(h):
    high=[*map(s1.find,h)]
    c=Counter(h)
    m=[c for _,c in c.most_common()]
    return [m,high]

def value2(h):
    high=[*map(s2.find,h)]
    c=Counter(h.replace('J',''))
    m=[c for _,c in c.most_common()]or[0]
    m[0]+=h.count('J')
    return [m,high]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split()
        r+=[[a,int(b)]]
        
for f in value1, value2:
    print(sum(i*b for i,(a,b) in enumerate(sorted(r,key=lambda h:f(h[0])),1)))

