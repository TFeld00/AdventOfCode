_pow = pow
from math import *
pow = _pow
r=[]
r=r[0]
s=''
for c in r:s+=f'{int(c,16):04b}'

def get_packet(s):
    v=int(s[:3],2)
    s=s[3:]
    t=int(s[:3],2)
    s=s[3:]
    if t==4:
        n=''
        while 1:
            a=s[0]
            n+=s[1:5]
            s=s[5:]
            if a=='0':
                break
        P=(v,t,n,int(n,2))
    else:
        lt=s[0]
        s=s[1:]
        if lt=='0':
            l=int(s[:15],2)
            s=s[15:]
            P=(v,t,lt,l)
        else:
            l=int(s[:11],2)
            s=s[11:]
            P=(v,t,lt,l)
    return P,s
        
def get_packets(s,count=999):
    P=[]
    while len(s)>5 and count>0:
        count-=1
        p,s = get_packet(s)
        v,t,*x=p
        if t==4:
            P+=(p,[]),
        else:
            lt,l=x
            if lt=='0':
                S=s[:l]
                s=s[l:]
                P+=(p,get_packets(S)[0]),
            else:
                p1,s=get_packets(s,l)
                P+=(p,p1),
    return P,s

packs,s=get_packets(s)

def sum_version(P):
    v=0
    for p,s in P:
        w,*x=p
        v+=w
        v+=sum_version(s)
    return v

print(sum_version(packs))

def calc(P):
    p,s=P
    v,t,*x=p
    S=[*map(calc,s)]
    if t==0:
        return sum(S)
    elif t==1:
        return prod(S)
    elif t==2:
        return min(S)
    elif t==3:
        return max(S)
    elif t==4:
        return x[-1]
    elif t==5:
        a,b=S
        return int(a>b)
    elif t==6:
        a,b=S
        return int(a<b)
    elif t==7:
        a,b=S
        return int(a==b)
    
print(calc(packs[0]))