DAY,_,_=__file__.rpartition('.')

from alg.util import rotate90clockwise, rotate180, rotate90counterclockwise
from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        r+=[l]
        
        
W,H=len(r[0]),len(r)

s=0
r = [list(l)for l in r]
for l in [*r, *(l[::-1]for l in r), *rotate90clockwise(r), *(l[::-1] for l in rotate90clockwise(r))]:
    s+=(''.join(l)).count('XMAS')

for X in r,rotate90clockwise(r),rotate180(r),rotate90counterclockwise(r):
    for i in range(len(X)-3):
        a,b,c,d=X[i:i+4]
        
        for x,y,z,w in zip(a,b[1:],c[2:],d[3:]):
            q=x+y+z+w
            s+=q=='XMAS'
print(s)

# Part 2

s=0
for i in range(H-2):
    for j in range(W-2):
        x=[l[j:j+3]for l in r[i:i+3]]
        for y in [x,rotate180(x),rotate90clockwise(x),rotate90counterclockwise(x)]:
            s+= y[0][0]==y[0][2]=='M' and y[1][1]=='A' and y[2][0]==y[2][2]=='S'
print(s)