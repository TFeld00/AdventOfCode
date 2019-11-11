l=[]
with open('17.txt','r')as f:
 for line in f:
  a,b=line.split(', ')
  t=[map(int,a[2:].split('..'))*2,map(int,b[2:].split('..'))]
  if a[0]=='x':l+=[t]
  else:l+=[t[::-1]]

X=sum(zip(*l)[0],[])
minX,maxX=min(X)-2,max(X)+2
Y=sum(zip(*l)[1],[])
minY,maxY=min(Y),max(Y)

print minX,maxX
print minY,maxY
w=maxX-minX+1
h=maxY+1
m=[list('.'*w)for _ in range(h)]

for (a,b),(c,d) in l:
 for i in range(a,b+1):
  for j in range(c,d+1):
   m[j][i-minX]='#'

m[0][500-minX]='+'
g=0
stack=[(500-minX,1)]
while stack:
#for i in range(1500):
 g+=1
 x,y=stack[-1]
 if m[y][x]=='.':m[y][x]='|'
 if y>=maxY or x<=0 or x>=w-1:stack.pop();continue
 if m[y+1][x]=='.':
  m[y][x]='|'
  stack+=[(x,y+1)]
 elif m[y+1][x]in'#~':
  s=''.join(m[y])
  s1=s[:x].rpartition('#')[2]
  s2=s[x+1:].split('#',1)[0]
  sb=m[y+1][x-len(s1):x+len(s2)+1]
  if set(sb)<=set('#~'):
   stack.pop()
   m[y][x-len(s1):x+len(s2)+1]=['~']*len(sb)
  elif m[y][x-1]+m[y][x+1]=='||':
   stack.pop()
  else:
   if m[y][x]=='!':m[y][x]='|';stack.pop()
   m[y][x]='!'
  if m[y][x-1]=='.':
   stack+=[(x-1,y)]
  if m[y][x+1]=='.':
   stack+=[(x+1,y)]
 else:stack.pop()
print w,h

if stack:
 x,y=stack[-1]
 m[y][x]='+'

with open('17.ppm','w') as f:
 f.write('P3\n')
 f.write(str(w)+' '+str(h)+' 1\n')
 for l in m:
   f.write('  '.join(['1 1 1','0 0 0','1 0 0','0 0 1','0 1 1']['.#+~|'.find(p)]for p in l)+'\n')

print'-'
print g
print'-'
print len(stack)
print stack[-5:]
print'-'

print sum(c in'~'for l in m[minY:1921]for c in l)
