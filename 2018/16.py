l=[]
p=[]
while 1:
 try:
  x=raw_input()
  if x[:1]=='B':
   a=eval(x.split(' ',1)[1])
   o=map(int,raw_input().split())
   b=eval(raw_input().split(' ',1)[1])
   l+=[[a,o,b]]
   a=raw_input()
  else:p+=[x]
 except:
  break

p=[map(int,l.split())for l in p[2:]]

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

reg=[0]*4
total=0
O={}
ops={11:eqrr,7:eqri,13:eqir,12:gtri,3:gtrr,0:gtir,6:banr,8:bani,14:setr,2:seti,9:addr,5:borr,4:bori,10:addi,15:muli,1:mulr}

for o,a,b,c in p:
 reg=ops[o](reg,a,b,c)
print reg
