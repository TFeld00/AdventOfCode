DAY,_,_=__file__.rpartition('.')

from alg.string import block_print

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split()
        r+=[l]

x=1
s=0
y=0
lit=[]
for o,*l in r:
    a=o=='addx'
    for _ in ' '*(a + 1):
        lit+=x-1<=s%40<=x+1,
        s+=1
        if s%40==20:y+=x*s
    if a:
        x+=int(l[0])

print(y)
block_print(zip(*[iter(lit)]*40))