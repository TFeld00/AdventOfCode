DAY,_,_=__file__.rpartition('.')

from alg.util import get_neigbors_both

from alg.file import download_input
download_input(DAY)

r=[]
with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[list('.'+l+'.')]        
        
W,H=len(r[0]),len(r)

a=list('.'*W)
r=a,*r,a

s=0
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='@' and sum(v=='@'for _,_,v in get_neigbors_both(r,i,j))<4:
            s+=1
print(s)

# ---

q=[]
s=0
for i,l in enumerate(r):
    for j,c in enumerate(l):
        if c=='@' and sum(v=='@'for _,_,v in get_neigbors_both(r,i,j))<4:
            q+=(i,j),
for i,j in q:
    N=[*get_neigbors_both(r,i,j)]
    if r[i][j]=='@' and sum(v=='@'for _,_,v in N)<4:
        r[i][j]='x'
        for y,x,w in N:
            if w=='@':
                q+=[(y,x)]
        s+=1
print(s)