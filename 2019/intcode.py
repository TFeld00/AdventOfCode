def get(l,m,v):
    if m==1:
        return v
    if m==2:
        return l.get(v+getRB(l),0)
    return l.get(v,0)

def setV(l,m,j,v):
    if m==2:
        l[getRB(l)+j]=v
    else: l[j]=v
def getRB(l):
    return l.get('RB',0)

def setRB((l,mod,i),val):
    l['RB']=getRB(l)+val

def getB((l,(D,C,B),i)):
    return get(l,B,l[i+1])

def getC((l,(D,C,B),i)):
    return get(l,C,l[i+2])

def getD((l,(D,C,B),i)):
    return get(l,D,l[i+3])

def setB((l,(D,C,B),i),val):
    b=l[i+1]
    setV(l,B,b,val)

def setC((l,(D,C,B),i),val):
    c=l[i+2]
    setV(l,C,c,val)

def setD((l,(D,C,B),i),val):
    d=l[i+3]
    setV(l,D,d,val)

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
    try:
        v=read()
        setB(x,v)
        return move2(x)
    except:
        return [x[0],x[2]]

def out(x):
    writeOutput(getB(x))
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

def rel(x):
    v=getB(x)
    setRB(x,v)
    return move2(x)

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
    9:rel,

    99:ext
}

def move(l,i):
    a=l[i]
    mod=a/10000,a/1000%10,a/100%10
    a=a%100

    f=F.get(a,unknown)
    return f((l,mod,i))

def printF(v):
    print v

def intcode(l,inputF=input,outputF=printF):
    i=0
    global readInput
    global writeOutput
    readInput=inputF
    writeOutput=outputF
    while i in l:
        j=move(l,i)
        if j==None:return
        i=j
    return l


def intcodeUntilRead(l,i=0,inputF=input,outputF=printF):
    global readInput
    global writeOutput
    readInput=inputF
    writeOutput=outputF
    while i in l:
        j=move(l,i)
        if type(j)==list:return j
        if j==None:return
        i=j

def intcodeOnce(l,i=0,inputF=input,outputF=printF):
    global readInput
    global writeOutput
    readInput=inputF
    writeOutput=outputF
    if i not in l:return
    j=move(l,i)
    return l,j


def makeGen(*l):
    l=(v for v in l)
    return lambda:l.next()
