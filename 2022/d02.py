DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]
        pass

s=0
A,B='ABC','XYZ'
for a,b in r:
    a=A.find(a)
    b=B.find(b)
    d=(a-b)%3
    s+=[3,0,6][d] + b+1
print(s)


s=0
A,B='ABC','YXZ'
for a,b in r:
    a=A.find(a)
    d=(B.find(b))

    b=(a-d)%3
    s+=[3,0,6][d] + b+1
print(s)