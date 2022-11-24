DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n.')
        _,d,_,w,*_,p,=l.split()
        r+=[(int(d[1:]),int(w),int(p))]

#part 1
i=0
while 1:
    if all((d+p+i)%w==0 for d,w,p in r):break
    i+=1

print(i)

#part 2
r+=[(7,11,0)]
i=0
while 1:
    if all((d+p+i)%w==0 for d,w,p in r):break
    i+=1

print(i)