import collections

reg=''
with open('20.txt','r')as f:
 for line in f:
  reg+=line[:-1]


print len(reg)


def path(x,y,r,m):
 i=0
 while i<len(r):
  c=r[i]
  if c=='(':
   p=1
   l=[]
   t=i+1
   for j in xrange(i+1,len(r)):
    C=r[j]
    if C==')':p-=1
    elif C=='(':p+=1
    elif C=='|' and p==1:
     l+=[r[t:j]];t=j+1
    if p==0:break
   l+=[r[t:j]]
   for v in l:
    path(x,y,v,m)
   i=j
  elif c in'NS':
   a=' S'.find(c)
   m[(x,y+a)]='-'
   y+=2*a
   m[(x,y)]='.'
  elif c in'WE':
   a=' E'.find(c)
   m[(x+a,y)]='|'
   x+=2*a
   m[(x,y)]='.'
  i+=1


x,y=0,0
m={(x,y):'X'}

path(x,y,reg[1:-1],m)
m[(x,y)]='X'
print len(m)

x,y=zip(*m.keys())
minX,maxX=min(x),max(x)
minY,maxY=min(y),max(y)

w=maxX-minX+1
h=maxY-minY+1

print w,h
M=[list('#'*w)for _ in range(h)]

for x,y in m:
 M[y-minY][x-minX]=m[(x,y)]

with open('20.ppm','w') as f:
 f.write('P3\n')
 f.write(str(w)+' '+str(h)+' 1\n')
 for l in M:
   f.write('  '.join(['1 1 1','0 0 0','1 0 0','0 0 1','0 1 1']['.#X|-'.find(p)]for p in l)+'\n')

print sum(l.count('.')for l in M)
def BFS(root):
  visited, queue = set([root]), collections.deque([root])
  d={root:0}
  
  while queue: 
   x,y = queue.popleft()
   for (A,B)in((0,-1),(0,1),(-1,0),(1,0)):
    if m.get((x+A,y+B),'!')in'-|':
     a,b=x+2*A,y+2*B
     if (a,b)not in visited:
      visited.add((a,b))
      d[(a,b)]=d[(x,y)]+1
      queue.append((a,b))
  return d

d=BFS((0,0))
print len(d)
print sum(v>999 for v in d.values())
