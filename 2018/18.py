import time
VIS=0
m=[]
with open('18.txt','r')as f:
 for line in f:
  m+=[list(line[:-1])]


w=len(m[0])
h=len(m)
MAX=1000000000
R=[]
for _ in range(510):
 M=[l[:]for l in m]
 for i in range(w):
  for j in range(h):
   x=m[j][i]
   s=sum([l[max(0,i-1):i+2]for l in m[max(0,j-1):j+2]],[])
   if x=='.':
    if s.count('|')>=3:
     M[j][i]='|'
   elif x=='|':
    if s.count('#')>=3:
     M[j][i]='#'
   elif x=='#':
    if s.count('#')>1 and '|' in s:pass
    else:
     M[j][i]='.'

 m=[l[:]for l in M]
 if VIS:
  print'\n'.join(['']*4+[''.join(l)for l in m])
  time.sleep(.1)
 S=sum(m,[])
 T=S.count('|')
 L=S.count('#')
 r=T*L
 R+=[r]

A=R.index(226806)
B=R.index(226806,A+1)
print A,B, B-A
print R[A:B]
print R[A:B][(MAX-A)%28]
print
print R[A:B][(MAX-A-1)%28]
print R[A:B][(MAX-A+1)%28]
