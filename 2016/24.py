from Queue import *
m=[]
with open('24.txt','r')as f:
 for line in f:
  m+=[list(line.strip())]

pois = [(x,y)for x,l in enumerate(m)for y,c in enumerate(l)if c.isdigit()]
print pois
print len(m),len(m[0])
P=[]
with open('24-1.ppm','r')as f:
    X=[]
    for l in f:X+=l,
    w,h=map(int,X[2].split())
    x,y=-1,0
    for a,b,c in zip(*[iter(X[4:])]*3):
        x+=1
        if x>=w:x=0;y+=1
        if not a==b==c=='255\n':
            if not m[y][x].isdigit():m[y][x]='#'

with open('20.ppm','w') as f:
 f.write('P3\n')
 f.write(str(len(m[0]))+' '+str(len(m))+' 1\n')
 for l in m:
   f.write('  '.join(['1 1 1','0 0 0','1 0 0','0 0 1','0 1 1']['.#X|-'.find(p)]for p in l)+'\n')

def bfs((a,b),t):
    q=Queue()
    q.put((a,b,0))
    s=set()
    t=set(t)
    r={}
    while not q.empty():
        x,y,l=q.get()
        s|={(x,y)}
        for dx,dy in(-1,0),(1,0),(0,-1),(0,1):
            X,Y=x+dx,y+dy
            if m[X][Y]=='#':continue
            if(X,Y)in t:
                r[(X,Y)]=l+1
                t-={(X,Y)}
                if not t:return r
            if (X,Y)in s:continue
            q.put((X,Y,l+1))
    return r



d={
    (1, 39):{(39, 131): 150, (7, 171): 214, (33, 165): 210, (19, 165): 196, (21, 9): 62, (7, 17): 48, (41, 5): 82},
    (7, 17):{(39, 131): 178, (33, 165): 238, (19, 165): 224, (21, 9): 26, (41, 5): 66, (7, 171): 242},
    (7, 171):{(33, 165): 40, (41, 5): 260, (21, 9): 252, (39, 131): 76, (19, 165): 30},
    (19, 165):{(33, 165): 30, (41, 5): 242, (21, 9): 234, (39, 131): 58},
    (21, 9):{(41, 5): 76, (33, 165): 248, (39, 131): 188},
    (33, 165):{(39, 131): 72, (41, 5): 256},
    (39, 131):{(41, 5): 192},
    (41, 5):{}
    }
i=7
#f=pois[i]
#d[f]=bfs(f,pois[i+1:])
#print f,d[f]
print
#print  d

p={(x,y):int(m[x][y])for(x,y)in pois}
D={p[a]:{p[b]:d[a][b]for b in d[a]} for a in d}
print D
d=[[0]*8 for _ in range(8)]
for a in D:
    for b in D[a]:
        d[a][b]=d[b][a]=D[a][b]
print d

def dist( p):
    r=0
    for a,b in zip((0,)+p,p+(0,)):
       r+=d[a][b]
    return r

from itertools import *
print min(map(dist,permutations(range(1,8))))
