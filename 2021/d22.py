DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]
s=0

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')

        a,b=l.split()
        a=a=='on'
        b=[v.split('..')for v in b.split(',')]
        b=[(int(x[2:]),int(y))for x,y in b]

        r+=[(a,*b)]

#part 1 (naive)
d={}
for s,xr,yr,zr in r:
    for x in range(max(-50,xr[0]),min(51,xr[1]+1)):
        for y in range(max(-50,yr[0]),min(51,yr[1]+1)):
            for z in range(max(-50,zr[0]),min(51,zr[1]+1)):
                d[(x,y,z)]=s

print(sum(d.values()))

#part 2
def line_overlap(r,R):
    a,b=r
    c,d=R
    y,x= min(b,d),max(a,c)
    if x<=y:return x,y,(y-x+1)
    return 0,0,0

def get_overlap(a,b):
    xr,yr,zr=a
    XR,YR,ZR=b
    *x_overlap,x = line_overlap(xr,XR)
    *y_overlap,y = line_overlap(yr,YR)
    *z_overlap,z = line_overlap(zr,ZR)
    return (*x_overlap,),(*y_overlap,),(*z_overlap,),x*y*z

on=0
seen=[]
for s,xr,yr,zr in r:
    x,X=xr;y,Y=yr;z,Z=zr
    o=0
    if s:o=(X-x+1)*(Y-y+1)*(Z-z+1)
    next_seen=[]
    for S,XR,YR,ZR in seen:
        a,b,c,d=get_overlap((xr,yr,zr),(XR,YR,ZR))
        if d:
            next_seen+=[(not S,a,b,c)]
            if S:o-=d
            else:o+=d
    seen+=next_seen
    on+=o
    if s:
        seen+=[(s,xr,yr,zr)]
print(on)