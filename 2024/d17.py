DAY,_,_=__file__.rpartition('.')

from itertools import zip_longest
import re

from alg.file import download_input
download_input(DAY)

r=[]

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        l=[*map(int,re.findall('-?\d+',l))]
        r+=l
        
A,B,C,*L=r

def run(newA):
    A,B,C,*L=r
    A=newA
    def combo(i):
        return [0,1,2,3,A,B,C][i]

    out=[]
    i=0
    while i<len(L):
        o,a=L[i:i+2]
        if o==0:
            A//=2**combo(a)
        elif o==1:
            B^=a
        elif o==2:
            B=combo(a)%8
        elif o==3:
            if A:
                i=a-2
        elif o==4:
            B^=C
        elif o==5:
            out+=combo(a)%8,
            #if not all(x==y for x,y in zip(out,L)):return []
        elif o==6:
            B=A//2**combo(a)
        elif o==7:
            C=A//2**combo(a)
        i+=2


    return out

def run2(A):
    B=C=0
    out=[]
    while A:
        #2,4
        B=A%8
        #1,7
        B^=7
        #7,5
        C=A//2**B
        #0,3
        A//=8
        #4,4
        B^=C
        #1,7
        B^=7
        #5,5
        out+=B%8,
        #3,0
    return out

def run3(A):
    out=[]
    while A:
        out+=(A%8)^(A>>((A%8)^7))%8,
        A//=8
    return out

print(','.join(map(str,run3(A))))


# Part 2

### From run3 above:
### Each output-digit is the XOR of current 3-bit digit, and 3-bit digit at offset equal to value
### getMoves(d) returns each possible bitmask for a given output digit.

def mergeIfValid(a,b):
    s=''
    valid=1
    for v,w in zip_longest(a,b,fillvalue='?'):
        if v==w or '?' in v+w:
            s+=min(v,w)
        else:valid=0
    if valid:
        return s.rstrip('?')

def getMoves(d):
    for i in range(8):
        p='?'*7+'{0:03b}'.format(i)
        n='?'*i+'{0:03b}'.format(i^d)+'?'*(i^7)
        
        s=mergeIfValid(p,n)
        if s:
            yield s

# BFS for each digit, if bitmasks can overlap.
val={'0'*7}
for i,d in enumerate(L[::-1]):
    next=set()
    for m in getMoves(d):
        for v in val:
            s=mergeIfValid(v,'?'*i*3+m)
            if s:next|={s}
    val = next

print(int(min(val),2))