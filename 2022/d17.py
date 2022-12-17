DAY,_,_=__file__.rpartition('.')

from img.img import write_img_fromlist

from alg.file import download_input
download_input(DAY)

s=''

with open(f'{DAY}.txt','r')as F:
    for l in F:
        l=l.rstrip('\n')
        s+=l

rocks=[
    {3,2,1,0},
    {1+2j,1j,1+1j,2+1j,1},
    {2+2j,2+1j,0,1,2},
    {3j,2j,1j,0},
    {1j,1+1j,0,1}
]

def draw(b,n):
    y={int(v.imag) for v in (b|n)}
    for i in range(max(y),-1,-1):
        s='|'
        for j in range(7):
            v=j+i*1j
            s+='#' if v in b else '@' if v in n else '.'
        s+='|'
        print(s)
    print('+-------+')
    print()

moves=[[-1,1][c=='>']for c in s]
b=set()
h=0
i=0
###part 2
R=len(rocks)
##
_=0
last=[]
seen=set()
heights=[]
rep=0
while 1:
    n=rocks[_%R]
    _+=1
    n={2+(h+3)*1j + v for v in n}
    while 1:
        m=moves[i%len(moves)]
        i+=1
        N={v+m for v in n}
        if N-b==N and all(0<=v.real<7 for v in N):
            n=N
        N={v-1j for v in n}
        if N&b or min(v.imag for v in N)<0:
            h=max(h,int(max(v.imag for v in n))+1)
            b|=n
            break
        else:
            n=N
    heights+=h,
    if not rep:
        top=tuple((v-h*1j)for v in b if h-5<=v.imag)
        pos=(_%R,i%len(moves),top)
        if pos in seen:
            repStart=last.index(pos)
            repEnd = _-1
            rep=repEnd-repStart
            B=h
            A=heights[repStart]
            X,Y=divmod(1000000000000-repStart,rep)
            C=heights[repStart+Y-1]
        else:
            seen|={pos}
            last+=pos,
    if _==2022: #part 1
        print(h)
    if rep and _>=2022:
        break

#part 2
print((B-A)*X+C)

# image
COLS = {
    1: (255, 255, 255),
    0: (0, 0, 0),
}

l=[[0]*7 for _ in range(h)]

for v in b:
    x,y=int(v.real),int(v.imag)
    l[~y][x]=1
write_img_fromlist(l,'2022/d17',COLS)
