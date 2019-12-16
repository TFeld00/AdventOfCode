
L=[]
with open('16.txt','r')as f:
 for l in f:
  L+=map(int,l)

def shift(s,start=1):
    r=[]
    for i in xrange(start,len(s)+1):
        S=0
        j=1
        for _ in xrange(i-1,len(s),i):
            m=[0,1,0,-1][j]
            j=(j+1)%4
            if m==0:continue
            for k in xrange(_,_+i):
                if k>=len(s):break
                S+=m*s[k]
        r+=abs(S)%10,
    return r


l=L[:]
for _ in xrange(100):
    l=shift(l)
print ''.join(map(str,l[:8]))



l=L[:]
offset=int(''.join(map(str,l[:7])))

LEN=len(l)
w=LEN*10000-offset
a,b=divmod(w,LEN)

l2=(l[b:]+l*a)[::-1]
for _ in xrange(100):
    l3=[]
    x=0
    for i in xrange(w):
        x+=l2[i]
        l3+=[x%10]
    l2=l3 
    print'.',
    
print
l2=l2[::-1]
print ''.join(map(str,l2[:8]))


