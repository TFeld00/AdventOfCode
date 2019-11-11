import collections
import time

DEB=0

HP=200
M=''
m=map(list,"""################################
###########################..###
##########################...###
#########################..#####
####...##################.######
#####..################...#.####
#..G...G#########.####G.....####
#.......########.....G.......###
#.....G....###G....#....E.....##
####...##......##.............##
####G...#.G...###.G...........##
####G.......................####
####.........G#####.........####
####...GG#...#######.......#####
###.........#########G....######
###.G.......#########G...#######
###.G.......#########......#####
####.....G..#########....E..####
#####.......#########..E....####
######...##G.#######........####
######.#.#.G..#####.....##..####
########....E...........##..####
########....E#######........####
########......######E....##..E.#
########......#####.....#......#
########.....######............#
##################...#.E...E...#
##################.............#
###################.......E#####
####################....#...####
####################.###########
################################""".split('\n'))




C=[]
for i in range(len(m)):
 for j in range(len(m[0])):
  x=m[i][j]
  t='GE'.find(x)
  if t>-1:
   C+=[[(i,j),t,HP]]

def bfs(root,P):
  visited, queue = set([root]), collections.deque([root])
  d={root:(0,None)}
  R=set()
  while queue: 
   x,y = queue.popleft()
   for (a,b)in((x,y-1),(x,y+1),(x-1,y),(x+1,y)):
    if m[b][a]=='.':
     if (a,b)not in visited: 
      visited.add((a,b))
      d[(a,b)]=(d[(x,y)][0]+1,(x,y))
      queue.append((a,b))
      if(a,b)in P:
       R|={(d[(a,b)],b,a)}
  if R:
   (l,p),y,x=min(R,key=lambda((l,p),y,x):(l,y,x))
   E=(x,y)
   while p and p!=root:
    x,y=p
    (l,p)=d[p]
     # return(x,y)
   A=(x,y)
   (l,p),y,x=min(R,key=lambda((l,p),y,x):(l,y,x))
   visited, queue = set(), collections.deque([(x,y)])
   d={(x,y):(0,None)}
   R=set()
   if l==1:R|={(d[(x,y)],y,x)}
   X,Y=root
   while queue:
    x,y = queue.popleft()
    for (a,b)in((x,y-1),(x,y+1),(x-1,y),(x+1,y)):
     if m[b][a]=='.':
      if (a,b)not in visited: 
       visited.add((a,b))
       d[(a,b)]=(d[(x,y)][0]+1,(x,y))
       queue.append((a,b))
       if(a,b)in ((X,Y-1),(X,Y+1),(X-1,Y),(X+1,Y)):
        R|={(d[(a,b)],b,a)}
   (l,p),y,x=min(R,key=lambda((l,p),y,x):(l,y,x))
   B=(x,y)
   #if A!=B:print A,B,R
   return B

ATK=[3,20]
STOP=0
for _ in range(1,201):
 if DEB:print _
 C=sorted(C)
 for c in sorted(C):
  if len(set(zip(*C)[1]))==1:
   STOP=1
   break
  (y,x),t,h=c
  if h<=0:continue
  X,Y=x,y
  P={(a,b)for (b,a),T,h in C if t!=T}
  H={(a,b):h for (b,a),T,h in C if t!=T}
  
  f=[(a,b)for a,b in((x,y-1),(x,y+1),(x-1,y),(x+1,y))if(a,b)in P]
  F=min(f,key=lambda (x,y):(H[(x,y)],y,x))if f else 0
  if not F:
   Q={(a,b)for z,w in P for(a,b)in((z,w-1),(z,w+1),(z-1,w),(z+1,w))if m[b][a]=='.'}
   N=bfs((x,y),Q)
   #move
   if N:
    X,Y=N
    if DEB:print'GE'[t],'MOVE ',(x,y),(X,Y)
    m[y][x]='.';m[Y][X]='GE'[t]
    f=[(a,b)for a,b in((X,Y-1),(X,Y+1),(X-1,Y),(X+1,Y))if(a,b)in P]
    F=min(f,key=lambda (x,y):(H[(x,y)],y,x))if f else 0
  if F:
   #fight
   if DEB:print'GE'[t],'FIGHT',(X,Y),F,'\t',f,[H[n]for n in f]
   e=[b for b in C if b[0][::-1]==F][0]
   e[2]-=ATK[t]
   if e[2]<=0:
    print 'DED',_,
    if not t:print 'DEADELF!!!',1/0
    y,x=e[0]
    m[y][x]='.'
    C.pop(C.index(e))
  c[:]=[(Y,X),t,h]
 if STOP:_-=1
 if len(set(zip(*C)[1]))==1:
  break


#if 1:
 M=[l[:]for l in m]
# for(y,x),t in C:
#  M[y][x]='GE'[t]
 print'\n'.join(['']*10+[str(_)]+[''.join(l)for l in M])
 #time.sleep(.1)

ROUNDS=_
HEALTH=sum(zip(*C)[2])
print ROUNDS
print HEALTH
print ROUNDS * HEALTH
