def get(l,m,v):
    if m:
        return v
    return l[v]

def getB((l,(D,C,B),i)):
    return get(l,B,l[i+1])

def getC((l,(D,C,B),i)):
    return get(l,C,l[i+2])

def getD((l,(D,C,B),i)):
    return get(l,D,l[i+3])

def setB((l,mod,i),val):
    l[l[i+1]]=val

def setC((l,mod,i),val):
    l[l[i+2]]=val

def setD((l,mod,i),val):
    l[l[i+3]]=val

def move2((l,mod,i)):return i+2
def move3((l,mod,i)):return i+3
def move4((l,mod,i)):return i+4

def add(x):
    v=getB(x)+getC(x)
    setD(x,v)
    return move4(x)

def mul(x):
    v=getB(x)*getC(x)
    setD(x,v)
    return move4(x)

def inp(x):
    v=read()
    setB(x,v)
    return move2(x)

def out(x):
    print getB(x)
    return move2(x)

def jit(x):
    if getB(x):
        return getC(x)
    return move3(x)

def jif(x):
    if not getB(x):
        return getC(x)
    return move3(x)

def vlt(x):
    v=int(getB(x)<getC(x))
    setD(x,v)
    return move4(x)

def veq(x):
    v=int(getB(x)==getC(x))
    setD(x,v)
    return move4(x)

def ext((l,(D,C,B),i)):
    return len(l)

def unknown((l,(D,C,B),i)):
    print 'unknown code: %d'%l[i]
    return None

def read():
    return readInput()

F={
    1:add,
    2:mul,
    3:inp,
    4:out,
    5:jit,
    6:jif,
    7:vlt,
    8:veq,

    99:ext
}

def move(l,i):
    a=l[i]
    mod=a/10000,a/1000%10,a/100%10
    a=a%100
    
    f=F.get(a,unknown)
    return f((l,mod,i))
    
def intcode(l,inputF=input):
    i=0
    global readInput
    readInput=inputF
    while i<len(l):
        j=move(l,i)
        if j==None:return
        i=j
    return l


def makeGen(*l):
    l=(v for v in l)
    return lambda:l.next()
