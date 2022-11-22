from Queue import *
m=[]
with open('25.txt','r')as f:
 for line in f:
  m+=[line.split()]
print m


def get(v):
    if v in reg:
        return reg[v]
    return int(v)
    
def cpy(x,y):
    if y in reg:
        reg[y]=get(x)
def inc(x):
    if x in reg:
        reg[x]+=1
def dec(x):
    if x in reg:
        reg[x]-=1
def jnz(x,y):
    if get(x):
        return get(y)
    return 1
def tgl(c,*v):
    if len(v)==1:
        if c=='inc':return'dec'
        return'inc'
    if len(v)==2:
        if c=='jnz':return'cpy'
        return'jnz'
def out(x):
    return get(x)
def func(c):
    if c=='cpy':return cpy
    if c=='inc':return inc
    if c=='dec':return dec
    if c=='jnz':return jnz
    if c=='tgl':return tgl
    if c=='out':return out

def state(reg,p):
    return (reg['a'],reg['b'],reg['c'],reg['d'],p)
p=0
#reg['a']=0
A=0
a=A
while 1:
    if a>A+1e6:break
    a+=1
    reg={'a':a,'b':0,'c':0,'d':0}
    CL=[]
    p=0

    while p<len(m):
        l=m[p]
        c=l[0]
        v=l[1:]
        if c=='jnz':
            p+=jnz(*v)
        elif c=='out':
            CL+=[out(*v)]
            p+=1
            if CL[10:] and CL[-1]==CL[-2]:print a,CL;break
        elif c=='tgl':
            d=get(*v)
            if 0<=p+d<len(m):
                m[p+d][0]=tgl(*m[p+d])
            p+=1
        else:
            f=eval(c)
            f(*v)
            p+=1

        if len(CL)>60:
            print a
            print CL
            1/0
print a,CL,reg
