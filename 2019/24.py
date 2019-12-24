from collections import *
import sys

m=[]
with open('24.txt','r')as f:
 for l in f:
  m+=[int(c=='#')for c in l.rstrip('\n')]

m=sum(2**i*v for i,v in enumerate(m))

#-- PART 1 --
def draw(m):
    s=''
    for i in range(25):
        s+='.#'[m&(2**i)>0]
        if i%5==4:print s;s=''
    print

def life(i,m):
    a=0
    if i>4:
        j=2**(i-5)
        a+=m&j>0
    if i<20:
        j=2**(i+5)
        a+=m&j>0
    if i%5>0:
        j=2**(i-1)
        a+=m&j>0
    if i%5<4:
        j=2**(i+1)
        a+=m&j>0
    j=2**i
    
    if m&j and a!=1:return 0
    if not m&j and 0<a<3:return j
    return m&j

s={m}
while 1:
    m=sum(life(i,m)for i in range(25))
    if m in s:
        break
    s|={m}
print m


#-- PART 2 --m=[]
m=[]
with open('24.txt','r')as f:
 for l in f:
  m+=[int(c=='#')for c in l.rstrip('\n')]

def blank():
    return[0]*25

def hasInner(m):
    return any(m[i]for i in (7,11,13,17))
def hasOuter(m):
    return any(m[i]for i in (0,1,2,3,4,5,9,10,14,15,19,20,21,22,23,24))

def countNeighbors(i,l,M):
    m=M[l]
    if i==0:return M[l-1][11]+M[l-1][7]+m[1]+m[5]
    if i==1:return m[0]+M[l-1][7]+m[2]+m[6]
    if i==2:return m[1]+M[l-1][7]+m[3]+m[7]
    if i==3:return m[2]+M[l-1][7]+m[4]+m[8]
    if i==4:return m[3]+M[l-1][7]+M[l-1][13]+m[9]

    if i==5:return M[l-1][11]+m[0]+m[6]+m[10]
    if i==6:return m[5]+m[1]+m[7]+m[11]
    if i==7:return m[6]+m[2]+m[8]+sum(M[l+1][:5])
    if i==8:return m[7]+m[3]+m[9]+m[13]
    if i==9:return m[8]+m[4]+M[l-1][13]+m[14]

    if i==10:return M[l-1][11]+m[5]+m[11]+m[15]
    if i==11:return m[10]+m[6]+sum(M[l+1][j]for j in range(0,25,5))+m[16]
    if i==12:return 0
    if i==13:return sum(M[l+1][j]for j in range(4,25,5))+m[8]+m[14]+m[18]
    if i==14:return m[13]+m[9]+M[l-1][13]+m[19]

    if i==15:return M[l-1][11]+m[10]+m[16]+m[20]
    if i==16:return m[15]+m[11]+m[17]+m[21]
    if i==17:return m[16]+sum(M[l+1][20:])+m[18]+m[22]
    if i==18:return m[17]+m[13]+m[19]+m[23]
    if i==19:return m[18]+m[14]+M[l-1][13]+m[24]

    if i==20:return M[l-1][11]+m[15]+m[21]+M[l-1][17]
    if i==21:return m[20]+m[16]+m[22]+M[l-1][17]
    if i==22:return m[21]+m[17]+m[23]+M[l-1][17]
    if i==23:return m[22]+m[18]+m[24]+M[l-1][17]
    if i==24:return m[23]+m[19]+M[l-1][13]+M[l-1][17]
    
def life2(i,l,M):
    m=M[l]
    a=countNeighbors(i,l,M)
    if m[i]and a!=1:return 0
    if not m[i]and 0<a<3:return 1
    return m[i]

def gen(l,M):
    return[life2(i,l,M)for i in range(25)]

M=defaultdict(blank)
M[0]=m

minLevel=maxLevel=0
gens=200

for _ in xrange(gens):
    D={}
    for i in range(minLevel,maxLevel+1):
        D[i]=gen(i,M)
    if hasOuter(M[minLevel]):
        minLevel-=1
        D[minLevel]=gen(minLevel,M)
    if hasInner(M[maxLevel]):
        maxLevel+=1
        D[maxLevel]=gen(maxLevel,M)
    for i in range(minLevel,maxLevel+1):
        M[i]=D[i]
    
print sum(map(sum,M.values()))
#print M
