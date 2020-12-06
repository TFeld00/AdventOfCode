from queue import Queue

q=Queue()
s=set()

r=[]
r="""......#..
.#......#
#.####...
.#....#..
##..#.#.#
#..#.....
#......#.
.#..#.##.""".split()

maxX=len(r[0])
maxY=len(r)
x,y=0,0
q.put((x,y,0))

while not q.empty():
    x,y,l=q.get()
    for dx,dy in (0,1),(0,-1),(1,0),(-1,0):
        X,Y=x+dx,y+dy
        if (X,Y)in s:continue
        if (X,Y)==(maxX-1,maxY-1):
            print(l)
            #WIN
        s|={(X,Y)}
        if 0<=X<maxX and 0<=Y<maxY:
            if r[Y][X]=='.':
                q.put((X,Y,l+1))