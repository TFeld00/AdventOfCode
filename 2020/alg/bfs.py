from queue import Queue


r=[]
r="""......#..
.#......#
#.####...
.#....#..
##..#.#.#
#..#.....
#......#.
.#..#.##.""".split()


W=len(r[0])
H=len(r)
x,y=0,0

def bfs(x,y):
    q=Queue()
    s=set()
    q.put((x,y,0))
    while not q.empty():
        x,y,l=q.get()
        for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
            X,Y=x+dx,y+dy
            if (X,Y)in s:continue

            if (X,Y)==(W-1,H-1):
                print(l)
                #WIN
                return l
            
            s|={(X,Y)}
            if 0<=X<W and 0<=Y<H:
                if r[Y][X]=='.':
                    q.put((X,Y,l+1))