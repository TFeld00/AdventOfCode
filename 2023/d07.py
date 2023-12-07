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
    m=c.most_common()
    return [order(m),high]

def value2(h):
    high=[*map(s2.find,h)]
    c=Counter(h.replace('J',''))
    m=c.most_common()
    j=h.count('J')
    if not m:m=[['J',0]]
    m=[*map(list,m)]
    m[0][1]+=j
    return [order(m),high]

def order(m):
    if m[0][1]==5:v=5
    elif m[0][1]==4:v=4
    elif m[0][1]==3 and m[1][1]==2:v=3
    elif m[0][1]==3:v=2
    elif m[0][1]==2 and m[1][1]==2:v=1
    elif m[0][1]==2:v=0
    else:v=-1
    return v

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        a,b=l.split()
        r+=[[a,int(b)]]
        
for f in value1, value2:
    print(sum(i*b for i,(a,b) in enumerate(sorted(r,key=lambda h:f(h[0])),1)))

