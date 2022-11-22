DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

#part 1
d={0:1}
x=0
for c in s:
    x+=[1,-1,1j,-1j]['^v<>'.find(c)]
    d[x]=d.get(x,0)+1

print(len(d))

#part 2
d={0:1}
x=y=0
for c in s:
    x+=[1,-1,1j,-1j]['^v<>'.find(c)]
    d[x]=d.get(x,0)+1
    x,y=y,x

print(len(d))
