DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]

a,b=0,0
c=0
for s in r:
    a+=len(s)
    b+=len(eval(s))
    c+=len(s)+s.count('"')+s.count('\\')+2

#part 1
print(a-b)

#part 2
print(c-a)
