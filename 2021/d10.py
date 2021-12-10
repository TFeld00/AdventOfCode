DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

def reduced(t):
    s=[]
    for c in t:
        if c in'([{<':
            s+=')]}>'['([{<'.find(c)],
        else:
            if s[-1]!=c:
                return 0,c
            else:s.pop()
    return 1,s

r2=[]
I=0
for l in r:
    c,s=reduced(l)
    if not c:
        I+={')':3,']':57,'}':1197,'>':25137}[s]
    else:
        r2+=[s]
print(I)


t=[]
for l in r2:
    s=0
    for c in l[::-1]:
        s*=5
        s+={')':1,']':2,'}':3,'>':4}[c]
    t+=s,
t.sort()
print(t[len(t)//2])