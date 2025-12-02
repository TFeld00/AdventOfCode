DAY,_,_=__file__.rpartition('.')

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=l.split(',')
        for v in l:
            a,b=v.split('-')
            r+=[[int(a),int(b)]]

s1=0
s2=0

def f1(n):
    a=str(n)
    if len(a)%2==0:
        w=len(a)//2
        return a[:w]==a[w:]

def f2(n):
    a=str(n)
    w=len(a)
    for i in range(1,w//2+1):
        if w%i<1:
            n=w//i
            x=a[:i]
            if x*n==a:return 1

s=0
for a,b in r:
    for n in range(a,b+1):
        if f1(n):
            s1+=n
        if f2(n):
            s2+=n

print(s1)
print(s2)
