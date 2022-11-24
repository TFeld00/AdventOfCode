DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split('-'))]
        r+=[l]

block=set()
for a,b in r:
    n=set()
    o=0
    for x,y in block:
        if a<=x<=b or x<=a<=y:
            n|={(min(a,x),max(b,y))}
            o=1
        else:
            n|={(x,y)}
    if not o:n|={(a,b)}
    block = n

r=[]
p=0
for a,b in sorted(block):
    r+=range(p+1,a)
    p=b

#part 1
print(min(r))

#part 2
print(len(r))

#Alternative
p1=None
p2=0
p=-1
for a,b in sorted(block):
    p2 += max(0,a-p-1)
    if p1==None and a>p+1:
        p1=p+1
    p=b

#part 1
print(p1)

#part 2
print(p2)