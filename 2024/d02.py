DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]
s=0
t=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,l.split())]
        r+=[l]

# Part 1  
s=0
for x in r:
    d={b-a for a,b in zip(x,x[1:])}
    
    if d<={1,2,3} or d<={-1,-2,-3}:s+=1
print(s)

#Part 2
s=0
for x in r:
    for i in range(len(x)):
        y=x[:i]+x[i+1:]
        d={b-a for a,b in zip(y,y[1:])}
    
        if d<={1,2,3} or d<={-1,-2,-3}:s+=1;break
print(s)