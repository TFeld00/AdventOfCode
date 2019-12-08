I=''
W,H=25,6
with open('8.txt','r')as F:
    for l in F:
        I+=l.strip()

s=W*H
l=[I[i:i+s]for i in xrange(0,len(I),s)]

m=min(l,key=lambda x:x.count('0'))
print m.count('1')*m.count('2')


r=[2]*W*H

for i in l:
    for j,v in enumerate(i):
        v=int(v)
        if 2==r[j]and v<2:r[j]=v

for i in range(H):
    print''.join(' #-'[v]for v in r[i*W:i*W+W])
