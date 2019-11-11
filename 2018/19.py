l=[]
with open('19.txt','r')as f:
 for line in f:
  l+=[line[:-1].split()]

ip=int(l[0][1])
l=l[1:]

def opt(op,r,A,B,C):
 x=r[:]
 x[C]=op(r,A,B)
 return x

def addr(r,A,B,C):return opt(lambda r,a,b:r[a]+r[b],r,A,B,C)
def addi(r,A,B,C):return opt(lambda r,a,b:r[a]+b,r,A,B,C)
def mulr(r,A,B,C):return opt(lambda r,a,b:r[a]*r[b],r,A,B,C)
def muli(r,A,B,C):return opt(lambda r,a,b:r[a]*b,r,A,B,C)
def banr(r,A,B,C):return opt(lambda r,a,b:r[a]&r[b],r,A,B,C)
def bani(r,A,B,C):return opt(lambda r,a,b:r[a]&b,r,A,B,C)
def borr(r,A,B,C):return opt(lambda r,a,b:r[a]|r[b],r,A,B,C)
def bori(r,A,B,C):return opt(lambda r,a,b:r[a]|b,r,A,B,C)

def setr(r,A,B,C):return opt(lambda r,a,b:r[a],r,A,B,C)
def seti(r,A,B,C):return opt(lambda r,a,b:a,r,A,B,C)

def gtir(r,A,B,C):return opt(lambda r,a,b:a>r[b],r,A,B,C)
def gtri(r,A,B,C):return opt(lambda r,a,b:r[a]>b,r,A,B,C)
def gtrr(r,A,B,C):return opt(lambda r,a,b:r[a]>r[b],r,A,B,C)
def eqir(r,A,B,C):return opt(lambda r,a,b:a==r[b],r,A,B,C)
def eqri(r,A,B,C):return opt(lambda r,a,b:r[a]==b,r,A,B,C)
def eqrr(r,A,B,C):return opt(lambda r,a,b:r[a]==r[b],r,A,B,C)

l=[map(eval,o) for o in l]
reg=[0]*6

#reg[0]=1
#reg = [1, 3, 5, 4522447, 10551275, False] 
i=reg[ip]
x=0
while i<len(l):
 x+=1
 reg[ip]=i
 op,a,b,c = l[i]
 TEMP=reg[0]
 reg=op(reg,a,b,c)
 i=reg[ip]+1
 if TEMP!=reg[0]:print reg,x
print x
print reg
