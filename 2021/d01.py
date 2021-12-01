DAY,_,_=__file__.rpartition('.')

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=int(l)
        r+=[l]
        pass

x=0
for a,b in zip(r,r[1:]):
    x+=a<b
print(x)

y=0
for a,b in zip(r,r[3:]):
    y+=a<b
print(y)